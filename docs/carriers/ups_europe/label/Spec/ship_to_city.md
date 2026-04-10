# Field: ship_to_city

## Display Name
Ship To City

## Field Description
The city name of the destination/consignee address. Encoded in the MaxiCode secondary message.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 1-20 characters (variable)
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Valid city name
- **Required:** yes

## Examples from Spec
- `ATLANTA` (validated address example)
- `SALT LAKE CITY` (non-validated and letter/envelope examples)
- `COLOGNE` (international example, Germany)

## Position on Label
Encoded within MaxiCode secondary message. Also printed as human-readable text in the ship-to address block.

## ZPL Rendering
- **Typical Position:** Ship-to address block, center/middle of label
- **Font / Size:** Not specified
- **Field Prefix:** None (part of address block)
- **ZPL Command:** ^FD (text field) for human-readable; encoded within ^BD (MaxiCode)

## Edge Cases & Notes
- Maximum 20 characters.

## Claude Confidence
HIGH — spec clearly defines the field with maximum length and multiple examples

## Review Status
- [ ] Reviewed by human