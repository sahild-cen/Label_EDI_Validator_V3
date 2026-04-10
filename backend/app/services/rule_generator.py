"""
V3 Phase 3: Rule Generator

Reads all .md spec files from docs/carriers/{carrier_code}/Spec/
and generates JSON validation rules.

This step runs AFTER human review. Input is trusted.
Claude's role here is to:
  1. Parse each spec file and understand the field semantics
  2. Generate detect_by instructions (ZPL-specific, not in spec files)
  3. Extract regex patterns from human-written format descriptions
  4. Build final JSON rules

Output:
  - docs/carriers/{carrier_code}/Rules/rules.json  (file-based copy)
  - MongoDB carriers collection (active versioned rules for live validation)
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime, timezone

from app.services.pdf_extractor import DOCS_BASE
from app.services.claude_service import client, deployment_name, extract_json_from_text


RULE_GENERATION_PROMPT = """\
You are an expert in ZPL (Zebra Programming Language) shipping label validation and logistics carrier specifications.

Carrier: {carrier_code}

Below are human-reviewed specification files for each field on this carrier's shipping labels.
Your job is to convert them into precise JSON validation rules.

For each field, you must provide:

1. field: snake_case field name
2. required: true or false (from "Required" section of spec file)
3. detect_by: HOW a ZPL label parser finds this field (critical — see instructions below)
4. regex: validation pattern (from Pattern/Regex section, or derive from format description)
5. description: 1-sentence description
6. zpl_position: approximate X,Y position from the "ZPL Rendering" section (e.g. "50,100" or "" if unknown)
7. zpl_font: ZPL font command from the spec (e.g. "^A0N,30,30" or "^CF0,25" or "" if unknown)
8. field_prefix: the literal text prefix before the data (e.g. "DATE:", "SHP WT:", "DESC:"). Empty string for barcodes/graphics or fields with no prefix.

═══ DETECT_BY INSTRUCTIONS ═══

Choose the most precise detect_by type for each field:

  zpl_command:^BD         For fields identified by a ZPL command in the script
                          Examples: MaxiCode (^BD), PDF417 (^B7), GS1 DataMatrix (^BX)

  barcode_data:^1Z        For barcodes whose DATA matches a regex prefix
                          Examples: UPS tracking (^1Z), DHL tracking (^JD|^JJD),
                          FedEx tracking (^\\d{{12,20}}$)

  text_prefix:DATE:       For text that STARTS WITH a known literal prefix
                          Examples: DATE:, BILLING:, REF:, SHP WT:, TRACKING #:, MRN:

  text_contains:phrase    For text that CONTAINS a phrase (case-insensitive)
                          Examples: "SHIPPER'S LETTER OF INSTRUCTION", "Terms and Conditions"

  text_pattern:regex      For text matching a REGEX PATTERN
                          Examples: routing code (^[A-Z]{{2,3}} \\d{{3}}), package count (\\d+ OF \\d+),
                          service title (^UPS |^DHL |^FEDEX )

  text_exact:A|B|C        For text that EQUALS one of a set of values
                          Examples: country codes (US|CA|MX), doc types (EDI|DOC|INV)

  graphic:GFA             For graphic/image elements in the ZPL
                          Examples: carrier logo, service icon

  spatial:ship_from       For the shipper address block
  spatial:ship_to         For the consignee/recipient address block

When in doubt, prefer text_prefix or text_pattern over spatial.
Always provide a detect_by — never leave it empty.

═══ REGEX RULES ═══

- Only include regex if the spec file's Format section specifies a clear pattern
- For tracking numbers: capture the full format (e.g., ^1Z[A-Z0-9]{{16}}$)
- For postal codes: match the country-specific format
- For dates: match the spec's stated date format
- If no clear pattern in spec, set regex to ""

═══ REQUIRED FIELD ═══

- required: true if spec says "required", "mandatory", "must appear", or field is in a required table
- required: false if spec says "optional", "conditional", or "when applicable"

═══ OUTPUT FORMAT ═══

Return ONLY valid JSON:
{{
  "carrier_code": "{carrier_code}",
  "rules": [
    {{
      "field": "tracking_number",
      "required": true,
      "detect_by": "barcode_data:^1Z",
      "regex": "^1Z[A-Z0-9]{{16}}$",
      "description": "UPS tracking barcode in 1Z format, 18 characters total",
      "zpl_position": "50,800",
      "zpl_font": "",
      "field_prefix": "TRACKING #:"
    }},
    {{
      "field": "maxicode",
      "required": true,
      "detect_by": "zpl_command:^BD",
      "regex": "",
      "description": "MaxiCode 2D barcode encoding routing and postal information",
      "zpl_position": "50,400",
      "zpl_font": "",
      "field_prefix": ""
    }},
    {{
      "field": "shipment_date",
      "required": true,
      "detect_by": "text_prefix:DATE:",
      "regex": "^\\d{{2}}/\\d{{2}}/\\d{{4}}$",
      "description": "Shipment date in MM/DD/YYYY format",
      "zpl_position": "400,50",
      "zpl_font": "^A0N,20,20",
      "field_prefix": "DATE:"
    }}
  ]
}}

═══ SPEC FILES ═══

{spec_files_content}
"""


EDI_RULE_GENERATION_PROMPT = """\
You are an expert in EDI (Electronic Data Interchange) standards including ANSI X12, UN/EDIFACT, and carrier-specific formats.

Carrier: {carrier_code}

Below are human-reviewed specification files for this carrier's EDI requirements.
Your job is to convert them into precise JSON validation rules.

═══ WHAT TO IDENTIFY ═══

1. **format_type**: x12, edifact, xml, json — whichever the spec describes
2. **required_segments**: Segment IDs that MUST be present
3. **segment_order**: The correct sequence of segments
4. **required_fields**: Data fields that must have values
5. **delimiter_rules**: Expected delimiters for the format
6. **field_rules**: Per-field validation (segment, position, format, regex)

═══ X12 COMMON SEGMENTS ═══

ISA — Interchange Control Header
GS  — Functional Group Header
ST  — Transaction Set Header (e.g., 856=ASN, 204=Motor Carrier Load Tender)
BSN — Beginning Segment for Ship Notice
HL  — Hierarchical Level
TD1/TD3/TD5 — Carrier/Transport Details
N1/N3/N4    — Name/Address
REF — Reference Identification
DTM — Date/Time Reference
SE  — Transaction Set Trailer
GE  — Functional Group Trailer
IEA — Interchange Control Trailer

═══ EDIFACT COMMON SEGMENTS ═══

UNA — Service String Advice
UNB — Interchange Header
UNH — Message Header
BGM — Beginning of Message
DTM — Date/Time/Period
NAD — Name and Address
TDT — Transport Information
LOC — Place/Location Identification
RFF — Reference
GID — Goods Item Details
MEA — Measurements
PCI — Package Identification
CNT — Control Total
UNT — Message Trailer
UNZ — Interchange Trailer

═══ OUTPUT FORMAT ═══

Return ONLY valid JSON:
{{
  "carrier_code": "{carrier_code}",
  "format_type": "x12",
  "required_segments": ["ISA", "GS", "ST", "BSN", "HL", "TD5", "N1", "REF", "DTM", "SE", "GE", "IEA"],
  "segment_order": ["ISA", "GS", "ST", "BSN", "HL", "TD5", "N1", "REF", "DTM", "SE", "GE", "IEA"],
  "required_fields": ["sender_id", "receiver_id", "transaction_set_id", "shipment_id"],
  "delimiter_rules": {{
    "segment_delimiter": "~",
    "element_delimiter": "*",
    "sub_element_delimiter": ":"
  }},
  "field_rules": [
    {{
      "field": "sender_id",
      "segment": "ISA",
      "position": 6,
      "required": true,
      "regex": "",
      "description": "Interchange sender identification"
    }}
  ]
}}

═══ RULES ═══

- required_segments: include ALL segments the spec says are mandatory
- segment_order: list segments in the order they should appear per the spec
- required_fields: list all fields/data elements that must have values
- delimiter_rules: specify the actual delimiters (~ for X12, ' for EDIFACT, etc.)
- field_rules: for each important field, specify segment, element position, and any regex pattern
- If the spec mentions a specific standard version (4010, 5010, D96A), include it in the description
- Set required: true only for mandatory fields; conditional fields are required: false

═══ SPEC FILES ═══

{spec_files_content}
"""


# Max spec files per Claude call — above this we batch to avoid truncation
MAX_SPECS_PER_BATCH = 20


def _merge_rules(batches: List[List[Dict]]) -> List[Dict]:
    """
    Merge rule lists from multiple Claude calls.
    Deduplicates by field name, keeping the entry with more content.
    """
    seen: Dict[str, Dict] = {}
    for batch in batches:
        for rule in batch:
            field = rule.get("field", "").strip()
            if not field:
                continue
            if field not in seen:
                seen[field] = rule
            else:
                # Keep the one with a longer description or non-empty regex
                existing = seen[field]
                if len(rule.get("description", "")) > len(existing.get("description", "")) or (
                    rule.get("regex") and not existing.get("regex")
                ):
                    seen[field] = rule
    return list(seen.values())


def _call_claude_for_edi_rules(carrier_code: str, spec_context: str) -> Optional[Dict]:
    """
    Call Claude to generate EDI rules. Returns full rule dict with
    required_segments, segment_order, field_rules, etc.
    """
    if not client:
        print("[Phase 3] Claude client not initialized")
        return None

    prompt = EDI_RULE_GENERATION_PROMPT.format(
        carrier_code=carrier_code,
        spec_files_content=spec_context,
    )

    print(f"  [Phase 3-EDI] Calling Claude ({len(spec_context):,} chars of spec content)...")

    try:
        response = client.messages.create(
            model=deployment_name,
            max_tokens=8192,
            messages=[{"role": "user", "content": prompt}],
        )

        if not response.content:
            print("  [Phase 3-EDI] Empty response from Claude")
            return None

        text = response.content[0].text
        data = extract_json_from_text(text)

        if not data:
            print("  [Phase 3-EDI] Could not parse JSON from Claude response")
            return None

        segs = len(data.get("required_segments", []))
        fields = len(data.get("field_rules", []))
        print(f"    -> Got {segs} segments, {fields} field rules")
        return data

    except Exception as e:
        print(f"  [Phase 3-EDI] Claude error: {e}")
        return None


def _merge_edi_rules(batches: List[Dict]) -> Dict:
    """Merge EDI rule dicts from multiple Claude calls."""
    merged: Dict = {
        "required_segments": [],
        "segment_order": [],
        "required_fields": [],
        "delimiter_rules": {},
        "format_type": "",
        "field_rules": [],
    }

    seen_segments: set = set()
    seen_fields: set = set()
    seen_rule_fields: set = set()

    for batch in batches:
        for seg in batch.get("required_segments", []):
            if seg not in seen_segments:
                seen_segments.add(seg)
                merged["required_segments"].append(seg)

        # Keep the longest segment_order
        if len(batch.get("segment_order", [])) > len(merged["segment_order"]):
            merged["segment_order"] = batch["segment_order"]

        for field in batch.get("required_fields", []):
            if field not in seen_fields:
                seen_fields.add(field)
                merged["required_fields"].append(field)

        if not merged["delimiter_rules"] and batch.get("delimiter_rules"):
            merged["delimiter_rules"] = batch["delimiter_rules"]

        if not merged["format_type"] and batch.get("format_type"):
            merged["format_type"] = batch["format_type"]

        for rule in batch.get("field_rules", []):
            field = rule.get("field", "")
            if field and field not in seen_rule_fields:
                seen_rule_fields.add(field)
                merged["field_rules"].append(rule)

    return merged


def _rules_to_edi_format(edi_data: Dict) -> Dict:
    """
    Convert EDI Claude output to the format expected by EDIValidator.
    """
    field_formats = {}
    for r in edi_data.get("field_rules", []):
        field = r.get("field", "")
        if field:
            field_formats[field] = {
                "segment": r.get("segment", ""),
                "position": r.get("position", 0),
                "pattern": r.get("regex", ""),
                "required": r.get("required", False),
                "description": r.get("description", ""),
            }

    return {
        "required_segments": edi_data.get("required_segments", []),
        "segment_order": edi_data.get("segment_order", []),
        "required_fields": edi_data.get("required_fields", []),
        "delimiter_rules": edi_data.get("delimiter_rules", {}),
        "format_type": edi_data.get("format_type", ""),
        "field_formats": field_formats,
        "confidence_score": 0.9,
    }


def _load_spec_files(carrier_code: str, spec_type: str = "label") -> List[Dict]:
    """
    Load all .md spec files from the Spec/ directory.
    Returns list of {field_name, content, reviewed} dicts.
    """
    spec_dir = DOCS_BASE / carrier_code / spec_type / "Spec"

    if not spec_dir.exists():
        raise FileNotFoundError(
            f"No Spec/ directory for '{carrier_code}'. Run Phase 2 first."
        )

    spec_files = []
    for path in sorted(spec_dir.glob("*.md")):
        if path.name.startswith("_"):
            continue  # skip meta files like _generation_meta.json

        content = path.read_text(encoding="utf-8")
        reviewed = "- [x] Reviewed by human" in content

        spec_files.append({
            "field_name": path.stem,
            "filename": path.name,
            "content": content,
            "reviewed": reviewed,
        })

    return spec_files


def _build_spec_context(spec_files: List[Dict], reviewed_only: bool = False) -> str:
    """
    Build a combined text block of all spec files for the Claude prompt.
    """
    files_to_use = spec_files
    if reviewed_only:
        files_to_use = [f for f in spec_files if f["reviewed"]]

    if not files_to_use:
        return ""

    parts = []
    for f in files_to_use:
        separator = "=" * 60
        review_status = "[REVIEWED]" if f["reviewed"] else "[PENDING REVIEW]"
        parts.append(
            f"{separator}\n"
            f"FILE: {f['filename']} {review_status}\n"
            f"{separator}\n"
            f"{f['content']}"
        )

    return "\n\n".join(parts)


def _call_claude_for_rules(carrier_code: str, spec_context: str) -> List[Dict]:
    """
    Call Claude to generate JSON rules from spec file content.
    Returns list of rule dicts.
    """
    if not client:
        print("[Phase 3] Claude client not initialized")
        return []

    prompt = RULE_GENERATION_PROMPT.format(
        carrier_code=carrier_code,
        spec_files_content=spec_context,
    )

    print(f"  [Phase 3] Calling Claude ({len(spec_context):,} chars of spec content)...")

    try:
        response = client.messages.create(
            model=deployment_name,
            max_tokens=8192,
            messages=[{"role": "user", "content": prompt}],
        )

        if not response.content:
            print("  [Phase 3] Empty response from Claude")
            return []

        text = response.content[0].text
        data = extract_json_from_text(text)

        if not data:
            print("  [Phase 3] Could not parse JSON from Claude response")
            return []

        rules = data.get("rules", [])
        print(f"    -> Generated {len(rules)} rule(s)")
        return rules

    except Exception as e:
        print(f"  [Phase 3] Claude error: {e}")
        return []


def _validate_and_clean_rules(rules: List[Dict]) -> List[Dict]:
    """
    Basic sanity checks on generated rules before saving.
    - Ensure required fields are present
    - Validate regex patterns
    - Normalize field names
    """
    cleaned = []
    for rule in rules:
        field = rule.get("field", "").strip()
        if not field:
            continue

        # Normalize field name
        field = re.sub(r"[^\w]", "_", field.lower()).strip("_")
        field = re.sub(r"_+", "_", field)

        # Validate regex
        regex = rule.get("regex", "")
        if regex:
            try:
                re.compile(regex)
                # Check for impossible quantifiers like {15,10}
                quants = re.findall(r"\{(\d+),(\d+)\}", regex)
                for min_v, max_v in quants:
                    if int(min_v) > int(max_v):
                        regex = ""
                        break
            except re.error:
                regex = ""

        # Ensure detect_by has a colon separator (type:value format)
        detect_by = rule.get("detect_by", "")
        if detect_by and ":" not in detect_by:
            detect_by = f"text_contains:{detect_by}"

        cleaned.append({
            "field": field,
            "required": bool(rule.get("required", False)),
            "detect_by": detect_by,
            "regex": regex,
            "description": rule.get("description", ""),
            "zpl_position": rule.get("zpl_position", ""),
            "zpl_font": rule.get("zpl_font", ""),
            "field_prefix": rule.get("field_prefix", ""),
        })

    return cleaned


def _rules_to_label_format(rules: List[Dict]) -> Dict:
    """
    Convert rule list to the label_rules dict format used by label_validator.py
    and stored in MongoDB carriers collection.

    Format:
    {
        "field_formats": {
            "field_name": {
                "pattern": "...",
                "required": true,
                "detect_by": "...",
                "description": "..."
            }
        },
        "required_fields": ["field1", "field2", ...]
    }
    """
    field_formats = {}
    required_fields = []

    for rule in rules:
        field = rule["field"]
        field_formats[field] = {
            "pattern": rule.get("regex", ""),
            "required": rule.get("required", False),
            "detect_by": rule.get("detect_by", ""),
            "description": rule.get("description", ""),
            "zpl_position": rule.get("zpl_position", ""),
            "zpl_font": rule.get("zpl_font", ""),
            "field_prefix": rule.get("field_prefix", ""),
        }
        if rule.get("required"):
            required_fields.append(field)

    return {
        "field_formats": field_formats,
        "required_fields": required_fields,
        "confidence_score": 0.9,  # high confidence: human-reviewed input
    }


async def generate_rules_from_specs(
    carrier_code: str,
    db=None,
    reviewed_only: bool = False,
    spec_type: str = "label",
) -> Dict:
    """
    Phase 3 main entry point.

    Reads reviewed .md spec files and generates JSON validation rules.
    Saves to {spec_type}/Rules/rules.json and MongoDB.

    Args:
        carrier_code: e.g. "dhl_express", "ups"
        db: MongoDB database object (required for saving to MongoDB)
        reviewed_only: if True, only use files marked as reviewed
        spec_type: "label" or "edi"

    Returns:
        Summary dict with rule counts and save status.
    """
    code = carrier_code.lower().replace(" ", "_")
    stype = spec_type.lower()
    rules_dir = DOCS_BASE / code / stype / "Rules"
    rules_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"[Phase 3] Generating {stype} rules for '{code}'")
    print(f"{'='*60}")

    # Step 1: Load spec files
    spec_files = _load_spec_files(code, spec_type=stype)
    total_files = len(spec_files)
    reviewed_files = sum(1 for f in spec_files if f["reviewed"])

    print(f"  Spec files: {total_files} total, {reviewed_files} reviewed")

    if total_files == 0:
        return {
            "success": False,
            "carrier_code": code,
            "message": "No .md spec files found. Run Phase 2 first.",
            "rules_generated": 0,
        }

    if reviewed_only and reviewed_files == 0:
        return {
            "success": False,
            "carrier_code": code,
            "message": (
                "No reviewed spec files found. "
                "Mark files as reviewed with '[x] Reviewed by human' first."
            ),
            "rules_generated": 0,
        }

    using_reviewed_only = reviewed_only and reviewed_files > 0
    files_to_use = [f for f in spec_files if f["reviewed"]] if using_reviewed_only else spec_files
    files_used = len(files_to_use)
    print(f"  Using: {files_used} file(s) {'(reviewed only)' if using_reviewed_only else '(all files)'}")

    # Step 2 + 3: Build context and call Claude (batched if many spec files)
    if files_used == 0:
        return {
            "success": False,
            "carrier_code": code,
            "spec_type": stype,
            "message": "Could not build spec context.",
            "rules_generated": 0,
        }

    # Split into batches to avoid truncated JSON output
    batches = [
        files_to_use[i : i + MAX_SPECS_PER_BATCH]
        for i in range(0, files_used, MAX_SPECS_PER_BATCH)
    ]
    num_batches = len(batches)
    print(f"  Processing in {num_batches} batch(es) of up to {MAX_SPECS_PER_BATCH} spec files each")

    # ── Branch: Label vs EDI use different prompts and merge strategies ──
    if stype == "edi":
        all_edi_batches: List[Dict] = []
        for batch_idx, batch in enumerate(batches, start=1):
            batch_context = _build_spec_context(batch, reviewed_only=False)
            if not batch_context:
                continue
            print(f"  Batch {batch_idx}/{num_batches}: {len(batch)} spec file(s), {len(batch_context):,} chars")
            edi_data = _call_claude_for_edi_rules(code, batch_context)
            if edi_data:
                all_edi_batches.append(edi_data)
            else:
                print(f"  Batch {batch_idx}/{num_batches}: no EDI rules returned — skipping")

        if not all_edi_batches:
            return {
                "success": False,
                "carrier_code": code,
                "message": "Claude did not generate any EDI rules. Check spec file content.",
                "rules_generated": 0,
            }

        merged_edi = _merge_edi_rules(all_edi_batches)
        formatted_rules = _rules_to_edi_format(merged_edi)
        # For display/save: flatten field_rules + segment info
        rules = merged_edi.get("field_rules", [])
        rules_count = len(merged_edi.get("required_segments", [])) + len(rules)
        required_names = merged_edi.get("required_fields", [])
        optional_names = [r.get("field", "") for r in rules if not r.get("required")]

        print(f"  EDI: {len(merged_edi.get('required_segments', []))} segments, {len(rules)} field rules")

    else:
        all_raw_rule_batches: List[List[Dict]] = []
        for batch_idx, batch in enumerate(batches, start=1):
            batch_context = _build_spec_context(batch, reviewed_only=False)
            if not batch_context:
                continue
            print(f"  Batch {batch_idx}/{num_batches}: {len(batch)} spec file(s), {len(batch_context):,} chars")
            batch_rules = _call_claude_for_rules(code, batch_context)
            if batch_rules:
                all_raw_rule_batches.append(batch_rules)
            else:
                print(f"  Batch {batch_idx}/{num_batches}: no rules returned — skipping")

        raw_rules = _merge_rules(all_raw_rule_batches)

        if not raw_rules:
            return {
                "success": False,
                "carrier_code": code,
                "message": "Claude did not generate any rules. Check spec file content.",
                "rules_generated": 0,
            }

        # Validate and clean label rules
        rules = _validate_and_clean_rules(raw_rules)
        formatted_rules = _rules_to_label_format(rules)
        rules_count = len(rules)
        required_names = [r["field"] for r in rules if r["required"]]
        optional_names = [r["field"] for r in rules if not r["required"]]

        print(f"  Validated: {len(rules)} label rule(s)")
        for r in rules:
            status = "REQUIRED" if r["required"] else "optional"
            detect = r.get("detect_by", "?")
            print(f"    {r['field']} [{status}] detect_by={detect}")

    # ── Save rules.json ──
    rules_output = {
        "carrier_code": code,
        "spec_type": stype,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "spec_files_used": files_used,
        "reviewed_only": using_reviewed_only,
        "rules": rules,
        "formatted_rules": formatted_rules,
    }
    rules_json_path = rules_dir / "rules.json"
    rules_json_path.write_text(
        json.dumps(rules_output, indent=2, ensure_ascii=False, default=str),
        encoding="utf-8",
    )
    print(f"\n  Saved: {rules_json_path}")

    # ── Save to MongoDB (if db provided) ──
    mongo_saved = False
    mongo_version = None

    if db is not None:
        try:
            rules_field = "label_rules" if stype == "label" else "edi_rules"
            other_field = "edi_rules" if stype == "label" else "label_rules"

            existing = await db.carriers.find_one({"carrier": code})
            new_version = 1
            # Preserve the other type's rules from the previous active version
            prev_other_rules = {}
            if existing and "rules" in existing:
                new_version = len(existing["rules"]) + 1
                prev_active = next(
                    (r for r in existing["rules"] if r.get("status") == "active"),
                    None,
                )
                if prev_active:
                    prev_other_rules = prev_active.get(other_field, {})

            rule_entry = {
                "version": new_version,
                "created_at": datetime.now(timezone.utc),
                rules_field: formatted_rules,
                other_field: prev_other_rules,
                "ai_extracted_rules": rules,
                "status": "active",
                "source": "v3_spec_files",
                "spec_type": stype,
                "spec_files_reviewed": reviewed_files,
            }

            if existing and "rules" in existing:
                await db.carriers.update_one(
                    {"carrier": code},
                    {"$set": {"rules.$[].status": "inactive"}},
                )
                await db.carriers.update_one(
                    {"carrier": code},
                    {"$push": {"rules": rule_entry}},
                )
            else:
                await db.carriers.update_one(
                    {"carrier": code},
                    {
                        "$set": {"carrier": code},
                        "$push": {"rules": rule_entry},
                    },
                    upsert=True,
                )

            mongo_saved = True
            mongo_version = new_version
            print(f"  Saved to MongoDB: carrier='{code}', version={new_version}")

            await db.carrier_specs.update_one(
                {"carrier_code": code},
                {
                    "$set": {
                        f"{stype}_rules_generated": True,
                        f"{stype}_rules_version": new_version,
                        f"{stype}_rules_generated_at": datetime.now(timezone.utc),
                        f"{stype}_rules_count": rules_count,
                    }
                },
                upsert=True,
            )

        except Exception as e:
            print(f"  [Phase 3] MongoDB save error: {e}")

    print(f"\n[Phase 3] Complete — {rules_count} rules generated for {stype}")

    return {
        "success": True,
        "carrier_code": code,
        "spec_type": stype,
        "rules_generated": rules_count,
        "required_fields": required_names,
        "optional_fields": optional_names,
        "spec_files_used": files_used,
        "reviewed_only": using_reviewed_only,
        "rules_json_path": str(rules_json_path),
        "mongo_saved": mongo_saved,
        "mongo_version": mongo_version,
        "rules": rules,
    }
