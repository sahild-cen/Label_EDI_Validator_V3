"""
Quick test script for the V3 PDF extraction pipeline.
Run from backend/:  python test_extraction.py

Tests against DHL Label Spec.pdf in uploads/.
"""

import asyncio
import sys
import json
from pathlib import Path

# Add parent to path so imports work
sys.path.insert(0, str(Path(__file__).parent))

from app.services.pdf_extractor import PDFExtractor, DOCS_BASE


async def test_extraction():
    # Find a test PDF
    uploads = Path("uploads")
    test_pdfs = [
        uploads / "DHL Label Spec.pdf",
    ]

    # Also grab the first label_spec PDF as fallback
    for f in sorted(uploads.glob("label_spec_*.pdf")):
        test_pdfs.append(f)
        break

    pdf_path = None
    for p in test_pdfs:
        if p.exists():
            pdf_path = p
            break

    if not pdf_path:
        print("ERROR: No test PDF found in uploads/")
        print("Available PDFs:", list(uploads.glob("*.pdf")))
        return

    print(f"Testing extraction with: {pdf_path}")
    print(f"File size: {pdf_path.stat().st_size / 1024:.1f} KB")
    print("-" * 60)

    extractor = PDFExtractor("dhl_express_test")
    result = await extractor.extract(str(pdf_path))

    print("\n=== EXTRACTION RESULTS ===")
    print(json.dumps(result, indent=2, default=str))

    # Show a preview of what was extracted
    print("\n=== TEXT PREVIEW (first 500 chars) ===")
    full_text_path = Path(result["output_paths"].get("full_text", ""))
    if full_text_path.exists():
        text = full_text_path.read_text(encoding="utf-8")
        print(text[:500])
        print(f"\n... ({len(text)} total characters)")

    # Show sections
    sections_path = Path(result["output_paths"].get("sections", ""))
    if sections_path.exists():
        sections = json.loads(sections_path.read_text(encoding="utf-8"))
        print(f"\n=== SECTIONS ({len(sections)}) ===")
        for s in sections[:10]:
            content_preview = s["content"][:80] if isinstance(s["content"], str) else ""
            print(f"  Page {s['page']}: {s['title'][:60]}")

    # Show tables
    tables_path = result["output_paths"].get("tables")
    if tables_path:
        tables = json.loads(Path(tables_path).read_text(encoding="utf-8"))
        print(f"\n=== TABLES ({len(tables)}) ===")
        for t in tables[:5]:
            print(f"  Page {t['page']}: {t['row_count']} rows x {t['col_count']} cols")
            if t["header"]:
                print(f"    Header: {t['header'][:5]}")

    # Show images
    img_desc_path = result["output_paths"].get("image_descriptions")
    if img_desc_path:
        images = json.loads(Path(img_desc_path).read_text(encoding="utf-8"))
        print(f"\n=== IMAGES ({len(images)}) ===")
        for img in images[:5]:
            print(f"  Page {img['page']}: {img['type']} - {img['description'][:60]}")

    print(f"\n=== OUTPUT DIR ===")
    print(f"  {DOCS_BASE / 'dhl_express_test'}")

    print("\nDone! Extraction pipeline working.")


if __name__ == "__main__":
    asyncio.run(test_extraction())
