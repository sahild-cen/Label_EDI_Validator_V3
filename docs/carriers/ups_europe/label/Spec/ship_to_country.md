# Field: ship_to_country

## Display Name
Ship To Country

## Field Description
The country name of the destination/consignee address.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted (full country names)
- **Required:** conditional — required for international shipments

## Examples from Spec
"COUNTRY", "GERMANY", "FRANCE", "JAPAN", "UNITED STATES", "CANADA", "COUNTRY NAME"

## Position on Label
Middle-left area of label, last line of the ship-to address block.

## ZPL Rendering
- **Typical Position:** Middle-left, last line of ship-to address block
- **Font / Size:** 12 pt Bold per spec
- **Field Prefix:** None — data value
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
May be omitted for domestic shipments within a country. Present on all international label examples.

## Claude Confidence
HIGH — consistently shown in international label examples

## Review Status
- [ ] Reviewed by human