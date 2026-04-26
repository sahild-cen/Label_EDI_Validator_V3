"""
ZPL Raw Data Extractor
=======================
Extracts ALL data from a ZPL script into a structured format
that the validator can match against rules.

This parser makes ZERO assumptions about what each field "is".
It just extracts:
  - Every text block (^FD) with its position
  - Every barcode command and its data
  - Every graphic element (decoded to PIL Image)
  - Every ZPL command present

The validator then uses the "detect_by" field from the rules
to find each required element in this raw data.
"""

import re
from typing import Dict, Any, List, Optional

try:
    from PIL import Image
except ImportError:
    Image = None


# ═══════════════════════════════════════════════════════════════
# ^GF GRAPHIC DECODER
# ═══════════════════════════════════════════════════════════════
# Decodes ZPL ^GFA compressed hex data into PIL Images.
# Handles:
#   - ASCII hex (0-9, A-F)
#   - ZPL compression: G-Y = repeat 1-19, g-y = repeat 20-380
#   - Row controls: colon = repeat previous row,
#     comma = fill rest with 0, bang = fill rest with F
#   - Multi-line data (newlines inside data block)
# ═══════════════════════════════════════════════════════════════

_HEX_CHARS = set("0123456789ABCDEFabcdef")


def _extract_gf_data_block(script: str, data_start: int) -> str:
    """
    Extract the raw data block after ^GFA,total,total,bpr,
    Reads until the next ^ command. Handles multi-line data
    (DHL labels embed newlines inside graphic data).
    """
    end = data_start
    length = len(script)
    while end < length:
        if script[end] == "^":
            break
        end += 1
    return script[data_start:end]


def _decompress_zpl_gf(data: str, bytes_per_row: int) -> List[str]:
    """
    Decompress ZPL ^GF ASCII-hex data into rows of hex strings.

    Compression codes:
        G-Y   repeat next hex char 1-19 times
        g-y   repeat next hex char 20-380 times (multiples of 20)
        g-y followed by G-Y: additive (e.g. gH = 20+2 = 22 repeats)
        :     repeat the entire previous row
        ,     fill remainder of current row with 0 (white)
        !     fill remainder of current row with F (black)
    """
    hex_per_row = bytes_per_row * 2
    if hex_per_row == 0:
        return []

    rows: List[str] = []
    current_row = ""
    prev_row = "0" * hex_per_row

    i = 0
    length = len(data)

    while i < length:
        ch = data[i]

        # ── Row-level controls ──
        if ch == ":":
            # Flush any partial current row first
            if current_row:
                current_row = current_row.ljust(hex_per_row, "0")[:hex_per_row]
                rows.append(current_row)
                prev_row = current_row
                current_row = ""
            rows.append(prev_row)
            i += 1
            continue

        if ch == ",":
            current_row = current_row.ljust(hex_per_row, "0")[:hex_per_row]
            rows.append(current_row)
            prev_row = current_row
            current_row = ""
            i += 1
            continue

        if ch == "!":
            current_row = current_row.ljust(hex_per_row, "F")[:hex_per_row]
            rows.append(current_row)
            prev_row = current_row
            current_row = ""
            i += 1
            continue

        # ── Repeat-count characters ──
        repeat = 0

        # Lowercase g-y = multiples of 20
        if "g" <= ch <= "y":
            repeat = (ord(ch) - ord("g") + 1) * 20
            i += 1
            # Optional uppercase G-Y additive
            if i < length and "G" <= data[i] <= "Y":
                repeat += ord(data[i]) - ord("G") + 1
                i += 1
        # Uppercase G-Y = 1-19
        elif "G" <= ch <= "Y":
            repeat = ord(ch) - ord("G") + 1
            i += 1

        if repeat > 0:
            # Next character is the hex digit to repeat
            if i < length and data[i] in _HEX_CHARS:
                current_row += data[i].upper() * repeat
                i += 1
            # Check if row is now complete
            if len(current_row) >= hex_per_row:
                rows.append(current_row[:hex_per_row])
                prev_row = current_row[:hex_per_row]
                current_row = current_row[hex_per_row:]
            continue

        # ── Regular hex character ──
        if ch in _HEX_CHARS:
            current_row += ch.upper()
            i += 1
            # Check if row is now complete
            if len(current_row) >= hex_per_row:
                rows.append(current_row[:hex_per_row])
                prev_row = current_row[:hex_per_row]
                current_row = current_row[hex_per_row:]
            continue

        # Skip whitespace and unknown characters
        i += 1

    # Flush any remaining partial row
    if current_row:
        current_row = current_row.ljust(hex_per_row, "0")[:hex_per_row]
        rows.append(current_row)

    return rows


def _hex_rows_to_image(rows: List[str], bytes_per_row: int) -> Optional["Image.Image"]:
    """Convert decompressed hex rows into a PIL Image (mode '1', black & white)."""
    if Image is None:
        return None
    if not rows or bytes_per_row == 0:
        return None

    width = bytes_per_row * 8
    height = len(rows)

    # Build raw bitmap bytes — 1 bit per pixel, MSB first
    row_bytes = []
    for row_hex in rows:
        try:
            row_bytes.append(bytes.fromhex(row_hex))
        except ValueError:
            row_bytes.append(b"\x00" * bytes_per_row)

    bitmap = b"".join(row_bytes)

    try:
        # ZPL: set bit = black dot; PIL frombytes('1'): set bit = white.
        # Invert by XOR-ing raw bytes before decoding — avoids ImageOps.invert
        # which doesn't support mode '1' and silently returns None via exception.
        inverted = bytes(b ^ 0xFF for b in bitmap)
        img = Image.frombytes("1", (width, height), inverted)
        return img
    except Exception:
        return None


def _calc_pixel_density(img: "Image.Image") -> float:
    """Calculate fraction of black pixels in a PIL '1' mode image."""
    if img is None:
        return 0.0
    try:
        pixels = list(img.getdata())
        total = len(pixels)
        if total == 0:
            return 0.0
        # In mode '1': 0 = black, 255 = white
        black = sum(1 for p in pixels if p == 0)
        return round(black / total, 4)
    except Exception:
        return 0.0


def _decode_all_gf_graphics(script: str) -> List[Dict[str, Any]]:
    """
    Find and decode all ^GF graphics in a ZPL script.
    Returns list of graphic dicts with metadata + decoded PIL Image.
    Handles labels with zero graphics gracefully (returns []).
    """
    graphics: List[Dict[str, Any]] = []
    seen_positions: set = set()

    # Pattern: ^FO{x},{y} ... ^GFA,{total},{total},{bpr},
    # The ^FO may be separated from ^GFA by other commands (^A, ^CF, etc.)
    fo_gfa_pattern = re.compile(
        r"\^FO(\d+(?:\.\d+)?),(\d+(?:\.\d+)?)"  # ^FO x,y
        r"((?:\^(?!GF)[^\^]*)*)"                  # optional commands between
        r"\^GFA,(\d+),(\d+),(\d+),"               # ^GFA,total,total,bpr,
    )

    for match in fo_gfa_pattern.finditer(script):
        x = float(match.group(1))
        y = float(match.group(2))
        total_bytes = int(match.group(4))
        bytes_per_row = int(match.group(6))

        if bytes_per_row == 0:
            continue

        pos_key = (x, y, total_bytes)
        if pos_key in seen_positions:
            continue
        seen_positions.add(pos_key)

        data_start = match.end()
        raw_data = _extract_gf_data_block(script, data_start)
        rows = _decompress_zpl_gf(raw_data, bytes_per_row)

        width = bytes_per_row * 8
        height = len(rows) if rows else (total_bytes // bytes_per_row if bytes_per_row else 0)

        img = _hex_rows_to_image(rows, bytes_per_row)
        density = _calc_pixel_density(img)

        graphics.append({
            "type": "GFA",
            "x": x,
            "y": y,
            "total_bytes": total_bytes,
            "bytes_per_row": bytes_per_row,
            "width": width,
            "height": height,
            "aspect_ratio": round(width / height, 3) if height > 0 else 0,
            "pixel_density": density,
            "image": img,
        })

    # Also catch ^GFA without preceding ^FO (position unknown)
    bare_pattern = re.compile(r"\^GFA,(\d+),(\d+),(\d+),")
    for match in bare_pattern.finditer(script):
        total_bytes = int(match.group(1))
        bytes_per_row = int(match.group(3))

        if bytes_per_row == 0:
            continue

        pos_key = (0, 0, total_bytes)
        if pos_key in seen_positions:
            continue
        # Check if this total_bytes was already captured by the positioned regex
        if any(g["total_bytes"] == total_bytes for g in graphics):
            continue
        seen_positions.add(pos_key)

        data_start = match.end()
        raw_data = _extract_gf_data_block(script, data_start)
        rows = _decompress_zpl_gf(raw_data, bytes_per_row)

        width = bytes_per_row * 8
        height = len(rows) if rows else (total_bytes // bytes_per_row if bytes_per_row else 0)

        img = _hex_rows_to_image(rows, bytes_per_row)
        density = _calc_pixel_density(img)

        graphics.append({
            "type": "GFA",
            "x": 0,
            "y": 0,
            "total_bytes": total_bytes,
            "bytes_per_row": bytes_per_row,
            "width": width,
            "height": height,
            "aspect_ratio": round(width / height, 3) if height > 0 else 0,
            "pixel_density": density,
            "image": img,
        })

    return graphics


def _extract_fx_comment_map(script: str) -> Dict[tuple, str]:
    """
    Extract ^FX comment labels and map them to the nearest following ^FO/^FT position.

    In ZPL, ^FX is a comment command — its text runs until the next ^ character.
    When users annotate their label scripts with comments like:
        ^FX Pickup Date^FO400,50^A0N,22,26^FDDATE: 04/15/2026^FS
    we use the comment to:
      - Identify exactly WHERE a field lives on the label
      - Resolve carrier-specific field names (e.g. "Pickup Date" = shipment_date)

    Returns: dict mapping (x, y) → comment_text for each annotated field origin.
    """
    comment_map: Dict[tuple, str] = {}

    # ^FX: everything until the next ^ is the comment text
    fx_pattern = re.compile(r"\^FX([^\^]*)", re.IGNORECASE)
    fo_pattern = re.compile(r"\^(?:FO|FT)(\d+(?:\.\d+)?),(\d+(?:\.\d+)?)")

    # Collect all FO/FT positions with their byte offset in the script
    fo_entries = [
        (m.start(), float(m.group(1)), float(m.group(2)))
        for m in fo_pattern.finditer(script)
    ]

    for fx_match in fx_pattern.finditer(script):
        comment_text = fx_match.group(1).strip()
        # Drop ^FS suffix if user wrote ^FX text^FS
        comment_text = re.sub(r"\^FS\s*$", "", comment_text).strip()
        if not comment_text or len(comment_text) < 2:
            continue

        fx_end = fx_match.end()  # position of the ^ that ends this comment

        # Find the nearest ^FO/^FT within 500 chars after this comment
        for fo_offset, x, y in fo_entries:
            if fo_offset >= fx_end and fo_offset - fx_end <= 500:
                comment_map[(x, y)] = comment_text
                break

    return comment_map


def parse_zpl_to_raw(script: str) -> Dict[str, Any]:
    """
    Extract ALL data from a ZPL script — no field name assumptions.
    
    Returns a dict with:
      - text_blocks: list of {x, y, text, font_size} for every ^FD
      - barcodes: list of {type, data, x, y, height} for every barcode command
      - graphics: list of {type, x, y, size} for every graphic element
      - zpl_commands: set of all ZPL command types found (^BC, ^BD, ^GFA, etc.)
      - raw_texts: list of all ^FD text values (flat, for simple searching)
    """
    raw = {
        "text_blocks": [],
        "barcodes": [],
        "graphics": [],
        "zpl_commands": set(),
        "raw_texts": [],
        "combined_line_texts": [],
    }

    # ── Extract default font (^CF) ──
    default_font = ""
    default_font_height = 0
    default_font_width = 0
    cf_match = re.search(r"\^CF([A-Z0-9]),(\d+)(?:,(\d+))?", script)
    if cf_match:
        default_font = f"^CF{cf_match.group(1)},{cf_match.group(2)}"
        default_font_height = int(cf_match.group(2))
        default_font_width = int(cf_match.group(3)) if cf_match.group(3) else default_font_height

    # ── Extract all positioned text blocks ──
    # Match ^FO or ^FT (field typeset) x,y followed eventually by ^FD content ^FS
    for fo_match in re.finditer(r"\^(FO|FT)(\d+(?:\.\d+)?),(\d+(?:\.\d+)?)", script):
        pos_type = fo_match.group(1)  # "FO" or "FT"
        x = float(fo_match.group(2))
        y = float(fo_match.group(3))
        rest = script[fo_match.end():]

        # Extract font command: ^A variants (^A0N,h,w  ^AAN,h,w  ^ABN,h,w etc.)
        font_cmd = ""
        font_size = 0
        font_match = re.match(r"[^\^]*\^(A[A-Z0-9]N?,(\d+)(?:,(\d+))?)", rest)
        if font_match:
            font_cmd = "^" + font_match.group(1)
            font_size = int(font_match.group(2))
        elif default_font:
            font_cmd = default_font
            font_size = default_font_height

        # Find ^FD before next ^FO/^FT
        fd_match = re.search(r"\^FD(.*?)\^FS", rest, re.DOTALL)
        next_fo = re.search(r"\^F[OT]\d", rest)

        if fd_match:
            if next_fo is None or fd_match.start() < next_fo.start():
                text = fd_match.group(1).strip()
                if text:
                    raw["text_blocks"].append({
                        "x": x, "y": y,
                        "text": text,
                        "font_size": font_size,
                        "font_cmd": font_cmd,
                        "pos_type": pos_type,
                    })
                    raw["raw_texts"].append(text)

    # Also catch ^FD blocks that aren't preceded by ^FO (rare but possible)
    for fd_match in re.finditer(r"\^FD(.*?)\^FS", script, re.DOTALL):
        text = fd_match.group(1).strip()
        if text and text not in raw["raw_texts"]:
            raw["raw_texts"].append(text)

    # ── Extract all barcode commands and their data ──
    barcode_commands = {
        "BC": "CODE128",
        "BD": "MAXICODE",
        "B7": "PDF417",
        "BX": "DATAMATRIX",
        "BQ": "QRCODE",
        "BA": "CODE39",
        "B2": "INTERLEAVED2OF5",
        "B3": "CODE39",
        "BE": "EAN13",
        "B8": "EAN8",
    }

    for cmd, barcode_type in barcode_commands.items():
        # Pattern: ^FO x,y ... ^Bx params ... ^FD data ^FS
        pattern = rf"\^FO(\d+(?:\.\d+)?),(\d+(?:\.\d+)?)[^\^]*(?:\^[A-Z][^\^]*)*\^{cmd}([^\^]*?)(?:\^[A-Z][^\^]*)*\^FD(.*?)\^FS"
        for match in re.finditer(pattern, script, re.DOTALL):
            x = float(match.group(1))
            y = float(match.group(2))
            params = match.group(3).strip()
            data = match.group(4).strip().lstrip(">;")

            # Extract height from params if available
            height = 0
            height_match = re.search(r"N?,?(\d+)", params)
            if height_match:
                height = int(height_match.group(1))

            raw["barcodes"].append({
                "type": barcode_type,
                "data": data,
                "x": x, "y": y,
                "height": height,
            })

        # Also catch barcode commands without ^FO positioning
        pattern2 = rf"\^{cmd}([^\^]*?)\^FD(.*?)\^FS"
        for match in re.finditer(pattern2, script, re.DOTALL):
            data = match.group(2).strip().lstrip(">;")
            already_found = any(b["data"] == data for b in raw["barcodes"])
            if not already_found and data:
                raw["barcodes"].append({
                    "type": barcode_type,
                    "data": data,
                    "x": 0, "y": 0,
                    "height": 0,
                })

    # MaxiCode special: ^BD can appear as ^BD3^FH^FD... (with ^FH hex indicator)
    for match in re.finditer(r"\^BD(\d?)(?:\^FH)?\^FD(.*?)\^FS", script, re.DOTALL):
        data = match.group(2).strip()
        already_found = any(b["data"] == data and b["type"] == "MAXICODE" for b in raw["barcodes"])
        if not already_found and data:
            raw["barcodes"].append({
                "type": "MAXICODE",
                "data": data,
                "x": 0, "y": 0,
                "height": 0,
            })

    # ── Decode graphic elements (^GFA → PIL Image) ──
    raw["graphics"] = _decode_all_gf_graphics(script)

    # ── Catalog all ZPL commands present ──
    for match in re.finditer(r"\^([A-Z][A-Z0-9])", script):
        raw["zpl_commands"].add("^" + match.group(1))

    # Convert set to list for JSON serialization
    raw["zpl_commands"] = sorted(list(raw["zpl_commands"]))

    # Enrich text_blocks with ^FX comment labels if the script contains any
    comment_map = _extract_fx_comment_map(script)
    if comment_map:
        for block in raw["text_blocks"]:
            label = comment_map.get((block["x"], block["y"]))
            if label:
                block["comment_label"] = label

    # Sort text blocks by position (top to bottom, left to right)
    raw["text_blocks"].sort(key=lambda b: (b["y"], b["x"]))

    # Build combined-line texts: join all text blocks that share the same Y
    # coordinate (within a 5-dot tolerance) into a single space-separated string.
    # ZPL labels often split one visual line across multiple ^FD fields — without
    # this, patterns like "\d+\.\d+[A-Z]\s\d{2}/\d{4}" fail when "18.5A" and
    # "01/2020" are in separate ^FD blocks on the same row.
    if raw["text_blocks"]:
        rows: Dict[int, list] = {}
        for block in raw["text_blocks"]:
            row_key = round(block["y"] / 5) * 5  # bucket to nearest 5 dots
            rows.setdefault(row_key, []).append(block["text"])
        for texts_in_row in rows.values():
            if len(texts_in_row) > 1:
                combined = " ".join(texts_in_row)
                if combined not in raw["raw_texts"]:
                    raw["combined_line_texts"].append(combined)

    return raw


def parse_zpl_script(script: str) -> Dict[str, Any]:
    """
    Backward-compatible wrapper.
    
    Returns the raw extraction AND a basic parsed dict with common
    field names for backward compatibility with existing code.
    
    The raw data is stored under "_raw" key for the new validator to use.
    """
    raw = parse_zpl_to_raw(script)

    # Build backward-compatible parsed dict
    parsed = {}
    parsed["_raw"] = raw

    # Basic extractions that don't assume carrier-specific naming
    _extract_basics(parsed, raw, script)

    return parsed


def _extract_basics(parsed: dict, raw: dict, script: str):
    """
    Extract basic fields for backward compatibility.
    These are generic ZPL patterns that work across all carriers.
    """
    texts = raw["raw_texts"]
    barcodes = raw["barcodes"]

    # Tracking number — from barcode data or TRACKING #: text
    for bc in barcodes:
        if bc["type"] == "CODE128":
            data = bc["data"]
            # UPS: 1Z + 16 alphanumeric
            if re.match(r"^1Z[A-Z0-9]{16}$", data):
                parsed["tracking_number"] = data
                parsed["barcode"] = data
                break
            # DHL: JD + digits
            if re.match(r"^JD\d{18,}$", data):
                parsed["tracking_number"] = data
                parsed["barcode"] = data
                break
            # FedEx/Generic: 12-22 digit barcode
            if re.match(r"^\d{12,22}$", data):
                parsed.setdefault("tracking_number", data)
                parsed.setdefault("barcode", data)

    # From TRACKING #: text
    for t in texts:
        if "TRACKING" in t.upper() and "#" in t:
            match = re.search(r"TRACKING\s*#\s*:\s*([\dA-Z\s]+)", t, re.IGNORECASE)
            if match:
                parsed.setdefault("tracking_number", match.group(1).strip().replace(" ", ""))

    # Weight — standalone number + KG/LBS
    for t in texts:
        if re.match(r"^\d+(\.\d+)?\s+(KG|LBS?)\s*$", t.strip(), re.IGNORECASE):
            if not any(kw in t.upper() for kw in ["SHP WT", "SHP DWT"]):
                parsed["weight"] = t.strip()
                break

    # Piece count — N OF X
    for t in texts:
        match = re.search(r"\b(\d+)\s+OF\s+(\d+|_+)\b", t, re.IGNORECASE)
        if match:
            parsed["piece_count"] = match.group(0)
            break

    # Service type — from known service prefixes
    for t in texts:
        upper = t.upper().strip()
        if any(upper.startswith(p) for p in ["UPS ", "DHL ", "FEDEX ", "TNT ", "DPD "]):
            if len(upper) <= 40:
                parsed["service_type"] = upper
                break

    # Sender/receiver addresses — from spatial position
    ship_to_y = None
    for block in raw["text_blocks"]:
        if block["text"].upper().strip() in ("SHIP", "SHIP TO:", "SHIP TO"):
            ship_to_y = block["y"]
            break

    if ship_to_y:
        sender_lines = []
        receiver_lines = []
        for block in raw["text_blocks"]:
            if block["text"].upper().strip() in ("SHIP", "TO:", "SHIP TO:", "TO"):
                continue
            if block["y"] < ship_to_y and block["x"] < 400:
                # Skip package info in top-right
                if block["x"] > 400:
                    continue
                if any(kw in block["text"].upper() for kw in ["SHP#", "SHP WT", "SHP DWT", "DATE:"]):
                    continue
                if re.match(r"^\d+(\.\d+)?\s+(KG|LBS)", block["text"].strip(), re.IGNORECASE):
                    continue
                if re.match(r"^\d+\s+OF\s+", block["text"].strip(), re.IGNORECASE):
                    continue
                sender_lines.append(block["text"].strip())
            elif block["x"] >= 200 and block["y"] >= ship_to_y - 30 and block["y"] < ship_to_y + 160:
                receiver_lines.append(block["text"].strip())

        if sender_lines:
            parsed["sender_address"] = " | ".join(sender_lines)
        if receiver_lines:
            parsed["receiver_address"] = " | ".join(receiver_lines)

    # Billing
    for t in texts:
        if t.upper().startswith("BILLING"):
            match = re.search(r"BILLING\s*:\s*(.+)", t, re.IGNORECASE)
            if match:
                parsed["billing"] = match.group(1).strip()
                break

    # Country
    country_names = {
        "GERMANY", "FRANCE", "SPAIN", "PORTUGAL", "ITALY", "NETHERLANDS",
        "BELGIUM", "AUSTRIA", "SWITZERLAND", "SWEDEN", "DENMARK", "NORWAY",
        "FINLAND", "POLAND", "IRELAND", "UNITED KINGDOM", "UK", "USA",
        "UNITED STATES", "CANADA", "BRAZIL", "MEXICO", "JAPAN", "CHINA",
        "INDIA", "AUSTRALIA", "SINGAPORE", "HUNGARY", "ROMANIA", "GREECE",
        "CZECH REPUBLIC", "TURKEY", "CROATIA", "BULGARIA", "SERBIA",
        "LUXEMBOURG", "SLOVAKIA", "SLOVENIA", "ESTONIA", "LATVIA", "LITHUANIA",
    }
    for t in texts:
        if t.upper().strip() in country_names:
            parsed["destination_country"] = t.upper().strip()
            break