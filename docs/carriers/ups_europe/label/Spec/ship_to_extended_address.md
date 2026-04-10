# Field: ship_to_extended_address

## Display Name
Ship To Extended Address

## Field Description
Additional address line(s) for the destination/consignee (e.g., suite, floor, building). For Access Point shipments, this may be the UAP extended address.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** no — optional

## Examples from Spec
"EXTENDED ADDRESS", "UAP EXTENDED ADDRESS"

## Position on Label
Middle-left area of label, in the ship-to address block.

## ZPL Rendering
- **Typical Position:** Middle-left, ship-to address block
- **Font / Size:** 12 pt Bold per spec
- **Field Prefix:** None — data value
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Some labels omit this field entirely. Access Point labels may have UAP-specific extended address lines.

## Claude Confidence
HIGH — shown in many examples, clearly optional

## Review Status
- [ ] Reviewed by human