from typing import Dict, Any
from datetime import datetime
from app.database import get_database
from app.utils.pdf_extractor import (
    extract_structured_pdf_data,
    generate_rule_template_from_spec
)


class SpecEngine:
    def __init__(self):
        self.db = get_database()

    # ----------------------------------------
    # PROCESS SPEC UPLOAD (VERSIONED SAVE)
    # ----------------------------------------
    async def process_spec_upload(
        self,
        carrier_name: str,
        label_spec_path: str = None,
        edi_spec_path: str = None
    ) -> Dict[str, Any]:

        label_rules = {}
        edi_rules = {}
        ai_extracted_rules = []

        # ──────── LABEL SPEC ────────
        if label_spec_path:
            # Path A: Structured extraction (regex-based)
            spec_data = extract_structured_pdf_data(label_spec_path)
            label_rules, structured_conf = generate_rule_template_from_spec(
                spec_data, spec_type="label"
            )
            final_confidence = structured_conf

            # Path B: AI extraction (Two-Pass Claude pipeline)
            try:
                from app.services.rule_extractor import extract_rules_from_pdf

                # Pass carrier_name so Pass 2 has context
                ai_rules = extract_rules_from_pdf(label_spec_path, carrier_name=carrier_name)

                if ai_rules:
                    ai_extracted_rules = ai_rules

                    # Merge AI-validated rules into field_formats
                    for rule in ai_rules:
                        field = rule.get("field", "")
                        if not field:
                            continue

                        # Add to field_formats (AI rules are already validated by Pass 2)
                        if "field_formats" not in label_rules:
                            label_rules["field_formats"] = {}

                        if field not in label_rules["field_formats"]:
                            label_rules["field_formats"][field] = {
                                "pattern": rule.get("regex", ""),
                                "required": rule.get("required", False),
                                "detect_by": rule.get("detect_by", ""),
                                "description": rule.get("description", "")
                            }
                        else:
                            # Merge: prefer AI regex if structured didn't find one
                            existing = label_rules["field_formats"][field]
                            if not existing.get("pattern") and rule.get("regex"):
                                existing["pattern"] = rule["regex"]
                            if rule.get("description") and not existing.get("description"):
                                existing["description"] = rule["description"]
                            if rule.get("detect_by") and not existing.get("detect_by"):
                                existing["detect_by"] = rule["detect_by"]

                        if rule.get("required") and field:
                            if field not in label_rules.get("required_fields", []):
                                label_rules.setdefault("required_fields", []).append(field)

                    # Boost confidence based on AI validated rules
                    if len(ai_rules) >= 3:
                        final_confidence = min(
                            0.5 * structured_conf + 0.5 * min(len(ai_rules) / 10, 1.0),
                            1.0
                        )

                    print("AI extracted and validated {} rules for {}".format(
                        len(ai_rules), carrier_name
                    ))

            except Exception as e:
                print("AI extraction failed (continuing with structured): {}".format(e))

            # Path C: ML fallback if confidence still low
            if final_confidence < 0.6:
                try:
                    from app.services.ml_fallback.layout_engine import run_layout_fallback
                    ml_rules, ml_conf, _ = run_layout_fallback(
                        spec_data.get("image_bytes")
                    )
                    if isinstance(ml_rules, dict):
                        label_rules.update(ml_rules)
                    final_confidence = 0.6 * final_confidence + 0.4 * ml_conf
                except Exception as e:
                    print("ML fallback failed: {}".format(e))

            label_rules["confidence_score"] = round(final_confidence, 2)

        # ──────── EDI SPEC ────────
        if edi_spec_path:
            spec_data = extract_structured_pdf_data(edi_spec_path)
            edi_rules, edi_conf = generate_rule_template_from_spec(
                spec_data, spec_type="edi"
            )

            try:
                from app.services.rule_extractor import extract_rules_from_pdf
                edi_ai_rules = extract_rules_from_pdf(edi_spec_path, carrier_name=carrier_name)
                if edi_ai_rules:
                    for rule in edi_ai_rules:
                        field = rule.get("field", "")
                        if field and rule.get("regex"):
                            edi_rules.setdefault("field_formats", {})[field] = {
                                "pattern": rule.get("regex", ""),
                                "required": rule.get("required", False),
                                "description": rule.get("description", "")
                            }
                    edi_conf = min(
                        0.5 * edi_conf + 0.5 * min(len(edi_ai_rules) / 8, 1.0), 1.0
                    )
            except Exception as e:
                print("EDI AI extraction failed: {}".format(e))

            edi_rules["confidence_score"] = round(edi_conf, 2)

        # ──────── SAVE TO MONGO ────────
        # Always writes label_rules before edi_rules in the document.
        # Overwrites only the spec type that was uploaded; preserves the other.
        # Removes legacy versioned "rules" array if present.
        existing = await self.db.carriers.find_one({"carrier": carrier_name}) or {}
        existing.pop("_id", None)
        existing.pop("rules", None)  # remove old versioned array

        now = datetime.utcnow()
        replacement = {"carrier": carrier_name}

        # label_rules always first
        replacement["label_rules"] = label_rules if label_spec_path else existing.get("label_rules", {})
        replacement["label_rules_updated_at"] = now if label_spec_path else existing.get("label_rules_updated_at")

        # edi_rules always second
        replacement["edi_rules"] = edi_rules if edi_spec_path else existing.get("edi_rules", {})
        replacement["edi_rules_updated_at"] = now if edi_spec_path else existing.get("edi_rules_updated_at")

        # preserve any other fields (spec paths, position mappings, etc.)
        _skip = {"carrier", "label_rules", "label_rules_updated_at", "edi_rules", "edi_rules_updated_at", "rules"}
        for k, v in existing.items():
            if k not in _skip:
                replacement[k] = v

        await self.db.carriers.replace_one(
            {"carrier": carrier_name},
            replacement,
            upsert=True,
        )

        return {
            "carrier_name": carrier_name,
            "label_rules": label_rules,
            "edi_rules": edi_rules,
            "ai_rules_count": len(ai_extracted_rules)
        }

    # ----------------------------------------
    # GET ACTIVE RULE VERSION
    # ----------------------------------------
    async def get_carrier_rules(self, carrier_name: str) -> Dict[str, Any]:
        carrier = await self.db.carriers.find_one({"carrier": carrier_name})

        if not carrier:
            return {"label_rules": {}, "edi_rules": {}}

        return {
            "label_rules": carrier.get("label_rules", {}),
            "edi_rules": carrier.get("edi_rules", {}),
        }

    # ----------------------------------------
    # ROLLBACK
    # ----------------------------------------
    async def rollback_to_version(self, carrier_name: str, version: int) -> Dict[str, Any]:
        # Versioning has been removed. Rules are regenerated from spec files.
        return {
            "success": False,
            "message": "Rule versioning is no longer supported. Regenerate rules from spec files."
        }

    # ----------------------------------------
    # LIST VERSIONS (stub — versioning removed)
    # ----------------------------------------
    async def list_versions(self, carrier_name: str) -> Dict[str, Any]:
        return {"carrier": carrier_name, "versions": [], "message": "Versioning removed. Rules are always overwritten on regeneration."}

    # ----------------------------------------
    # COMPARE VERSIONS (stub — versioning removed)
    # ----------------------------------------
    async def compare_versions(self, carrier_name: str, v1: int, v2: int) -> Dict[str, Any]:
        return {"error": "Versioning removed. Rules are always overwritten on regeneration."}

    # ----------------------------------------
    # SIMULATE VALIDATION (stub — versioning removed)
    # ----------------------------------------
    async def simulate_validation(
        self, carrier_name: str, version_1: int, version_2: int, label_path: str
    ) -> Dict[str, Any]:
        return {"error": "Versioning removed. Rules are always overwritten on regeneration."}