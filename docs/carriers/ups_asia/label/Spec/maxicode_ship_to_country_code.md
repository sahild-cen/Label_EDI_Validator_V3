# Field: maxicode_ship_to_country_code

## Display Name
Ship To ISO Country Code (MaxiCode)

## Field Description
The 3-digit ISO numeric country code for the destination country, encoded in the MaxiCode data string.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 3 (exact)
- **Pattern/Regex:** `\d{3}`
- **Allowed Values:** ISO country codes (referenced in Appendix E of the full spec)
- **Required:** yes

## Examples from Spec
- `840` (United States)
- `276` (Germany)

## Position on Label
Encoded within the MaxiCode barcode (primary message, second data field).

## Edge Cases & Notes
- ISO country codes are listed in Appendix E of the full specification.

## Claude Confidence
HIGH — spec clearly defines as 3-digit numeric ISO country code with examples.

## Review Status
- [ ] Reviewed by human