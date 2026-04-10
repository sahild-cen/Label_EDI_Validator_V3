# Field: ship_from_extended_address

## Display Name
Ship From Extended Address

## Field Description
Additional address line for the shipper (e.g., suite, floor, building) in the ship-from address block.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** no — optional additional address line

## Examples from Spec
"EXTENDED ADDRESS"

## Position on Label
Top-left area of label, in the ship-from address block below company name.

## ZPL Rendering
- **Typical Position:** Top-left, shipper address block
- **Font / Size:** 10 pt per spec
- **Field Prefix:** None — data value
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Not always present on all label examples — some labels skip this line (e.g., page 52 label omits extended address).

## Claude Confidence
HIGH — shown on most label examples but clearly optional

## Review Status
- [ ] Reviewed by human