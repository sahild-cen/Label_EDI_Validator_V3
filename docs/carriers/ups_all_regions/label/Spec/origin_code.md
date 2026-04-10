# Field: origin_code

## Display Name
Origin Code

## Field Description
The airport/facility code for the origin location, used on Air Freight labels.

## Format & Validation Rules
- **Data Type:** string
- **Length:** 3 characters
- **Pattern/Regex:** `[A-Z]{3}`
- **Allowed Values:** Valid airport/facility codes
- **Required:** conditional — required for Air Freight labels

## Examples from Spec
- `ORIGIN: ATL`

## Position on Label
Near the top of the Air Freight label, in the header area.

## Edge Cases & Notes
Only shown on Air Freight label formats (e.g., UPS Air Freight Direct).

## Claude Confidence
HIGH — Clearly shown on the Air Freight label example.

## Review Status
- [ ] Reviewed by human