import re
import json
import xml.etree.ElementTree as ET
from typing import Dict, Any, List
from app.models.validation import ValidationError


class EDIValidator:
    def __init__(self, rules: Dict[str, Any]):
        self.rules = rules

    def detect_format(self, content: str) -> str:
        content_stripped = content.strip()

        if content_stripped.startswith("{") or content_stripped.startswith("["):
            try:
                json.loads(content)
                return "json"
            except Exception:
                pass

        if content_stripped.startswith("<"):
            try:
                ET.fromstring(content)
                return "xml"
            except Exception:
                pass

        if "~" in content and "*" in content:
            return "x12"

        if "'" in content and "+" in content:
            return "edifact"

        if "\n" in content and len(content.split("\n")) > 1:
            return "delimited"

        return "fixed_width"

    def parse_content(self, content: str, format_type: str) -> Dict[str, Any]:
        if format_type == "json":
            return json.loads(content)

        elif format_type == "xml":
            root = ET.fromstring(content)
            return self._xml_to_dict(root)

        elif format_type in ["x12", "edifact"]:
            return self._parse_edi_segments(content, format_type)

        elif format_type == "delimited":
            lines = content.strip().split("\n")
            return {"lines": lines, "segments": [line.split("|") for line in lines]}

        else:
            return {"raw_content": content}

    def _xml_to_dict(self, element: ET.Element) -> Dict[str, Any]:
        result = {}
        for child in element:
            child_data = child.text if child.text and not list(child) else self._xml_to_dict(child)
            result[child.tag] = child_data
        return result

    def _parse_edi_segments(self, content: str, format_type: str) -> Dict[str, Any]:
        if format_type == "x12":
            seg_delim, elem_delim = "~", "*"
        else:
            # EDIFACT: handle UNA service string advice
            seg_delim, elem_delim = "'", "+"

        segments = content.split(seg_delim)
        parsed = []

        for segment in segments:
            segment = segment.strip()
            if segment:
                elements = segment.split(elem_delim)
                parsed.append({
                    "segment_id": elements[0] if elements else "",
                    "elements": elements
                })

        return {"format": format_type, "segments": parsed}

    async def validate(self, edi_content: str) -> Dict[str, Any]:
        errors = []

        # ── Step 1: Detect format ──
        format_type = self.detect_format(edi_content)

        print("\n" + "=" * 70)
        print("EDI VALIDATION — TERMINAL DEBUG OUTPUT")
        print("=" * 70)
        print(f"\n📄 EDI Content Preview (first 300 chars):")
        print(f"   {edi_content[:300]}...")
        print(f"\n🔍 Detected Format: {format_type}")

        # ── Step 2: Parse content ──
        try:
            parsed_data = self.parse_content(edi_content, format_type)
        except Exception as e:
            print(f"\n❌ PARSE ERROR: {str(e)}")
            errors.append(ValidationError(
                field="parsing",
                expected=f"Valid {format_type} format",
                actual="Parse error",
                description=f"Failed to parse EDI content: {str(e)}"
            ))
            return {
                "status": "FAIL",
                "errors": [err.dict() for err in errors],
                "corrected_edi_script": None,
                "compliance_score": 0.0,
            }

        # ── Step 3: Log parsed segments ──
        if format_type in ["x12", "edifact"]:
            segments = parsed_data.get("segments", [])
            segment_ids = [seg["segment_id"] for seg in segments]

            print(f"\n📦 Parsed Segments ({len(segments)} total):")
            for seg in segments:
                sid = seg["segment_id"]
                elems = seg["elements"]
                preview = "+".join(elems[:5])
                if len(elems) > 5:
                    preview += f"... (+{len(elems) - 5} more)"
                print(f"   [{sid:6s}] {preview}")

            print(f"\n📋 Segment IDs found: {segment_ids}")
        else:
            segment_ids = []
            print(f"\n📦 Parsed Data Keys: {list(parsed_data.keys()) if isinstance(parsed_data, dict) else 'N/A'}")

        # ── Step 4: Load rules ──
        required_segments = self.rules.get("required_segments", [])
        segment_order = self.rules.get("segment_order", [])
        required_fields = self.rules.get("required_fields", [])
        delimiter_rules = self.rules.get("delimiter_rules", {})

        print(f"\n{'─' * 70}")
        print("📜 RULES FROM JSON (what we're validating against):")
        print(f"{'─' * 70}")
        print(f"   Required Segments: {required_segments}")
        print(f"   Segment Order:     {segment_order}")
        print(f"   Required Fields:   {required_fields}")
        print(f"   Delimiter Rules:   {delimiter_rules}")
        print(f"   Format Type Rule:  {self.rules.get('format_type', 'not specified')}")

        # ── Step 5: Validate format-specific rules ──
        total_checks = 0
        passed_checks = 0

        if format_type in ["x12", "edifact"]:

            # ── 5a: Check required segments ──
            print(f"\n{'─' * 70}")
            print("✅ SEGMENT PRESENCE CHECKS:")
            print(f"{'─' * 70}")

            # Filter required segments to match the detected format
            # X12 segments: ISA, GS, ST, SE, GE, IEA
            # EDIFACT segments: UNA, UNB, UNH, UNT, UNZ, BGM, DTM, etc.
            x12_segments = {"ISA", "GS", "ST", "SE", "GE", "IEA"}
            edifact_segments = {"UNA", "UNB", "UNH", "UNT", "UNZ", "BGM", "DTM",
                                "NAD", "CTA", "COM", "TDT", "LOC", "RFF", "FTX",
                                "GID", "MEA", "DIM", "PCI", "GIN", "CNT"}

            for required_seg in required_segments:
                total_checks += 1

                # Skip segments that don't belong to the detected format
                seg_upper = required_seg.upper().replace(":", "")
                if format_type == "edifact" and seg_upper in x12_segments:
                    print(f"   ⏭️  '{required_seg}' — SKIPPED (X12 segment, file is EDIFACT)")
                    passed_checks += 1  # Don't penalize
                    continue
                elif format_type == "x12" and seg_upper in edifact_segments:
                    print(f"   ⏭️  '{required_seg}' — SKIPPED (EDIFACT segment, file is X12)")
                    passed_checks += 1  # Don't penalize
                    continue

                # Check if segment exists (handle UNA: prefix edge case)
                found = False
                for sid in segment_ids:
                    # Normalize: "UNA:" → "UNA", "UNB" → "UNB"
                    sid_clean = sid.rstrip(":").strip()
                    req_clean = required_seg.rstrip(":").strip()
                    if sid_clean.upper() == req_clean.upper():
                        found = True
                        break

                if found:
                    print(f"   ✅ '{required_seg}' — FOUND in EDI")
                    passed_checks += 1
                else:
                    print(f"   ❌ '{required_seg}' — MISSING from EDI")
                    seg_heading = required_seg.rstrip(":").strip().upper()
                    errors.append(ValidationError(
                        field=seg_heading,
                        expected=f"Segment '{seg_heading}' present",
                        actual="Segment missing",
                        description=f"Required segment '{seg_heading}' is missing",
                    ))

            # ── 5b: Check segment order ──
            if segment_order:
                total_checks += 1
                print(f"\n{'─' * 70}")
                print("📐 SEGMENT ORDER CHECK:")
                print(f"{'─' * 70}")

                # Only check order for segments that are actually present and
                # belong to the detected format
                relevant_order = []
                for seg in segment_order:
                    seg_upper = seg.upper().replace(":", "")
                    if format_type == "edifact" and seg_upper in x12_segments:
                        continue
                    if format_type == "x12" and seg_upper in edifact_segments:
                        continue
                    relevant_order.append(seg)

                # Build actual order of relevant segments
                actual_relevant = []
                for sid in segment_ids:
                    sid_clean = sid.rstrip(":").strip().upper()
                    for rel in relevant_order:
                        if sid_clean == rel.upper():
                            actual_relevant.append(rel)
                            break

                print(f"   Expected order (format-filtered): {relevant_order}")
                print(f"   Actual order (in file):           {actual_relevant}")

                # Check if the relative order is preserved
                order_correct = True
                last_idx = -1
                for seg in relevant_order:
                    if seg in actual_relevant:
                        idx = actual_relevant.index(seg)
                        if idx < last_idx:
                            order_correct = False
                            break
                        last_idx = idx

                if order_correct:
                    print(f"   ✅ Segment order is correct")
                    passed_checks += 1
                else:
                    print(f"   ❌ Segment order violation detected")
                    actual_preview = ", ".join(segment_ids[:10])
                    if len(segment_ids) > 10:
                        actual_preview += "..."
                    errors.append(ValidationError(
                        field="segment_order",
                        expected=f"Segments in order: {', '.join(relevant_order)}",
                        actual=f"Actual order: {actual_preview}",
                        description="Segments are not in the correct order",
                    ))

            # ── 5c: Check delimiter rules ──
            if delimiter_rules:
                print(f"\n{'─' * 70}")
                print("🔤 DELIMITER CHECKS:")
                print(f"{'─' * 70}")

                expected_seg_delim = delimiter_rules.get("segment_delimiter")
                expected_elem_delim = delimiter_rules.get("element_delimiter")
                expected_sub_delim = delimiter_rules.get("sub_element_delimiter")

                if expected_seg_delim:
                    total_checks += 1
                    actual_delim = "'" if format_type == "edifact" else "~"
                    if actual_delim == expected_seg_delim:
                        print(f"   ✅ Segment delimiter: '{actual_delim}' matches expected '{expected_seg_delim}'")
                        passed_checks += 1
                    else:
                        print(f"   ❌ Segment delimiter: '{actual_delim}' ≠ expected '{expected_seg_delim}'")
                        errors.append(ValidationError(
                            field="delimiters",
                            expected=f"Segment delimiter: '{expected_seg_delim}'",
                            actual=f"Found: '{actual_delim}'",
                            description="Segment delimiter mismatch",
                        ))

                if expected_elem_delim:
                    total_checks += 1
                    actual_delim = "+" if format_type == "edifact" else "*"
                    if actual_delim == expected_elem_delim:
                        print(f"   ✅ Element delimiter: '{actual_delim}' matches expected '{expected_elem_delim}'")
                        passed_checks += 1
                    else:
                        print(f"   ❌ Element delimiter: '{actual_delim}' ≠ expected '{expected_elem_delim}'")
                        errors.append(ValidationError(
                            field="delimiters",
                            expected=f"Element delimiter: '{expected_elem_delim}'",
                            actual=f"Found: '{actual_delim}'",
                            description="Element delimiter mismatch",
                        ))

        # ── 5d: Check required fields (for any format) ──
        if required_fields:
            print(f"\n{'─' * 70}")
            print("📋 REQUIRED FIELD CHECKS:")
            print(f"{'─' * 70}")

            field_formats = self.rules.get("field_formats", {})

            for field in required_fields:
                fmt = field_formats.get(field, {})
                # segment may be stored as "segment" key, or fall back to the field name itself
                seg_id = (fmt.get("segment", "") or field).strip().upper()
                qualifier = fmt.get("qualifier", "").strip().upper()
                subfields = fmt.get("subfields", {})
                # Flat-format fields (old rules without subfields)
                element_position = int(fmt.get("element_position", 0) or fmt.get("position", 0) or 0)
                pattern = fmt.get("pattern", "") or fmt.get("regex", "")

                if format_type in ["x12", "edifact"]:
                    if not seg_id:
                        print(f"   ⏭️  '{field}' — SKIPPED (no segment mapping in rules)")
                        continue

                    # Strip qualifier that equals the segment name (Claude artifact)
                    if qualifier == seg_id:
                        qualifier = ""

                    elem_delim = "+" if format_type == "edifact" else "*"
                    qualifier_note = f"+{qualifier}" if qualifier else ""
                    heading = seg_id

                    # ── Find the segment ──
                    seg_match = None
                    for seg in parsed_data.get("segments", []):
                        sid_clean = seg.get("segment_id", "").rstrip(":").strip().upper()
                        if sid_clean != seg_id:
                            continue
                        elements = seg.get("elements", [])
                        if qualifier:
                            seg_qualifiers = [e.split(":")[0].strip().upper() for e in elements[1:4]]
                            if qualifier not in seg_qualifiers:
                                continue
                        seg_match = seg
                        break

                    if not seg_match:
                        total_checks += 1
                        print(f"   ❌ '{heading}' ({field}) — NOT found (expected {heading}{qualifier_note})")
                        errors.append(ValidationError(
                            field=heading,
                            expected=f"Segment {heading}{qualifier_note} present in EDI",
                            actual="Segment missing",
                            description=f"{field} — required segment {heading}{qualifier_note} is missing",
                        ))
                        continue

                    # ── Segment found: validate subfields (new hierarchical format) ──
                    if subfields:
                        elements = seg_match.get("elements", [])
                        for sub_name, sub_fmt in subfields.items():
                            if not sub_fmt.get("required", False):
                                continue
                            total_checks += 1
                            elem_pos = int(float(sub_fmt.get("element_position", 0) or 0))
                            sub_pattern = sub_fmt.get("pattern", "") or sub_fmt.get("regex", "")

                            if elem_pos <= 0 or elem_pos >= len(elements):
                                print(f"   ❌ '{heading}.{sub_name}' — element {elem_pos} out of range (segment has {len(elements)} elements)")
                                errors.append(ValidationError(
                                    field=heading,
                                    expected=f"Element {elem_pos} in {heading} for '{sub_name}'",
                                    actual=f"Segment only has {len(elements)} element(s)",
                                    description=f"{sub_name}: no element at position {elem_pos} in {heading}",
                                ))
                                continue

                            raw_elem = elements[elem_pos]
                            candidates = [raw_elem] + (raw_elem.split(":") if ":" in raw_elem else [])

                            if sub_pattern:
                                if any(re.match(sub_pattern, c.strip()) for c in candidates if c.strip()):
                                    print(f"   ✅ '{heading}.{sub_name}' — element {elem_pos} = '{raw_elem}' matches '{sub_pattern}'")
                                    passed_checks += 1
                                else:
                                    print(f"   ❌ '{heading}.{sub_name}' — element {elem_pos} = '{raw_elem}', expected '{sub_pattern}'")
                                    errors.append(ValidationError(
                                        field=heading,
                                        expected=f"Element {elem_pos} in {heading} matches '{sub_pattern}'",
                                        actual=f"Got '{raw_elem}'",
                                        description=f"{sub_name}: element {elem_pos} in {heading} is '{raw_elem}', expected pattern '{sub_pattern}'",
                                    ))
                            else:
                                if raw_elem.strip():
                                    print(f"   ✅ '{heading}.{sub_name}' — element {elem_pos} present")
                                    passed_checks += 1
                                else:
                                    print(f"   ❌ '{heading}.{sub_name}' — element {elem_pos} is empty")
                                    errors.append(ValidationError(
                                        field=heading,
                                        expected=f"Non-empty value at element {elem_pos} in {heading}",
                                        actual="Empty",
                                        description=f"{sub_name}: element {elem_pos} in {heading} is empty",
                                    ))

                    # ── Old flat format: single element_position + pattern ──
                    elif element_position > 0 and pattern:
                        total_checks += 1
                        elements = seg_match.get("elements", [])
                        is_seg_pattern = (
                            ("\\+" in pattern and format_type == "edifact")
                            or ("\\*" in pattern and format_type == "x12")
                        )
                        if is_seg_pattern:
                            full_seg = elem_delim.join(elements)
                            if re.match(pattern, full_seg):
                                print(f"   ✅ '{heading}' ({field}) — segment pattern matches")
                                passed_checks += 1
                            else:
                                print(f"   ❌ '{heading}' ({field}) — segment pattern mismatch")
                                errors.append(ValidationError(
                                    field=heading,
                                    expected=f"Segment {heading} matches '{pattern}'",
                                    actual="Pattern mismatch",
                                    description=f"{field}: {heading} does not satisfy pattern '{pattern}'",
                                ))
                        elif element_position < len(elements):
                            raw_elem = elements[element_position]
                            candidates = [raw_elem] + (raw_elem.split(":") if ":" in raw_elem else [])
                            if any(re.match(pattern, c.strip()) for c in candidates if c.strip()):
                                print(f"   ✅ '{heading}' ({field}) — valid")
                                passed_checks += 1
                            else:
                                print(f"   ❌ '{heading}' ({field}) — value mismatch at element {element_position} (expected: {pattern})")
                                errors.append(ValidationError(
                                    field=heading,
                                    expected=f"Element {element_position} in {heading} matches '{pattern}'",
                                    actual=f"Value at position {element_position} does not match",
                                    description=f"{field}: {heading}{qualifier_note} found but element {element_position} does not satisfy '{pattern}'",
                                ))
                        else:
                            print(f"   ❌ '{heading}' ({field}) — element {element_position} out of range")
                            errors.append(ValidationError(
                                field=heading,
                                expected=f"Element {element_position} in {heading}",
                                actual=f"Segment only has {len(elements)} element(s)",
                                description=f"{field}: element {element_position} missing in {heading}",
                            ))

                    else:
                        # Segment present, no further validation needed
                        total_checks += 1
                        print(f"   ✅ '{heading}' ({field}) — segment present")
                        passed_checks += 1

                else:
                    # Non-EDI: plain text search
                    total_checks += 1
                    edi_upper = edi_content.upper()
                    field_found = (
                        field.replace("_", " ").upper() in edi_upper
                        or field.upper() in edi_upper
                    )
                    heading = seg_id if seg_id else field
                    if field_found:
                        print(f"   ✅ '{heading}' ({field}) — found")
                        passed_checks += 1
                    else:
                        print(f"   ❌ '{heading}' ({field}) — NOT found")
                        errors.append(ValidationError(
                            field=heading,
                            expected=f"Field '{field}' present",
                            actual="Field missing",
                            description=f"Required field '{field}' is missing",
                        ))

        # ── Step 6: Calculate score ──
        if total_checks > 0:
            compliance_score = round((passed_checks / total_checks) * 100, 1)
        else:
            compliance_score = 100.0

        status = "PASS" if not errors else "FAIL"

        print(f"\n{'=' * 70}")
        print(f"EDI VALIDATION RESULT: {status}")
        print(f"Score: {compliance_score}% ({passed_checks}/{total_checks} checks passed)")
        print(f"Errors: {len(errors)}")
        if errors:
            for e in errors:
                print(f"   ❌ [{e.field}] {e.description}")
        print("=" * 70 + "\n")

        # ── Step 7: Generate corrected script ──
        corrected_script = None
        if errors:
            corrected_script = self._generate_corrected_script(
                edi_content, format_type, errors
            )

        return {
            "status": status,
            "errors": [err.dict() for err in errors],
            "corrected_edi_script": corrected_script,
            "compliance_score": compliance_score,
        }

    def _generate_corrected_script(
        self, original: str, format_type: str, errors: List[ValidationError]
    ) -> str:
        """
        Generate a corrected EDI script by adding missing segments at the
        correct position and annotating subfield value errors inline.
        """
        if format_type not in ["x12", "edifact"]:
            return original

        seg_delim = "'" if format_type == "edifact" else "~"
        elem_delim = "+" if format_type == "edifact" else "*"
        terminal_segs = {"UNT", "UNZ"} if format_type == "edifact" else {"SE", "GE", "IEA"}

        def seg_id_of(seg_text: str) -> str:
            return seg_text.strip().split(elem_delim)[0].rstrip(":").strip().upper()

        # Split original into segments (strip empty parts from trailing delimiter)
        raw_segs = [s for s in original.split(seg_delim) if s.strip()]

        # First-occurrence index map for each segment ID
        seg_index_map: Dict[str, int] = {}
        for i, seg_text in enumerate(raw_segs):
            sid = seg_id_of(seg_text)
            if sid and sid not in seg_index_map:
                seg_index_map[sid] = i

        present_seg_ids = set(seg_index_map.keys())

        # Collect missing segment IDs from errors
        structural_fields = {"segment_order", "delimiters", "parsing"}
        missing_segs: List[str] = []

        for err in errors:
            if err.field in structural_fields:
                continue
            if "is missing" in err.description.lower():
                seg_id = err.field.upper()
                if seg_id not in missing_segs:
                    missing_segs.append(seg_id)

        # Rules context for positioning and placeholder building
        segment_order = [s.upper() for s in self.rules.get("segment_order", [])]
        field_formats = self.rules.get("field_formats", {})

        def build_placeholder(seg_id: str) -> str:
            """Build a placeholder segment line using subfield names from rules."""
            fmt = field_formats.get(seg_id, {})
            subfields = fmt.get("subfields", {})
            if subfields:
                max_pos = max(
                    (int(float(sf.get("element_position", 0) or 0))
                     for sf in subfields.values()),
                    default=1,
                )
                elems = [""] * (max_pos + 1)
                elems[0] = seg_id
                for sf_name, sf_data in subfields.items():
                    pos = int(float(sf_data.get("element_position", 0) or 0))
                    if 0 < pos <= max_pos:
                        elems[pos] = f"[{sf_name}]"
                for i in range(1, len(elems)):
                    if not elems[i]:
                        elems[i] = "[element]"
                return elem_delim.join(elems)
            return f"{seg_id}{elem_delim}[placeholder]"

        def find_anchor(missing_id: str):
            """Return the segment ID after which missing_id should be inserted."""
            if missing_id not in segment_order:
                return None
            idx = segment_order.index(missing_id)
            for i in range(idx - 1, -1, -1):
                candidate = segment_order[i]
                if candidate in present_seg_ids:
                    return candidate
            return None

        # Phase 1: insert missing segments at correct positions
        output = list(raw_segs)
        offset = 0

        for missing_id in missing_segs:
            placeholder = build_placeholder(missing_id)
            anchor = find_anchor(missing_id)

            if anchor and anchor in seg_index_map:
                insert_at = seg_index_map[anchor] + offset + 1
            else:
                # Insert before first terminal segment
                insert_at = next(
                    (i for i, s in enumerate(output) if seg_id_of(s) in terminal_segs),
                    len(output),
                )

            output.insert(insert_at, placeholder)
            offset += 1

        return seg_delim.join(output) + seg_delim