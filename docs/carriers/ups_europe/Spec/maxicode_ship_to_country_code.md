# Field: maxicode_ship_to_country_code

## Display Name
Ship To ISO Country Code (MaxiCode)

## Field Description
The ISO 3166 numeric country code for the destination country, encoded in the MaxiCode primary message.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 3 (exactly)
- **Pattern/Regex:** `[0-9]{3}`
- **Allowed Values:** ISO 3166 numeric country codes (e.g., 840 = USA, 276 = Germany, 124 = Canada)
- **Required:** yes

## Examples from Spec
- `840` (United States)
- `276` (Germany)

## Position on Label
Encoded within MaxiCode barcode (primary message).

## Edge Cases & Notes
- Full list of ISO country codes is provided in Appendix E of the spec.
- Must be exactly 3 numeric digits.

## Claude Confidence
HIGH — spec clearly defines as numeric 3-digit ISO 3166 code with examples and reference table

## Review Status
- [x] Reviewed by human