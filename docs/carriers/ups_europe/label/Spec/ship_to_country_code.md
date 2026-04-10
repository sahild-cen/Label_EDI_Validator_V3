# Field: ship_to_country_code

## Display Name
Ship To ISO Country Code

## Field Description
The ISO 3166 numeric country code for the destination country. This 3-digit code is used in the MaxiCode primary message to identify the destination country.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 3 digits
- **Pattern/Regex:** `^[0-9]{3}$`
- **Allowed Values:** ISO 3166 numeric country codes (full list in Appendix E), e.g., 840 = USA, 276 = Germany, 124 = Canada
- **Required:** yes

## Examples from Spec
- `840` (United States)
- `276` (Germany)

## Position on Label
Encoded within MaxiCode primary message. May also appear as part of address block on label.

## ZPL Rendering
- **Typical Position:** Encoded within MaxiCode; not typically printed standalone
- **Font / Size:** Not specified
- **Field Prefix:** None
- **ZPL Command:** Encoded within ^BD (MaxiCode)

## Edge Cases & Notes
- Must use the 3-digit numeric ISO country code, not the 2-character alpha code, within the MaxiCode data string.
- Full ISO 3166 country code table is provided in Appendix E of the spec.

## Claude Confidence
HIGH — spec clearly defines the field with ISO 3166 reference and examples

## Review Status
- [ ] Reviewed by human