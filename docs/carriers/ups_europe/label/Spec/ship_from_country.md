# Field: ship_from_country

## Display Name
Ship From Country

## Field Description
The country name of the shipper/sender in the ship-from address block.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted (full country names used)
- **Required:** yes

## Examples from Spec
"COUNTRY", "GERMANY", "UNITED STATES", "ITALY", "BELGIUM", "UNITED KINGDOM"

## Position on Label
Top-left area of label, last line of the ship-from address block.

## ZPL Rendering
- **Typical Position:** Top-left, last line of shipper address block
- **Font / Size:** 10 pt per spec
- **Field Prefix:** None — data value
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Country may be omitted for domestic shipments in some examples.

## Claude Confidence
HIGH — consistently present in international label examples

## Review Status
- [ ] Reviewed by human