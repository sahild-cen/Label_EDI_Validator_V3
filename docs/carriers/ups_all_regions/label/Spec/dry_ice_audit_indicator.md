# Field: dry_ice_audit_indicator

## Display Name
Dry Ice Audit Indicator

## Field Description
A routing instruction line that prints below the Dry Ice declaration line, indicating whether UPS Operations needs to perform an acceptance audit of the package.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable (14-17 characters)
- **Pattern/Regex:** `^(AUDIT REQUIRED|NO AUDIT REQUIRED)$`
- **Allowed Values:** "AUDIT REQUIRED" or "NO AUDIT REQUIRED"
- **Required:** conditional — required when shipping dry ice

## Examples from Spec
- "AUDIT REQUIRED" (shown on both Dry Ice and Biological Substances label examples)

## Position on Label
Prints immediately below the Dry Ice declaration line in the Additional Routing Instructions block.

## Edge Cases & Notes
- Audit rules depend on shipment type: Non-medical domestic air under 49CFR with ≤5.5 lbs = no audit; under IATA regardless of weight = audit required. Non-medical international under IATA = audit. Medical domestic air under IATA = audit. Medical international under IATA = audit.
- Font Size = 10 pt.
- Please refer to the UPS Rate and Service Guide for detailed audit determination rules.

## Claude Confidence
HIGH — spec explicitly defines the two allowed values and conditions.

## Review Status
- [ ] Reviewed by human