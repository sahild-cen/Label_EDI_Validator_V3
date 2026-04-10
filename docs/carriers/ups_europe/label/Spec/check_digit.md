# Field: check_digit

## Display Name
Check Digit (Modified MOD 10)

## Field Description
A calculated character included at the end of the UPS Tracking Number whose value is used for performing a mathematical check on the validity of the encoded data. Uses the Modified MOD 10 algorithm.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 1 digit (last position of tracking number)
- **Pattern/Regex:** `[0-9]`
- **Allowed Values:** 0-9, calculated via Modified MOD 10 algorithm
- **Required:** yes

## Examples from Spec
No examples in spec.

## Position on Label
Last character of the tracking number (both in barcode and human-readable representation).

## ZPL Rendering
- **Typical Position:** Encoded as the final character of the tracking number barcode and human-readable text
- **Font / Size:** Not separately rendered — part of tracking number
- **Field Prefix:** None — integral part of tracking number
- **ZPL Command:** Part of tracking number ^BC barcode and ^FD text

## Edge Cases & Notes
- Modified MOD 10 is the specific algorithm used — this is different from standard MOD 10.
- Invalid check digits will cause the barcode to fail validation during scanning.

## Claude Confidence
HIGH — Clearly defined in glossary with specific algorithm name and position within tracking number.

## Review Status
- [ ] Reviewed by human