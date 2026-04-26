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
from typing import Dict, List, Optional, Any
from datetime import datetime, timezone

from app.services.pdf_extractor import DOCS_BASE
from app.services.claude_service import client, deployment_name, extract_json_from_text


RULE_GENERATION_PROMPT = """\
You are an expert in ZPL (Zebra Programming Language) shipping label validation and logistics carrier specifications.

Carrier: {carrier_code}

Below are human-reviewed specification files for each field on this carrier's shipping labels.
Your job is to convert them into precise JSON validation rules.

═══ SUBFIELD EXPANSION (READ CAREFULLY) ═══

If a spec file contains a "## Subfields" section, generate ONE SEPARATE RULE per subfield.
Name each rule as: {{parent_field_name}}_{{subfield_name}}
Example: ship_from_address has subfields name, postal_code → generate ship_from_address_name and ship_from_address_postal_code as separate rules.

For each rule (whether from a flat field or an expanded subfield), provide:

1. field: snake_case field name
2. required: true or false
3. detect_by: HOW the ZPL parser finds this field (see instructions below)
4. regex: validation pattern (from Pattern/Regex section)
5. description: 1-sentence description
6. zpl_position: approximate X,Y position (e.g. "50,100" or "" if unknown)
7. zpl_font: ZPL font command (e.g. "^A0N,30,30" or "" if unknown)
8. field_prefix: literal text prefix before the data (e.g. "DATE:"). Empty for barcodes/no prefix.

═══ DETECT_BY INSTRUCTIONS ═══

  zpl_command:^BD         For fields identified by a ZPL command (MaxiCode=^BD, PDF417=^B7)
  barcode_data:^1Z        For barcodes whose DATA matches a regex prefix
  text_prefix:DATE:       For text that STARTS WITH a known literal prefix
  text_contains:phrase    For text that CONTAINS a phrase
  text_pattern:regex      For text matching a REGEX PATTERN
  text_exact:A|B|C        For text that EQUALS one of a set of values
  graphic:GFA             For graphic/image elements
  spatial:ship_from       For the shipper address block
  spatial:ship_to         For the consignee/recipient address block

For subfields of an address block, inherit the parent's spatial detect_by.
Always provide a detect_by — never leave it empty.

═══ REGEX RULES ═══

- Only include regex if the spec specifies a clear pattern
- If no clear pattern, set regex to ""

═══ REQUIRED FIELD ═══

- required: true if spec says "required", "mandatory", "must appear"
- required: false if "optional", "conditional", "when applicable"

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
      "description": "UPS tracking barcode in 1Z format",
      "zpl_position": "50,800",
      "zpl_font": "",
      "field_prefix": ""
    }},
    {{
      "field": "ship_from_address_name",
      "required": true,
      "detect_by": "spatial:ship_from",
      "regex": ".{{1,35}}",
      "description": "Shipper name in ship-from address block",
      "zpl_position": "",
      "zpl_font": "",
      "field_prefix": ""
    }},
    {{
      "field": "ship_from_address_postal_code",
      "required": true,
      "detect_by": "spatial:ship_from",
      "regex": "\\\\d{{5}}(-\\\\d{{4}})?",
      "description": "ZIP code in ship-from address block",
      "zpl_position": "",
      "zpl_font": "",
      "field_prefix": ""
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
Each spec file represents ONE segment with its sub-elements listed under "## Subfields".
Your job is to convert them into precise JSON validation rules.

═══ CRITICAL: SUBFIELDS STRUCTURE ═══

Each segment in field_rules MUST include a "subfields" dict containing its required elements.
- The key is the subfield name (snake_case)
- element_position: 1-indexed position after the segment tag
  Example: BGM+610+73400858+9 → element 1="610", element 2="73400858", element 3="9"
- pattern: regex that the element value must match (empty string if no constraint)
- required: true/false

═══ OUTPUT FORMAT ═══

Return ONLY valid JSON:
{{
  "carrier_code": "{carrier_code}",
  "format_type": "edifact",
  "required_segments": ["UNB", "UNH", "BGM", "DTM", "NAD", "CNT", "UNT", "UNZ"],
  "segment_order": ["UNB", "UNH", "BGM", "DTM", "NAD", "CNT", "UNT", "UNZ"],
  "required_fields": ["BGM", "DTM", "NAD"],
  "delimiter_rules": {{
    "segment_delimiter": "'",
    "element_delimiter": "+",
    "sub_element_delimiter": ":"
  }},
  "field_rules": [
    {{
      "field": "BGM",
      "segment": "BGM",
      "required": true,
      "description": "Begin Message — identifies shipment notice type",
      "subfields": {{
        "document_name_code": {{
          "element_position": 1,
          "pattern": "610",
          "required": true,
          "description": "Document name code — 610 = Despatch advice"
        }},
        "document_identifier": {{
          "element_position": 2,
          "pattern": "\\\\d{{1,35}}",
          "required": true,
          "description": "Unique shipment document identifier"
        }},
        "message_function_code": {{
          "element_position": 3,
          "pattern": "9",
          "required": true,
          "description": "Message function — 9 = original"
        }}
      }}
    }},
    {{
      "field": "DTM",
      "segment": "DTM",
      "required": true,
      "description": "Date/Time/Period — shipment date",
      "subfields": {{
        "date_time_qualifier": {{
          "element_position": 1,
          "pattern": "137",
          "required": true,
          "description": "Qualifier 137 = document date/time"
        }},
        "date_value": {{
          "element_position": 2,
          "pattern": "\\\\d{{8}}",
          "required": true,
          "description": "Date in YYYYMMDD format"
        }}
      }}
    }}
  ]
}}

═══ RULES ═══

- required_segments: ALL segments the spec says are mandatory
- segment_order: sequence segments appear per spec
- required_fields: list of segment IDs (field names) that are required — matches keys in field_rules
- delimiter_rules: actual delimiters (' for EDIFACT, ~ for X12)
- field_rules: one entry per segment; each entry MUST have a "subfields" dict
- pattern must be a valid regex; use empty string "" if no format constraint
- Set required: true only for mandatory elements

═══ SPEC FILES ═══

{spec_files_content}
"""


# Max spec files per Claude call — EDI is lower because nested subfields
# produce ~3× more JSON output than flat label rules
MAX_SPECS_PER_BATCH = 20
MAX_EDI_SPECS_PER_BATCH = 8


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
            max_tokens=16384,
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
    Preserves subfields dict when present (new hierarchical format).
    """
    field_formats = {}
    for r in edi_data.get("field_rules", []):
        field = r.get("field", "")
        if not field:
            continue

        entry: Dict = {
            "segment": r.get("segment", field),
            "required": r.get("required", False),
            "description": r.get("description", ""),
        }

        subfields = r.get("subfields", {})
        if subfields:
            entry["subfields"] = subfields
        else:
            # Old flat format: single element_position + pattern
            entry["position"] = r.get("position", 0)
            entry["element_position"] = r.get("position", 0)
            entry["pattern"] = r.get("regex", "") or r.get("pattern", "")

        field_formats[field] = entry

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


def _clean_single_rule(field: str, rule: Dict) -> Optional[Dict]:
    """Normalize and validate a single flat rule dict. Returns None if invalid."""
    field = re.sub(r"[^\w]", "_", field.lower()).strip("_")
    field = re.sub(r"_+", "_", field)
    if not field:
        return None

    regex = rule.get("regex", "")
    if regex:
        try:
            re.compile(regex)
            quants = re.findall(r"\{(\d+),(\d+)\}", regex)
            for min_v, max_v in quants:
                if int(min_v) > int(max_v):
                    regex = ""
                    break
        except re.error:
            regex = ""

    detect_by = rule.get("detect_by", "")
    if detect_by and ":" not in detect_by:
        detect_by = f"text_contains:{detect_by}"

    return {
        "field": field,
        "required": bool(rule.get("required", False)),
        "detect_by": detect_by,
        "regex": regex,
        "description": rule.get("description", ""),
        "zpl_position": rule.get("zpl_position", ""),
        "zpl_font": rule.get("zpl_font", ""),
        "field_prefix": rule.get("field_prefix", ""),
    }


def _validate_and_clean_rules(rules: List[Dict]) -> List[Dict]:
    """
    Normalize and validate label rules.
    Rules with 'subfields' are expanded into separate flat rules named {parent}_{subfield}.
    """
    cleaned = []
    for rule in rules:
        parent_field = rule.get("field", "").strip()
        if not parent_field:
            continue

        subfields = rule.get("subfields", {})

        if subfields:
            # Expand each subfield into its own flat rule
            parent_norm = re.sub(r"[^\w]", "_", parent_field.lower()).strip("_")
            parent_norm = re.sub(r"_+", "_", parent_norm)
            parent_detect_by = rule.get("detect_by", "")

            for sub_name, sub_rule in subfields.items():
                flat_name = f"{parent_norm}_{sub_name}"
                merged = {
                    "regex": sub_rule.get("pattern", sub_rule.get("regex", "")),
                    "required": sub_rule.get("required", False),
                    "detect_by": sub_rule.get("detect_by", parent_detect_by),
                    "description": sub_rule.get("description", ""),
                    "zpl_position": sub_rule.get("zpl_position", rule.get("zpl_position", "")),
                    "zpl_font": sub_rule.get("zpl_font", rule.get("zpl_font", "")),
                    "field_prefix": sub_rule.get("field_prefix", ""),
                }
                cleaned_rule = _clean_single_rule(flat_name, merged)
                if cleaned_rule:
                    cleaned.append(cleaned_rule)
        else:
            cleaned_rule = _clean_single_rule(parent_field, rule)
            if cleaned_rule:
                cleaned.append(cleaned_rule)

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
    # EDI uses a smaller batch size because nested subfields produce ~3× more output
    batch_size = MAX_EDI_SPECS_PER_BATCH if stype == "edi" else MAX_SPECS_PER_BATCH
    batches = [
        files_to_use[i : i + batch_size]
        for i in range(0, files_used, batch_size)
    ]
    num_batches = len(batches)
    print(f"  Processing in {num_batches} batch(es) of up to {batch_size} spec files each")

    # ── Branch: Label vs EDI use different prompts and merge strategies ──
    if stype == "edi":
        all_edi_batches: List[Dict] = []

        def _process_edi_batch(batch_files: List[Dict], label: str) -> None:
            """Call Claude for a batch; on failure split in half and retry each half."""
            if not batch_files:
                return
            batch_context = _build_spec_context(batch_files, reviewed_only=False)
            if not batch_context:
                return
            print(f"  {label}: {len(batch_files)} spec file(s), {len(batch_context):,} chars")
            edi_data = _call_claude_for_edi_rules(code, batch_context)
            if edi_data:
                all_edi_batches.append(edi_data)
            elif len(batch_files) > 1:
                # Split at whole-file boundary and retry each half
                mid = len(batch_files) // 2
                print(f"  {label}: failed — retrying as two halves ({mid} + {len(batch_files)-mid} files)")
                _process_edi_batch(batch_files[:mid], f"{label}a")
                _process_edi_batch(batch_files[mid:], f"{label}b")
            else:
                print(f"  {label}: single-file batch failed — skipping '{batch_files[0]['filename']}'")

        for batch_idx, batch in enumerate(batches, start=1):
            _process_edi_batch(batch, f"Batch {batch_idx}/{num_batches}")

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
    # Always writes label_rules before edi_rules in the document.
    # Overwrites only the spec type being generated; preserves the other.
    # Removes legacy versioned "rules" array if present.
    mongo_saved = False
    mongo_version = None

    if db is not None:
        try:
            rules_field = "label_rules" if stype == "label" else "edi_rules"

            existing = await db.carriers.find_one({"carrier": code}) or {}
            existing.pop("_id", None)
            existing.pop("rules", None)  # remove old versioned array

            now = datetime.now(timezone.utc)
            replacement = {"carrier": code}

            # label_rules always first
            replacement["label_rules"] = formatted_rules if stype == "label" else existing.get("label_rules", {})
            replacement["label_rules_updated_at"] = now if stype == "label" else existing.get("label_rules_updated_at")

            # edi_rules always second
            replacement["edi_rules"] = formatted_rules if stype == "edi" else existing.get("edi_rules", {})
            replacement["edi_rules_updated_at"] = now if stype == "edi" else existing.get("edi_rules_updated_at")

            # preserve other fields (spec paths, position mappings, etc.)
            _skip = {"carrier", "label_rules", "label_rules_updated_at", "edi_rules", "edi_rules_updated_at", "rules"}
            for k, v in existing.items():
                if k not in _skip:
                    replacement[k] = v

            await db.carriers.replace_one(
                {"carrier": code},
                replacement,
                upsert=True,
            )

            mongo_saved = True
            mongo_version = None
            print(f"  Saved to MongoDB: carrier='{code}', field='{rules_field}'")

            await db.carrier_specs.update_one(
                {"carrier_code": code},
                {
                    "$set": {
                        f"{stype}_rules_generated": True,
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
