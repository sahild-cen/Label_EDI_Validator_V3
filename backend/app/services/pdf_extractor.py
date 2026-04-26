"""
V3 PDF Extraction Pipeline — Phase 1

Uses PyMuPDF (fitz) for text extraction and Pillow for image/table processing.
Outputs clean extracted text + image descriptions to:
    docs/carriers/{carrier_code}/Extracted/

This replaces the V2 single-pass text extraction with a richer pipeline
that preserves structure, images, and table data for downstream Claude analysis.
"""

import fitz  # PyMuPDF
import os
import re
import json
import hashlib
from io import BytesIO
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from datetime import datetime, timezone
from PIL import Image

# Base directory for carrier docs (relative to project root)
DOCS_BASE = Path(__file__).resolve().parents[3] / "docs" / "carriers"


class PDFExtractor:
    """
    Extracts text, images, and table-like structures from carrier spec PDFs.

    Pipeline:
        1. PyMuPDF extracts text per page with layout preservation
        2. PyMuPDF extracts embedded images
        3. Pillow processes images — describes dimensions, type, detects diagrams
        4. Table detection via line/rect analysis in PyMuPDF
        5. Everything saved to docs/carriers/{carrier_code}/Extracted/
    """

    def __init__(self, carrier_code: str, spec_type: str = "label"):
        self.carrier_code = carrier_code.lower().replace(" ", "_")
        self.spec_type = spec_type.lower()  # "label" or "edi"
        self.carrier_dir = DOCS_BASE / self.carrier_code
        # Each spec type lives in its own subfolder
        self.type_dir = self.carrier_dir / self.spec_type
        self.doc_dir = self.type_dir / "Documentation"
        self.extracted_dir = self.type_dir / "Extracted"
        self.spec_dir = self.type_dir / "Spec"
        self.rules_dir = self.type_dir / "Rules"

    def ensure_dirs(self):
        """Create the carrier directory structure."""
        for d in [self.doc_dir, self.extracted_dir, self.spec_dir, self.rules_dir]:
            d.mkdir(parents=True, exist_ok=True)

    async def extract(self, pdf_path: str) -> Dict:
        """
        Main entry point. Extracts all content from a carrier spec PDF.

        Args:
            pdf_path: Path to the uploaded PDF file.

        Returns:
            Dict with extraction results and output file paths.
        """
        self.ensure_dirs()

        # Copy original PDF to Documentation/ — always overwrite so re-uploads
        # use the latest file, not a cached copy from a previous run.
        import shutil
        pdf_name = os.path.basename(pdf_path)
        doc_copy = self.doc_dir / pdf_name
        shutil.copy2(pdf_path, doc_copy)

        doc = fitz.open(pdf_path)
        total_pages = len(doc)

        # Run extraction steps
        pages_text = self._extract_text_by_page(doc)
        sections = self._detect_sections(pages_text)
        tables = self._extract_tables(doc)
        images = self._extract_images(doc)
        image_descriptions = self._describe_images(images)
        metadata = self._extract_metadata(doc)

        doc.close()

        # Build the combined extraction output
        extraction_result = {
            "carrier_code": self.carrier_code,
            "source_pdf": pdf_name,
            "extracted_at": datetime.now(timezone.utc).isoformat(),
            "total_pages": total_pages,
            "metadata": metadata,
            "pages": pages_text,
            "sections": sections,
            "tables": tables,
            "images": image_descriptions,
        }

        # Save outputs
        output_paths = self._save_extraction(extraction_result, images)

        return {
            "success": True,
            "carrier_code": self.carrier_code,
            "total_pages": total_pages,
            "text_pages_extracted": len(pages_text),
            "sections_detected": len(sections),
            "tables_detected": len(tables),
            "images_extracted": len(images),
            "output_paths": output_paths,
        }

    # ── Step 1: Text extraction with layout preservation ──────────────

    def _extract_text_by_page(self, doc: fitz.Document) -> List[Dict]:
        """
        Extract text from each page preserving layout structure.
        Uses PyMuPDF's text extraction with blocks for spatial info.
        """
        pages = []

        for page_num in range(len(doc)):
            page = doc[page_num]

            # Get text with layout preservation (sorts by position)
            raw_text = page.get_text("text", sort=True)

            # Also get structured blocks for spatial analysis
            blocks = page.get_text("dict", sort=True)["blocks"]

            text_blocks = []
            for block in blocks:
                if block["type"] == 0:  # text block
                    block_text = ""
                    for line in block.get("lines", []):
                        line_text = ""
                        for span in line.get("spans", []):
                            line_text += span["text"]
                        block_text += line_text + "\n"

                    block_text = block_text.strip()
                    if block_text:
                        text_blocks.append({
                            "text": block_text,
                            "bbox": list(block["bbox"]),
                            "is_heading": self._is_heading(block),
                        })

            pages.append({
                "page_number": page_num + 1,
                "raw_text": raw_text.strip(),
                "text_blocks": text_blocks,
                "char_count": len(raw_text.strip()),
            })

        return pages

    def _is_heading(self, block: Dict) -> bool:
        """Detect if a text block is likely a heading based on font properties."""
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                font_size = span.get("size", 0)
                flags = span.get("flags", 0)
                is_bold = bool(flags & 2**4)  # bit 4 = bold
                text = span.get("text", "").strip()

                # Headings: large font, bold, or ALL CAPS short text
                if font_size >= 14:
                    return True
                if is_bold and font_size >= 11 and len(text) < 80:
                    return True
                if text.isupper() and 3 < len(text) < 60 and font_size >= 10:
                    return True
        return False

    # ── Step 2: Section detection ─────────────────────────────────────

    def _detect_sections(self, pages: List[Dict]) -> List[Dict]:
        """
        Identify logical sections from page text blocks.
        Merges heading blocks with their content.
        """
        sections = []
        current_section = {"title": "Document Start", "content": [], "page": 1}

        for page in pages:
            for block in page["text_blocks"]:
                if block["is_heading"]:
                    # Save previous section if it has content
                    if current_section["content"]:
                        current_section["content"] = "\n".join(current_section["content"])
                        sections.append(current_section)

                    current_section = {
                        "title": block["text"].strip(),
                        "content": [],
                        "page": page["page_number"],
                    }
                else:
                    current_section["content"].append(block["text"])

        # Don't forget last section
        if current_section["content"]:
            current_section["content"] = "\n".join(current_section["content"])
            sections.append(current_section)

        return sections

    # ── Step 3: Table detection ───────────────────────────────────────

    def _extract_tables(self, doc: fitz.Document) -> List[Dict]:
        """
        Detect and extract table-like structures using PyMuPDF's
        line/rect analysis and text positioning.
        """
        all_tables = []

        for page_num in range(len(doc)):
            page = doc[page_num]

            # Use PyMuPDF's built-in table finder (available in recent versions)
            try:
                tables = page.find_tables()
                for table_idx, table in enumerate(tables):
                    rows = table.extract()
                    if not rows or len(rows) < 2:
                        continue

                    # Clean cells
                    cleaned_rows = []
                    for row in rows:
                        cleaned_row = [
                            cell.strip() if cell else ""
                            for cell in row
                        ]
                        cleaned_rows.append(cleaned_row)

                    # Try to identify header row
                    header = cleaned_rows[0] if cleaned_rows else []
                    data_rows = cleaned_rows[1:] if len(cleaned_rows) > 1 else []

                    all_tables.append({
                        "page": page_num + 1,
                        "table_index": table_idx,
                        "header": header,
                        "rows": data_rows,
                        "row_count": len(data_rows),
                        "col_count": len(header),
                        "bbox": list(table.bbox) if hasattr(table, "bbox") else None,
                    })
            except AttributeError:
                # find_tables() not available — fall back to rect-based detection
                tables = self._detect_tables_from_rects(page, page_num)
                all_tables.extend(tables)

        return all_tables

    def _detect_tables_from_rects(self, page: fitz.Page, page_num: int) -> List[Dict]:
        """
        Fallback table detection using drawn rectangles and text alignment.
        Groups text blocks that are aligned in grid-like patterns.
        """
        drawings = page.get_drawings()
        if not drawings:
            return []

        # Find horizontal and vertical lines
        h_lines = []
        v_lines = []
        for d in drawings:
            for item in d.get("items", []):
                if item[0] == "l":  # line
                    p1, p2 = item[1], item[2]
                    if abs(p1.y - p2.y) < 2:  # horizontal
                        h_lines.append((min(p1.x, p2.x), p1.y, max(p1.x, p2.x)))
                    elif abs(p1.x - p2.x) < 2:  # vertical
                        v_lines.append((p1.x, min(p1.y, p2.y), max(p1.y, p2.y)))

        if len(h_lines) < 2 or len(v_lines) < 2:
            return []

        # There are lines forming a grid — extract text within the bounding area
        min_x = min(l[0] for l in h_lines)
        max_x = max(l[2] for l in h_lines)
        min_y = min(l[1] for l in h_lines)
        max_y = max(l[1] for l in h_lines)

        table_rect = fitz.Rect(min_x, min_y, max_x, max_y)
        text = page.get_text("text", clip=table_rect).strip()

        if text:
            lines = [line.strip() for line in text.split("\n") if line.strip()]
            return [{
                "page": page_num + 1,
                "table_index": 0,
                "header": [lines[0]] if lines else [],
                "rows": [[line] for line in lines[1:]],
                "row_count": len(lines) - 1,
                "col_count": 1,
                "bbox": [min_x, min_y, max_x, max_y],
                "detection_method": "rect_fallback",
            }]

        return []

    # ── Step 4: Image extraction + Pillow processing ──────────────────

    def _extract_images(self, doc: fitz.Document) -> List[Dict]:
        """
        Extract embedded images from the PDF using PyMuPDF.
        Returns image metadata + raw bytes for Pillow processing.
        """
        images = []
        seen_hashes = set()

        for page_num in range(len(doc)):
            page = doc[page_num]
            image_list = page.get_images(full=True)

            for img_idx, img_info in enumerate(image_list):
                xref = img_info[0]

                try:
                    base_image = doc.extract_image(xref)
                    if not base_image:
                        continue

                    image_bytes = base_image["image"]

                    # Skip duplicates (same image on multiple pages)
                    img_hash = hashlib.md5(image_bytes).hexdigest()
                    if img_hash in seen_hashes:
                        continue
                    seen_hashes.add(img_hash)

                    # Skip tiny images (likely icons/bullets)
                    width = base_image.get("width", 0)
                    height = base_image.get("height", 0)
                    if width < 50 or height < 50:
                        continue

                    images.append({
                        "page": page_num + 1,
                        "index": img_idx,
                        "xref": xref,
                        "width": width,
                        "height": height,
                        "colorspace": base_image.get("cs-name", "unknown"),
                        "bpc": base_image.get("bpc", 0),
                        "ext": base_image.get("ext", "png"),
                        "image_bytes": image_bytes,
                        "hash": img_hash,
                    })
                except Exception:
                    continue

        return images

    def _describe_images(self, images: List[Dict]) -> List[Dict]:
        """
        Use Pillow to analyze extracted images and produce descriptions.
        Classifies images as: label_diagram, table_image, barcode_example,
        flowchart, logo, or unknown.
        """
        descriptions = []

        for img in images:
            try:
                pil_image = Image.open(BytesIO(img["image_bytes"]))

                # Analyze image properties
                width, height = pil_image.size
                aspect_ratio = width / height if height > 0 else 0
                mode = pil_image.mode

                # Classify image type based on properties
                img_type = self._classify_image(pil_image, aspect_ratio)

                # Generate description
                description = self._generate_image_description(
                    img_type, width, height, aspect_ratio, img["page"]
                )

                descriptions.append({
                    "page": img["page"],
                    "index": img["index"],
                    "width": width,
                    "height": height,
                    "aspect_ratio": round(aspect_ratio, 2),
                    "mode": mode,
                    "type": img_type,
                    "description": description,
                    "filename": f"page{img['page']}_img{img['index']}.{img['ext']}",
                })
            except Exception:
                continue

        return descriptions

    def _classify_image(self, img: Image.Image, aspect_ratio: float) -> str:
        """
        Classify an image based on its visual properties.
        Uses Pillow analysis — no ML, just heuristics.
        """
        width, height = img.size

        # Convert to grayscale for analysis
        gray = img.convert("L")
        pixels = list(gray.getdata())
        total = len(pixels)

        if total == 0:
            return "unknown"

        # Calculate basic stats
        avg_brightness = sum(pixels) / total
        white_ratio = sum(1 for p in pixels if p > 240) / total
        black_ratio = sum(1 for p in pixels if p < 15) / total

        # High white ratio + some black lines = likely a diagram or label layout
        if white_ratio > 0.7 and black_ratio > 0.02:
            if 0.5 < aspect_ratio < 2.0 and width > 200:
                return "label_diagram"
            if aspect_ratio > 2.0 or aspect_ratio < 0.5:
                return "table_image"
            return "diagram"

        # Mostly black and white with structured patterns = barcode
        if (white_ratio + black_ratio) > 0.85 and width > 100:
            if aspect_ratio > 2.5:
                return "barcode_example"

        # Small, colorful = likely a logo
        if width < 300 and height < 300:
            return "logo"

        # Large with moderate content = label layout or flowchart
        if width > 400 and height > 400:
            return "label_diagram"

        return "unknown"

    def _generate_image_description(
        self, img_type: str, width: int, height: int,
        aspect_ratio: float, page: int
    ) -> str:
        """Generate a human-readable description of the image."""
        type_descriptions = {
            "label_diagram": f"Label layout diagram ({width}x{height}px) on page {page}. "
                           "Likely shows field positions and label structure.",
            "table_image": f"Table or structured data image ({width}x{height}px) on page {page}. "
                         "May contain field specifications in tabular format.",
            "barcode_example": f"Barcode example image ({width}x{height}px) on page {page}. "
                             "Shows barcode format/encoding requirements.",
            "diagram": f"Diagram or figure ({width}x{height}px) on page {page}. "
                      "May contain process flow or field relationships.",
            "flowchart": f"Flowchart ({width}x{height}px) on page {page}. "
                        "Shows decision logic or process steps.",
            "logo": f"Logo or icon ({width}x{height}px) on page {page}. "
                   "Likely carrier branding — not spec-relevant.",
            "unknown": f"Image ({width}x{height}px) on page {page}. "
                      "Content type unclear — may need manual review.",
        }
        return type_descriptions.get(img_type, type_descriptions["unknown"])

    # ── Step 5: Metadata extraction ───────────────────────────────────

    def _extract_metadata(self, doc: fitz.Document) -> Dict:
        """Extract PDF metadata (title, author, dates, etc.)."""
        meta = doc.metadata or {}
        return {
            "title": meta.get("title", ""),
            "author": meta.get("author", ""),
            "subject": meta.get("subject", ""),
            "creator": meta.get("creator", ""),
            "producer": meta.get("producer", ""),
            "creation_date": meta.get("creationDate", ""),
            "mod_date": meta.get("modDate", ""),
            "page_count": len(doc),
        }

    # ── Step 6: Save everything ───────────────────────────────────────

    def _save_extraction(self, result: Dict, images: List[Dict]) -> Dict:
        """
        Save extraction results to the Extracted/ directory.

        Creates:
            - full_text.txt         — all text concatenated
            - extraction.json       — structured extraction data
            - page_N.txt            — per-page text files
            - images/               — extracted images
            - tables.json           — extracted table data
            - sections.json         — detected sections
        """
        paths = {}

        # 1. Full concatenated text
        full_text = "\n\n".join(
            f"=== PAGE {p['page_number']} ===\n{p['raw_text']}"
            for p in result["pages"]
            if p["raw_text"]
        )
        full_text_path = self.extracted_dir / "full_text.txt"
        full_text_path.write_text(full_text, encoding="utf-8")
        paths["full_text"] = str(full_text_path)

        # 2. Per-page text files
        pages_dir = self.extracted_dir / "pages"
        pages_dir.mkdir(exist_ok=True)
        for page in result["pages"]:
            if page["raw_text"]:
                page_path = pages_dir / f"page_{page['page_number']:03d}.txt"
                page_path.write_text(page["raw_text"], encoding="utf-8")
        paths["pages_dir"] = str(pages_dir)

        # 3. Sections
        sections_path = self.extracted_dir / "sections.json"
        sections_path.write_text(
            json.dumps(result["sections"], indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        paths["sections"] = str(sections_path)

        # 4. Tables
        if result["tables"]:
            tables_path = self.extracted_dir / "tables.json"
            tables_path.write_text(
                json.dumps(result["tables"], indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
            paths["tables"] = str(tables_path)

        # 5. Images
        if images:
            images_dir = self.extracted_dir / "images"
            images_dir.mkdir(exist_ok=True)

            for img in images:
                img_filename = f"page{img['page']}_img{img['index']}.{img['ext']}"
                img_path = images_dir / img_filename
                img_path.write_bytes(img["image_bytes"])

            paths["images_dir"] = str(images_dir)

        # 6. Image descriptions
        if result["images"]:
            img_desc_path = self.extracted_dir / "image_descriptions.json"
            img_desc_path.write_text(
                json.dumps(result["images"], indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
            paths["image_descriptions"] = str(img_desc_path)

        # 7. Full extraction JSON (without raw image bytes or page raw_text duplication)
        extraction_meta = {
            "carrier_code": result["carrier_code"],
            "source_pdf": result["source_pdf"],
            "extracted_at": result["extracted_at"],
            "total_pages": result["total_pages"],
            "metadata": result["metadata"],
            "sections_count": len(result["sections"]),
            "tables_count": len(result["tables"]),
            "images_count": len(result["images"]),
        }
        meta_path = self.extracted_dir / "extraction_meta.json"
        meta_path.write_text(
            json.dumps(extraction_meta, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        paths["extraction_meta"] = str(meta_path)

        return paths


# ── Convenience function for use by routes ────────────────────────────

async def extract_carrier_pdf(carrier_code: str, pdf_path: str, spec_type: str = "label") -> Dict:
    """
    High-level function to extract a carrier spec PDF.

    Args:
        carrier_code: e.g. "dhl_express", "ups"
        pdf_path: Path to the uploaded PDF
        spec_type: "label" or "edi"

    Returns:
        Extraction result dict
    """
    extractor = PDFExtractor(carrier_code, spec_type=spec_type)
    return await extractor.extract(pdf_path)
