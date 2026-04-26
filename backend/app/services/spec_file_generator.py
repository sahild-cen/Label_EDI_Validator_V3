"""
V3 Phase 2: Spec File Generator

Reads extracted content from docs/carriers/{carrier_code}/Extracted/
Calls Claude to identify all label fields and generate one .md spec file per field.

Pipeline:
    1. Load full_text.txt + sections.json + tables.json from Extracted/
    2. Chunk content if PDF is large (> 35k chars)
    3. For each chunk, ask Claude to output fields using delimiter format (not JSON)
    4. Parse delimiters to extract individual field specs
    5. Merge results, deduplicate by field name
    6. Write each field spec to docs/carriers/{carrier_code}/Spec/{field}.md
    7. Already-reviewed files are never overwritten

NOTE: We use delimiter-based output (not JSON) because spec content contains
markdown, backticks, newlines and special chars that break JSON parsing.
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple
from datetime import datetime, timezone
import json

from app.services.pdf_extractor import DOCS_BASE
from app.services.claude_service import client, deployment_name


# Max chars to send in a single Claude prompt
MAX_CHUNK_CHARS = 35_000

LABEL_FIELD_EXTRACTION_PROMPT = """\
You are an expert in logistics carrier shipping label specifications and ZPL (Zebra Programming Language).

Below is extracted text from the specification PDF for carrier: {carrier_code}

Your task:
1. Identify ALL distinct fields/elements that must or can appear on this carrier's shipping labels
2. For each field, generate a complete structured specification file using the rules below

═══ GROUPING RULES (READ CAREFULLY) ═══

COMPOSITE FIELDS — create ONE parent file with a ## Subfields section:
  - Address blocks: ship_from_address, ship_to_address, return_address
    Subfields: name, address_line_1, address_line_2, city, state, postal_code, country
  - Weight/measurement: weight (subfields: value, unit)
  - Dimensions: dimensions (subfields: length, width, height, unit)

SIMPLE FIELDS — create a flat file WITHOUT subfields:
  - Barcodes: tracking_number, maxicode, postal_barcode, pdf417, etc.
  - Single-value text fields: service_type, shipment_date, piece_count, billing_type, etc.
  - Reference fields: po_number, reference_number, etc.

═══ WHAT TO LOOK FOR ═══
- Named data elements: tracking number, service type, routing code, weight, piece count, etc.
- Barcode elements: MaxiCode, PDF417, postal barcode, tracking barcode, 1D/2D barcodes
- Address blocks: ship-from, ship-to/consignee, return address
- Required indicators: service icons, billing indicators, delivery notifications
- Reference fields: PO number, reference number, department code, invoice number
- Date/time fields: ship date, delivery date
- Special fields: description of goods, country of origin, customs value

WHAT TO SKIP:
- Physical printing specs: barcode x-dimensions, quiet zones, DPI
- Document metadata: copyright, spec version numbers, page headers/footers
- Color and visual design specs

═══ OUTPUT FORMAT ═══
Do NOT wrap in JSON. Use EXACTLY these delimiters.

── FLAT FIELD (no subfields): ──

<<<FIELD_START: tracking_number>>>
# Field: tracking_number

## Display Name
Tracking Number

## Field Description
1-2 sentences about what this field represents.

## Format & Validation Rules
- **Data Type:** string | numeric | date | alphanumeric | barcode
- **Length:** exact length, min-max, or "variable"
- **Pattern/Regex:** regex if defined in spec, else "Not specified in spec"
- **Allowed Values:** enumerated list if applicable, else "Not restricted"
- **Required:** yes | no | conditional — explain condition

## Examples from Spec
Copy exact examples from the PDF. If none: "No examples in spec."

## ZPL Rendering
- **Typical Position:** approximate X,Y zone (e.g. "bottom barcode area")
- **Font / Size:** ZPL font command if specified, else "Not specified"
- **Field Prefix:** literal text prefix before the value (e.g. "DATE:"), or "None — barcode"
- **ZPL Command:** e.g. ^BC, ^BD, ^B7, ^GFA, or "^FD (text field)"

## Edge Cases & Notes
Anything unusual, conditional logic, carrier-specific quirks.

## Claude Confidence
HIGH | MEDIUM | LOW — brief explanation

## Review Status
- [ ] Reviewed by human
<<<FIELD_END>>>

── COMPOSITE FIELD (with subfields): ──

<<<FIELD_START: ship_from_address>>>
# Field: ship_from_address

## Display Name
Ship From Address

## Field Description
Complete ship-from address block printed in the upper-left area of the label.

## Required
yes

## ZPL Rendering
- **Typical Position:** top-left block
- **Font / Size:** Not specified

## Subfields

### name
- **Pattern/Regex:** .{{1,35}}
- **Required:** yes
- **Detect By:** spatial:ship_from
- **Description:** Shipper company or person name

### address_line_1
- **Pattern/Regex:** .{{1,35}}
- **Required:** yes
- **Description:** First line of street address

### city
- **Pattern/Regex:** [A-Za-z ]{{1,30}}
- **Required:** yes
- **Description:** City name

### state
- **Pattern/Regex:** [A-Z]{{2}}
- **Required:** conditional — required for US/CA addresses
- **Description:** State or province code

### postal_code
- **Pattern/Regex:** \\d{{5}}(-\\d{{4}})?
- **Required:** yes
- **Description:** ZIP or postal code

### country
- **Pattern/Regex:** [A-Z]{{2}}
- **Required:** conditional — required for international shipments
- **Description:** ISO 2-letter country code

## Edge Cases & Notes
Address lines 2+ are optional.

## Claude Confidence
HIGH — address block with clear subfields

## Review Status
- [ ] Reviewed by human
<<<FIELD_END>>>

Repeat <<<FIELD_START: ...>>> ... <<<FIELD_END>>> for EACH field found (both flat and composite).

EXTRACTED SPEC TEXT:
{extracted_text}
"""

# Keep old name as alias so any callers using FIELD_EXTRACTION_PROMPT still work
FIELD_EXTRACTION_PROMPT = LABEL_FIELD_EXTRACTION_PROMPT


EDI_FIELD_EXTRACTION_PROMPT = """\
You are an expert in EDI standards (ANSI X12, UN/EDIFACT) and logistics carrier EDI specifications.

Below is extracted text from the EDI specification PDF for carrier: {carrier_code}

Your task:
1. Identify ALL EDI segments mentioned in the spec
2. For each segment, generate ONE spec file listing its sub-elements (subfields)

═══ RULES ═══
- One <<<FIELD_START>>> block per SEGMENT (e.g. BGM, DTM, NAD, RFF, etc.)
- The field name = the segment ID in snake_case lowercase (e.g. bgm, dtm, nad)
- List every data element position as a subfield with: element_position, pattern, required, description
- element_position is 1-indexed from the first element after the segment tag
  Example: BGM+610+73400858+9  →  element 1 = "610", element 2 = "73400858", element 3 = "9"
- For EDIFACT composite elements (e.g. DTM+137:20231115:102), the sub-components after ':' are
  separate sub-element positions — treat the whole DTM+137:date:format as one DTM segment
- required: yes if the spec says the element is mandatory; no if optional

WHAT TO SKIP:
- Metadata: version numbers, spec headers, copyright
- Pure envelope segments with no carrier-specific rules (UNA is usually skippable)

═══ OUTPUT FORMAT ═══
Do NOT wrap in JSON. Use EXACTLY these delimiters.

<<<FIELD_START: bgm>>>
# Field: BGM

## Display Name
Begin Message

## Segment ID
BGM

## Required
yes

## Description
Identifies the beginning of the message and its type.

## Subfields

### document_name_code
- **Element Position:** 1
- **Pattern/Regex:** 610
- **Required:** yes
- **Description:** Document name code — 610 = Despatch advice / shipment notice

### document_identifier
- **Element Position:** 2
- **Pattern/Regex:** \\d{{1,35}}
- **Required:** yes
- **Description:** Unique document or shipment identifier

### message_function_code
- **Element Position:** 3
- **Pattern/Regex:** 9
- **Required:** yes
- **Description:** Message function — 9 = original

## Edge Cases & Notes
BGM appears once per message. document_name_code 610 is mandatory for this carrier.

## Claude Confidence
HIGH — spec clearly specifies all three elements

## Review Status
- [ ] Reviewed by human
<<<FIELD_END>>>

Repeat <<<FIELD_START: ...>>> ... <<<FIELD_END>>> for EACH segment found.

EXTRACTED SPEC TEXT:
{extracted_text}
"""


def _load_extracted_content(carrier_code: str, spec_type: str = "label") -> Dict:
    """Load all extracted content from the Extracted/ directory."""
    extracted_dir = DOCS_BASE / carrier_code / spec_type / "Extracted"

    if not extracted_dir.exists():
        raise FileNotFoundError(
            f"No extracted content found for '{carrier_code}'. "
            f"Run Phase 1 extraction first (POST /api/carrier-setup/extract)."
        )

    result = {"full_text": "", "sections": [], "tables": []}

    full_text_path = extracted_dir / "full_text.txt"
    if full_text_path.exists():
        result["full_text"] = full_text_path.read_text(encoding="utf-8")

    sections_path = extracted_dir / "sections.json"
    if sections_path.exists():
        result["sections"] = json.loads(sections_path.read_text(encoding="utf-8"))

    tables_path = extracted_dir / "tables.json"
    if tables_path.exists():
        result["tables"] = json.loads(tables_path.read_text(encoding="utf-8"))

    return result


def _build_context_chunks(content: Dict) -> List[str]:
    """
    Build text chunks from extracted content, staying under MAX_CHUNK_CHARS.
    Uses sections as natural boundaries; appends table data to the last chunk.
    """
    sections = content.get("sections", [])
    tables = content.get("tables", [])

    # Build table summary text
    table_text = ""
    if tables:
        parts = []
        for t in tables:
            header = t.get("header", [])
            rows = t.get("rows", [])
            page = t.get("page", "?")
            if header or rows:
                lines = [f"[Table — page {page}]"]
                if header:
                    lines.append(" | ".join(str(h) for h in header if h))
                for row in rows[:20]:
                    lines.append(" | ".join(str(c) for c in row if c))
                parts.append("\n".join(lines))
        if parts:
            table_text = "\n\n[STRUCTURED TABLES FROM SPEC]\n" + "\n\n".join(parts)

    if sections:
        combined_sections = []
        for s in sections:
            heading = s.get("title", "").strip()
            body = s.get("content", "").strip()
            if heading:
                combined_sections.append(f"=== {heading} ===\n{body}")
            elif body:
                combined_sections.append(body)
        combined = "\n\n".join(combined_sections) + table_text
    else:
        combined = content.get("full_text", "") + table_text

    if len(combined) <= MAX_CHUNK_CHARS:
        return [combined] if combined.strip() else []

    # Split at section boundaries
    chunks = []
    current = ""

    for s in sections:
        heading = s.get("title", "").strip()
        body = s.get("content", "").strip()
        section_text = (f"=== {heading} ===\n{body}\n\n" if heading else f"{body}\n\n")

        if len(current) + len(section_text) > MAX_CHUNK_CHARS:
            if current.strip():
                chunks.append(current.strip())
            current = section_text
        else:
            current += section_text

    if current.strip():
        if len(current) + len(table_text) <= MAX_CHUNK_CHARS:
            current += table_text
        else:
            chunks.append(current.strip())
            current = table_text

    if current.strip():
        chunks.append(current.strip())

    # Fallback: raw text chunks
    if not chunks:
        raw = content.get("full_text", "")
        for i in range(0, len(raw), MAX_CHUNK_CHARS):
            chunk = raw[i: i + MAX_CHUNK_CHARS].strip()
            if chunk:
                chunks.append(chunk)

    return chunks


def _parse_delimiter_response(response_text: str) -> List[Dict]:
    """
    Parse Claude's delimiter-based response into field dicts.

    Looks for:
        <<<FIELD_START: field_name>>>
        ...markdown content...
        <<<FIELD_END>>>
    """
    fields = []

    # Match all FIELD_START...FIELD_END blocks
    pattern = r'<<<FIELD_START:\s*([^\n>]+)>>>(.*?)<<<FIELD_END>>>'
    matches = re.findall(pattern, response_text, re.DOTALL)

    for raw_name, spec_content in matches:
        field_name = raw_name.strip().lower()
        field_name = re.sub(r"[^\w]", "_", field_name).strip("_")
        field_name = re.sub(r"_+", "_", field_name)

        spec_content = spec_content.strip()

        if field_name and spec_content:
            fields.append({
                "field_name": field_name,
                "spec_content": spec_content,
            })

    return fields


def _call_claude_for_specs(carrier_code: str, text_chunk: str, chunk_num: int,
                           prompt_template: str = None) -> List[Dict]:
    """
    Call Claude with a chunk of extracted spec text.
    Returns list of {field_name, spec_content} dicts parsed from delimiters.
    """
    if not client:
        print("[Phase 2] Claude client not initialized — skipping")
        return []

    template = prompt_template or LABEL_FIELD_EXTRACTION_PROMPT
    prompt = template.format(
        carrier_code=carrier_code,
        extracted_text=text_chunk,
    )

    print(f"  [Phase 2] Calling Claude for chunk {chunk_num} ({len(text_chunk):,} chars)...")

    try:
        response = client.messages.create(
            model=deployment_name,
            max_tokens=8000,
            messages=[{"role": "user", "content": prompt}],
        )

        if not response.content:
            print(f"  [Phase 2] Empty response for chunk {chunk_num}")
            return []

        text = response.content[0].text
        fields = _parse_delimiter_response(text)

        if not fields:
            # Log a snippet to help debug
            preview = text[:300].replace("\n", " ")
            print(f"  [Phase 2] No delimiters found in chunk {chunk_num} response. Preview: {preview}...")
        else:
            print(f"    -> Found {len(fields)} field(s)")

        return fields

    except Exception as e:
        print(f"  [Phase 2] Claude error (chunk {chunk_num}): {e}")
        return []


def _merge_field_specs(all_results: List[List[Dict]]) -> List[Dict]:
    """
    Merge field specs from multiple Claude calls.
    Keeps the entry with more content when duplicates exist.
    """
    seen: Dict[str, Dict] = {}

    for result_set in all_results:
        for field in result_set:
            name = field.get("field_name", "").strip()
            if not name:
                continue
            if name not in seen:
                seen[name] = field
            elif len(field.get("spec_content", "")) > len(seen[name].get("spec_content", "")):
                seen[name] = field

    return list(seen.values())


def _write_spec_file(spec_dir: Path, field_name: str, spec_content: str) -> Tuple[Path, bool]:
    """
    Write spec content to a .md file.
    Returns (path, was_written). Skips already-reviewed files.
    """
    safe_name = re.sub(r"[^\w]", "_", field_name.lower()).strip("_")
    safe_name = re.sub(r"_+", "_", safe_name)
    file_path = spec_dir / f"{safe_name}.md"

    # Never overwrite a reviewed file
    if file_path.exists():
        existing = file_path.read_text(encoding="utf-8")
        if "- [x] Reviewed by human" in existing:
            return file_path, False

    # Ensure the header is correct
    if not spec_content.startswith("# Field:"):
        spec_content = f"# Field: {safe_name}\n\n" + spec_content

    file_path.write_text(spec_content, encoding="utf-8")
    return file_path, True


async def generate_spec_files(carrier_code: str, spec_type: str = "label") -> Dict:
    """
    Phase 2 main entry point.

    Reads extracted content and uses Claude to generate per-field .md spec files.
    Output: docs/carriers/{carrier_code}/{spec_type}/Spec/
    """
    code = carrier_code.lower().replace(" ", "_")
    stype = spec_type.lower()
    spec_dir = DOCS_BASE / code / stype / "Spec"
    spec_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"[Phase 2] Generating {stype} spec files for '{code}'")
    print(f"  Spec dir: {spec_dir}")
    print(f"{'='*60}")

    # Delete all existing .md spec files before regenerating so every
    # re-upload starts completely fresh regardless of review status.
    if spec_dir.exists():
        deleted = 0
        for old_file in spec_dir.glob("*.md"):
            if not old_file.name.startswith("_"):
                old_file.unlink()
                deleted += 1
        if deleted:
            print(f"  Deleted {deleted} existing spec file(s) — regenerating from scratch")

    # Step 1: Load extracted content
    content = _load_extracted_content(code, spec_type=stype)
    text_len = len(content.get("full_text", ""))
    sections_n = len(content.get("sections", []))
    tables_n = len(content.get("tables", []))
    print(f"  Loaded: {text_len:,} chars | {sections_n} sections | {tables_n} tables")

    if text_len < 100 and sections_n == 0:
        return {
            "success": False,
            "carrier_code": code,
            "message": "Extracted content is too short. Re-run Phase 1 extraction.",
            "files_created": 0,
        }

    # Step 2: Build chunks
    chunks = _build_context_chunks(content)
    print(f"  Split into {len(chunks)} chunk(s)")

    if not chunks:
        return {
            "success": False,
            "carrier_code": code,
            "message": "Could not build context chunks from extracted content.",
            "files_created": 0,
        }

    # Step 3: Call Claude for each chunk (use EDI prompt for edi spec_type)
    prompt_template = EDI_FIELD_EXTRACTION_PROMPT if stype == "edi" else LABEL_FIELD_EXTRACTION_PROMPT
    all_results = []
    for i, chunk in enumerate(chunks, start=1):
        fields = _call_claude_for_specs(code, chunk, i, prompt_template=prompt_template)
        if fields:
            all_results.append(fields)

    if not all_results:
        return {
            "success": False,
            "carrier_code": code,
            "message": "Claude did not return any field specs. Check extraction quality.",
            "files_created": 0,
        }

    # Step 4: Merge and deduplicate
    merged = _merge_field_specs(all_results)
    print(f"  Merged: {len(merged)} unique field(s)")

    # Step 5: Write spec files
    files_created = 0
    files_skipped = 0
    files_written = []

    for field in merged:
        field_name = field.get("field_name", "").strip()
        spec_content = field.get("spec_content", "").strip()

        if not field_name or not spec_content:
            continue

        path, written = _write_spec_file(spec_dir, field_name, spec_content)
        if written:
            files_created += 1
            files_written.append(path.name)
            print(f"    + {path.name}")
        else:
            files_skipped += 1
            print(f"    ~ {path.name} (skipped — already reviewed)")

    # Step 6: Save generation metadata
    meta = {
        "carrier_code": code,
        "spec_type": stype,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "chunks_processed": len(chunks),
        "fields_found": len(merged),
        "files_created": files_created,
        "files_skipped": files_skipped,
        "spec_dir": str(spec_dir),
    }
    (spec_dir / "_generation_meta.json").write_text(
        json.dumps(meta, indent=2), encoding="utf-8"
    )

    print(f"\n[Phase 2] Done — {files_created} files created, {files_skipped} skipped")
    print(f"  Spec files at: {spec_dir}")

    return {
        "success": True,
        "carrier_code": code,
        "spec_type": stype,
        "fields_found": len(merged),
        "files_created": files_created,
        "files_skipped": files_skipped,
        "files": files_written,
        "spec_dir": str(spec_dir),
        "next_step": (
            f"Review .md files in: {spec_dir}  "
            "Mark reviewed: '[ ] Reviewed by human' → '[x] Reviewed by human'.  "
            f"Then call POST /api/carrier-setup/generate-rules/{{carrier_code}}?spec_type={stype}"
        ),
    }
