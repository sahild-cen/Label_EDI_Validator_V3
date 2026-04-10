# Field: check_digit

## Display Name
Check Digit (Modified MOD 10)

## Field Description
A mathematically derived check digit that appears at the end of the UPS Tracking Number. It is calculated using the Modified MOD 10 algorithm and is used for performing a mathematical check on the validity of the encoded data.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 1 character
- **Pattern/Regex:** Calculated via Modified MOD 10 algorithm
- **Allowed Values:** 0-9
- **Required:** yes

## Examples from Spec
No examples in spec.

## Position on Label
Last position of the Tracking Number, both in barcode and human-readable interpretation.

## Edge Cases & Notes
- The Modified MOD 10 algorithm is specific to UPS; it differs from standard MOD 10.

## Claude Confidence
MEDIUM — Clearly referenced in glossary but algorithm details not provided in this extract.

## Review Status
- [ ] Reviewed by human