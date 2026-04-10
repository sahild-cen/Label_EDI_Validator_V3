"""
V3 Carrier Setup Routes — Admin workflow for building carrier spec files.

Workflow:
    1. POST /extract                     — Phase 1: Upload PDF, run extraction
    2. POST /generate-specs/{code}       — Phase 2: Claude generates per-field .md spec files
    3. GET  /status/{code}               — Check extraction + review status
    4. GET  /spec-file/{code}/{field}    — View/edit a specific spec file
    5. POST /generate-rules/{code}       — Phase 3: Generate JSON rules from reviewed specs
    6. GET  /carriers                    — List all carriers with V3 setup status
    7. GET  /extracted/{code}            — View raw extracted content
"""

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import Optional
from pathlib import Path

from app.services.pdf_extractor import PDFExtractor, extract_carrier_pdf, DOCS_BASE
from app.utils.file_handler import save_upload_file
from app.database import get_database

import json

router = APIRouter(prefix="/api/carrier-setup", tags=["carrier-setup"])


# ═══════════════════════════════════════════════════════════════
# STEP 1: PDF EXTRACTION
# ═══════════════════════════════════════════════════════════════

@router.post("/extract")
async def extract_carrier_spec(
    carrier_code: str = Form(..., description="e.g. dhl_express, ups, fedex"),
    spec_file: UploadFile = File(..., description="Carrier specification PDF"),
    spec_type: str = Form("label", description="'label' or 'edi'"),
):
    """
    Upload a carrier spec PDF and run the V3 extraction pipeline.

    Extracts text, images, tables and saves to:
        docs/carriers/{carrier_code}/{spec_type}/Extracted/

    spec_type must be 'label' or 'edi'.
    """
    if spec_type not in ("label", "edi"):
        raise HTTPException(status_code=400, detail="spec_type must be 'label' or 'edi'")
    if not spec_file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    pdf_path = await save_upload_file(spec_file, f"carrier_{spec_type}_spec")

    try:
        result = await extract_carrier_pdf(carrier_code, pdf_path, spec_type=spec_type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Extraction failed: {str(e)}")

    code = carrier_code.lower().replace(" ", "_")
    db = get_database()

    # Path where the PDF was copied during extraction
    doc_pdf_path = str(DOCS_BASE / code / spec_type / "Documentation" / spec_file.filename)
    spec_path_field = f"{spec_type}_spec_path"

    # 1. Update carrier_specs metadata
    await db.carrier_specs.update_one(
        {"carrier_code": code},
        {
            "$set": {
                "carrier_code": code,
                f"{spec_type}_source_pdf": spec_file.filename,
                f"{spec_type}_total_pages": result["total_pages"],
                f"{spec_type}_sections_detected": result["sections_detected"],
                f"{spec_type}_tables_detected": result["tables_detected"],
                f"{spec_type}_images_extracted": result["images_extracted"],
                f"{spec_type}_extraction_status": "completed",
                f"{spec_type}_output_paths": result["output_paths"],
            },
            "$currentDate": {f"{spec_type}_extracted_at": True},
        },
        upsert=True,
    )

    # 2. Upsert into carriers collection so it shows in the carrier list
    #    and the PDF viewer can find the file
    await db.carriers.update_one(
        {"carrier": carrier_code},
        {
            "$set": {
                "carrier": carrier_code,
                spec_path_field: doc_pdf_path,
            }
        },
        upsert=True,
    )

    # ── Auto-run Phase 2: Generate per-field .md spec files ──
    phase2 = {"success": False, "message": "Not attempted"}
    try:
        from app.services.spec_file_generator import generate_spec_files as _gen_specs
        phase2 = await _gen_specs(code, spec_type=spec_type)
    except Exception as e:
        phase2 = {"success": False, "error": str(e)}

    return {
        "success": True,
        "spec_type": spec_type,
        "message": f"Extraction & spec generation complete for {carrier_code}",
        "spec_dir": str(DOCS_BASE / code / spec_type / "Spec"),
        "phase2": phase2,
        **result,
    }


# ═══════════════════════════════════════════════════════════════
# STATUS & VIEWING
# ═══════════════════════════════════════════════════════════════

@router.get("/status/{carrier_code}")
async def get_extraction_status(carrier_code: str):
    """Check extraction and review status for a carrier."""
    code = carrier_code.lower().replace(" ", "_")
    db = get_database()

    spec_doc = await db.carrier_specs.find_one(
        {"carrier_code": code}, {"_id": 0}
    )
    if not spec_doc:
        raise HTTPException(status_code=404, detail=f"No extraction found for {carrier_code}")

    # Check spec files review status
    spec_dir = DOCS_BASE / code / "Spec"
    spec_files = []
    if spec_dir.exists():
        for f in sorted(spec_dir.glob("*.md")):
            content = f.read_text(encoding="utf-8")
            reviewed = "- [x] Reviewed by human" in content
            spec_files.append({
                "filename": f.name,
                "field": f.stem,
                "reviewed": reviewed,
            })

    return {
        "carrier_code": code,
        "extraction": spec_doc,
        "spec_files": spec_files,
        "spec_files_count": len(spec_files),
        "reviewed_count": sum(1 for s in spec_files if s["reviewed"]),
    }


@router.get("/extracted/{carrier_code}")
async def get_extracted_content(carrier_code: str, page: Optional[int] = None):
    """
    View extracted content for a carrier.
    Optionally filter by page number.
    """
    code = carrier_code.lower().replace(" ", "_")
    extracted_dir = DOCS_BASE / code / "Extracted"

    if not extracted_dir.exists():
        raise HTTPException(status_code=404, detail=f"No extracted content for {carrier_code}")

    result = {}

    # Read extraction metadata
    meta_path = extracted_dir / "extraction_meta.json"
    if meta_path.exists():
        result["metadata"] = json.loads(meta_path.read_text(encoding="utf-8"))

    # Read sections
    sections_path = extracted_dir / "sections.json"
    if sections_path.exists():
        result["sections"] = json.loads(sections_path.read_text(encoding="utf-8"))

    # Read tables
    tables_path = extracted_dir / "tables.json"
    if tables_path.exists():
        result["tables"] = json.loads(tables_path.read_text(encoding="utf-8"))

    # Read image descriptions
    img_path = extracted_dir / "image_descriptions.json"
    if img_path.exists():
        result["images"] = json.loads(img_path.read_text(encoding="utf-8"))

    # Read text (optionally filtered by page)
    if page:
        page_file = extracted_dir / "pages" / f"page_{page:03d}.txt"
        if page_file.exists():
            result["text"] = page_file.read_text(encoding="utf-8")
        else:
            raise HTTPException(status_code=404, detail=f"Page {page} not found")
    else:
        full_text_path = extracted_dir / "full_text.txt"
        if full_text_path.exists():
            result["text"] = full_text_path.read_text(encoding="utf-8")

    return {
        "success": True,
        "carrier_code": code,
        **result,
    }


@router.get("/carriers")
async def list_carrier_setups():
    """List all carriers that have been through the V3 setup pipeline."""
    db = get_database()
    cursor = db.carrier_specs.find({}, {"_id": 0})
    carriers = await cursor.to_list(length=100)

    # Enrich with spec file counts
    for carrier in carriers:
        code = carrier.get("carrier_code", "")
        spec_dir = DOCS_BASE / code / "Spec"
        if spec_dir.exists():
            md_files = [f for f in spec_dir.glob("*.md") if not f.name.startswith("_")]
            carrier["spec_file_count"] = len(md_files)
            carrier["reviewed_count"] = sum(
                1 for f in md_files
                if "- [x] Reviewed by human" in f.read_text(encoding="utf-8")
            )
        else:
            carrier["spec_file_count"] = 0
            carrier["reviewed_count"] = 0

        rules_dir = DOCS_BASE / code / "Rules"
        carrier["rules_generated"] = (rules_dir / "rules.json").exists()

    return {"success": True, "carriers": carriers}


# ═══════════════════════════════════════════════════════════════
# PHASE 2: SPEC FILE GENERATION
# ═══════════════════════════════════════════════════════════════

@router.post("/generate-specs/{carrier_code}")
async def generate_spec_files(carrier_code: str, spec_type: str = "label"):
    """
    Phase 2: Use Claude to generate per-field .md spec files from extracted content.

    Reads from:  docs/carriers/{carrier_code}/{spec_type}/Extracted/
    Writes to:   docs/carriers/{carrier_code}/{spec_type}/Spec/

    spec_type: 'label' or 'edi'
    """
    from app.services.spec_file_generator import generate_spec_files as _generate

    if spec_type not in ("label", "edi"):
        raise HTTPException(status_code=400, detail="spec_type must be 'label' or 'edi'")

    code = carrier_code.lower().replace(" ", "_")

    extracted_dir = DOCS_BASE / code / spec_type / "Extracted"
    if not extracted_dir.exists():
        raise HTTPException(
            status_code=400,
            detail=f"No {spec_type} extracted content for '{carrier_code}'. Run POST /extract with spec_type={spec_type} first.",
        )

    try:
        result = await _generate(code, spec_type=spec_type)
    except FileNotFoundError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Spec generation failed: {str(e)}")

    db = get_database()
    await db.carrier_specs.update_one(
        {"carrier_code": code},
        {
            "$set": {
                f"{spec_type}_spec_files_generated": result.get("success", False),
                f"{spec_type}_spec_files_count": result.get("files_created", 0),
            },
            "$currentDate": {f"{spec_type}_specs_generated_at": True},
        },
        upsert=True,
    )

    return result


# ═══════════════════════════════════════════════════════════════
# SPEC FILE VIEWER / EDITOR SUPPORT
# ═══════════════════════════════════════════════════════════════

@router.get("/spec-file/{carrier_code}/{field_name}")
async def get_spec_file(carrier_code: str, field_name: str):
    """
    Get the content of a specific spec file for review/editing.
    Returns raw markdown content + review status.
    """
    code = carrier_code.lower().replace(" ", "_")
    safe_field = field_name.lower().replace(" ", "_")
    spec_path = DOCS_BASE / code / "Spec" / f"{safe_field}.md"

    if not spec_path.exists():
        raise HTTPException(
            status_code=404,
            detail=f"Spec file '{safe_field}.md' not found for carrier '{code}'.",
        )

    content = spec_path.read_text(encoding="utf-8")
    reviewed = "- [x] Reviewed by human" in content

    return {
        "carrier_code": code,
        "field_name": safe_field,
        "content": content,
        "reviewed": reviewed,
        "file_path": str(spec_path),
    }


@router.get("/spec-files/{carrier_code}")
async def list_spec_files(carrier_code: str, spec_type: str = "label"):
    """List all spec files for a carrier with their review status."""
    if spec_type not in ("label", "edi"):
        raise HTTPException(status_code=400, detail="spec_type must be 'label' or 'edi'")

    code = carrier_code.lower().replace(" ", "_")
    spec_dir = DOCS_BASE / code / spec_type / "Spec"

    if not spec_dir.exists():
        return {
            "carrier_code": code,
            "spec_type": spec_type,
            "total_files": 0,
            "reviewed_count": 0,
            "pending_count": 0,
            "files": [],
        }

    files = []
    for path in sorted(spec_dir.glob("*.md")):
        if path.name.startswith("_"):
            continue
        content = path.read_text(encoding="utf-8")
        reviewed = "- [x] Reviewed by human" in content
        files.append({
            "field_name": path.stem,
            "filename": path.name,
            "reviewed": reviewed,
            "size_chars": len(content),
        })

    reviewed_count = sum(1 for f in files if f["reviewed"])
    return {
        "carrier_code": code,
        "spec_type": spec_type,
        "total_files": len(files),
        "reviewed_count": reviewed_count,
        "pending_count": len(files) - reviewed_count,
        "files": files,
    }


# ═══════════════════════════════════════════════════════════════
# PHASE 3: RULE GENERATION
# ═══════════════════════════════════════════════════════════════

@router.post("/generate-rules/{carrier_code}")
async def generate_rules(
    carrier_code: str,
    spec_type: str = "label",
    reviewed_only: bool = False,
):
    """
    Phase 3: Generate JSON validation rules from reviewed spec files.

    Reads from:   docs/carriers/{carrier_code}/{spec_type}/Spec/*.md
    Writes to:    docs/carriers/{carrier_code}/{spec_type}/Rules/rules.json
                  MongoDB carriers collection (active versioned rules)

    spec_type: 'label' or 'edi'
    reviewed_only: if true, only use spec files marked as reviewed.
    """
    from app.services.rule_generator import generate_rules_from_specs

    if spec_type not in ("label", "edi"):
        raise HTTPException(status_code=400, detail="spec_type must be 'label' or 'edi'")

    code = carrier_code.lower().replace(" ", "_")

    spec_dir = DOCS_BASE / code / spec_type / "Spec"
    if not spec_dir.exists() or not any(spec_dir.glob("*.md")):
        raise HTTPException(
            status_code=400,
            detail=f"No {spec_type} spec files for '{code}'. Run Phase 2 first.",
        )

    db = get_database()

    try:
        result = await generate_rules_from_specs(
            carrier_code=code,
            db=db,
            reviewed_only=reviewed_only,
            spec_type=spec_type,
        )
    except FileNotFoundError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Rule generation failed: {str(e)}")

    return result
