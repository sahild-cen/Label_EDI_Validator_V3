# V3 Architecture — Claude Code Kickoff Prompt

> Copy everything below the line into Claude Code as your initial prompt when starting the V3 build.

---

## Context

I have an existing Label & EDI Validation System (V2) that extracts validation rules from carrier specification PDFs (UPS, DHL, FedEx, etc.) and validates ZPL shipping labels and EDI files against those rules. The current accuracy is ~60-70%.

**V2 problem:** It goes PDF → single Claude API call → JSON rules directly. This is a black box — when Claude misinterprets the spec, there's no way to catch or correct it before bad rules get generated.

**V3 goal:** Split that into inspectable, correctable steps with a human validation layer.

---

## V3 Architecture Overview

The system has TWO distinct workflows:

### Workflow 1: Carrier Setup (Admin/Dev only — runs rarely)
This is a multi-step pipeline that converts a carrier PDF spec into verified JSON validation rules. It is NOT a daily user workflow — it runs once per carrier, with human review.

```
PDF Upload
    ↓
Step 1: PDF Extraction (PyMuPDF + Pillow)
    - PyMuPDF extracts text content
    - Pillow processes images, tables, diagrams that PyMuPDF misses
    - Output: raw extracted text + image descriptions
    ↓
Step 2: Claude Analysis → Per-Field Spec Files
    - Extracted content sent to Claude API
    - Claude creates individual .md files per field in:
      docs/carriers/{carrier_code}/Spec/
    - Each .md file contains Claude's understanding of that field
      (format, validation rules, examples, edge cases, confidence notes)
    ↓
Step 3: Human Review & Correction ← THIS IS THE KEY ADDITION
    - Developer opens each .md file in Spec/ folder
    - Reviews Claude's interpretation against the actual PDF
    - Corrects any mistakes directly in the .md files
    - Marks files as reviewed/approved
    ↓
Step 4: JSON Rule Generation
    - Claude reads ALL finalized .md spec files for the carrier
    - Generates JSON validation rules (same format as V2)
    - Because input is now human-verified, accuracy should be much higher
```

### Workflow 2: Label Validation (Daily user workflow)
The existing validation dashboard — users upload ZPL labels or EDI files, system validates against the pre-generated JSON rules. This stays largely the same from V2.

---

## Tech Stack
- **Backend:** Python / FastAPI
- **Frontend:** React / TypeScript (validation page only — carrier setup may be CLI/script only)
- **Database:** MongoDB
- **PDF Processing:** PyMuPDF (text) + Pillow (images/tables)
- **LLM:** Claude API (Anthropic)
- **Label Format:** ZPL (Zebra Programming Language)

---

## File Structure (V3)

```
project-root/
├── app/
│   ├── main.py
│   ├── routes/
│   │   ├── validation.py          # Label validation endpoints (user-facing)
│   │   ├── corrections.py         # Feedback/corrections endpoints
│   │   └── carrier_setup.py       # Carrier setup endpoints (admin — optional API)
│   ├── services/
│   │   ├── pdf_extractor.py       # PyMuPDF + Pillow extraction pipeline
│   │   ├── spec_file_generator.py # Claude API → per-field .md files
│   │   ├── rule_generator.py      # Finalized .md files → JSON rules
│   │   ├── label_validator.py     # Validates labels against JSON rules
│   │   ├── zpl_parser.py          # ZPL spatial/semantic parser
│   │   ├── spec_matcher.py        # Auto-detect carrier from label
│   │   └── rule_canonicalizer.py  # Field name normalization
│   └── models/
│       └── ...
├── docs/
│   └── carriers/
│       └── {carrier_code}/        # One folder per carrier
│           ├── Documentation/     # Original uploaded PDFs
│           ├── Extracted/         # Raw extraction output (text + images)
│           ├── Spec/              # Per-field .md files (human-reviewable)
│           │   ├── tracking_number.md
│           │   ├── shipment_date.md
│           │   ├── service_type.md
│           │   ├── weight.md
│           │   ├── routing_barcode.md
│           │   └── ...            # One file per field
│           └── Rules/             # Final JSON rules (generated after review)
│               └── rules.json
├── frontend/
│   └── src/
│       ├── components/
│       │   └── ValidationDashboard.tsx
│       └── services/
│           └── api.ts
└── CLAUDE.md                      # This file (Claude Code instructions)
```

---

## Per-Field Spec File Format

Each file in `docs/carriers/{carrier_code}/Spec/` follows this structure. This is a template — Claude should adapt based on what the PDF actually contains for each field:

```markdown
# Field: {field_name_snake_case}

## Display Name
{Human readable name, e.g. "Tracking Number", "Shipment Date"}

## Field Description
{What this field represents according to the carrier spec. 1-2 sentences.}

## Format & Validation Rules
- **Data Type:** {string | numeric | date | alphanumeric | etc.}
- **Length:** {exact length, min-max range, or variable}
- **Pattern/Regex:** {if the spec defines a format pattern}
- **Allowed Values:** {enumerated values if applicable}
- **Required:** {yes | no | conditional — explain condition}

## Examples from Spec
{Copy exact examples from the carrier PDF. If none provided, state "No examples in spec."}
- Valid: `{example}`
- Valid: `{example}`
- Invalid: `{example}` (reason)

## Position on Label
{Where this field typically appears on the ZPL label — e.g., "Bottom barcode area", "Ship-to block", "Service banner". If not specified, state "Not specified in PDF."}

## Edge Cases & Notes
{Anything unusual, conditional logic, carrier-specific quirks, version differences, etc.}

## Claude Confidence
{HIGH | MEDIUM | LOW}
{Brief explanation — e.g., "HIGH — spec clearly defines format with regex and examples" or "LOW — only mentioned once in passing, no format details given"}

## Review Status
- [ ] Reviewed by human
```

---

## Key Design Principles (MUST follow)

1. **No hardcoded carrier logic** — every fix must work across all carriers. No `if carrier == "DHL"` blocks.
2. **Learning over patching** — the system improves through human corrections to spec files, not code changes.
3. **Inspectable intermediate state** — the .md spec files ARE the correction mechanism. If Claude misreads the PDF, the human fixes the .md file, and rule generation uses the corrected version.
4. **Carrier setup UI is optional** — this workflow can be script/CLI-driven. The validation dashboard is the only required UI.
5. **Extraction accuracy > speed** — use both PyMuPDF AND Pillow for PDF processing. Better to be slow and accurate than fast and wrong.
6. **Existing V2 validation logic stays** — the label validation pipeline (zpl_parser, label_validator, corrections feedback loop) carries over. We're improving the RULE GENERATION side, not the validation side.

---

## What to Build First

### Phase 1: PDF Extraction Pipeline
- `pdf_extractor.py` — PyMuPDF for text extraction, Pillow for image/table processing
- Test with existing carrier PDFs (DHL Express, UPS)
- Output: clean extracted text + image descriptions saved to `docs/carriers/{carrier_code}/Extracted/`

### Phase 2: Spec File Generator
- `spec_file_generator.py` — sends extracted content to Claude API
- Claude identifies all fields mentioned in the spec
- Creates one .md file per field in `Spec/` folder using the format above
- Must handle large PDFs (chunk if needed, but maintain context)

### Phase 3: Rule Generator (from finalized specs)
- `rule_generator.py` — reads ALL .md files in a carrier's `Spec/` folder
- Generates JSON rules in the same format V2 uses
- This runs AFTER human review, so input is trusted

### Phase 4: Wire into existing validation
- Connect generated rules to the existing label_validator pipeline
- Ensure ValidationDashboard.tsx works with V3-generated rules
- Carry over the corrections feedback loop from V2

---

## Existing V2 Files to Preserve/Migrate

These files from V2 contain working logic that should carry into V3:
- `zpl_parser.py` — spatial/semantic ZPL parser (keep as-is)
- `label_validator.py` — validation engine with mandatory overrides (keep, may need minor updates)
- `spec_matcher.py` — carrier auto-detection (keep as-is)
- `rule_canonicalizer.py` — field name normalization (keep as-is)
- `corrections.py` — feedback route with 4 correction types (keep as-is)
- `ValidationDashboard.tsx` — label-first UX with brown #4a4337 theme (keep as-is)

---

## MongoDB Collections

### From V2 (keep):
- `validation_corrections` — user feedback (false_positive, wrong_regex, wrong_required, missing_failure)
- `mandatory_field_overrides` — user-reported required field overrides
- `validation_rules` — generated JSON rules per carrier

### New for V3:
- `carrier_specs` — metadata about carrier spec files (carrier_code, field_count, review_status, extraction_date)
- `spec_review_log` — tracks which .md files have been human-reviewed and when

---

## Important Context from V2

- Sub-constraints (e.g., `license_plate_length`, `routing_barcode_prefix`) must NOT be classified as separate `DATA_VALIDATION` rules — they're sub-components of parent fields
- Bad LLM-extracted regexes (e.g., max quantifier < 15 for tracking numbers) are caught by `_tracking_regex_looks_wrong()` heuristic
- The corrections DB injects few-shot examples into the Pass 2 validation prompt
- Field name aliasing in `rule_canonicalizer.py` maps spec variants (e.g., "Piece Count" vs "piece_count") to canonical names
- `@app.on_event("startup")` must appear AFTER `app = FastAPI(...)` in main.py

---

## Start Here

Begin with Phase 1 (PDF Extraction Pipeline). Read the existing V2 code in the project to understand the current structure, then build `pdf_extractor.py` as a new service. Test it against a carrier PDF in the Documentation folder before moving to Phase 2.