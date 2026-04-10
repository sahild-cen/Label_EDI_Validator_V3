# Field: ship_to_street_address

## Display Name
Ship To Street Address

## Field Description
The street address of the destination/consignee. For Access Point shipments, this is the UAP street address.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
"STREET ADDRESS", "UAP STREET ADDRESS"

## Position on Label
Middle-left area of label, in the ship-to address block.

## ZPL Rendering
- **Typical Position:** Middle-left, ship-to address block
- **Font / Size:** 12 pt Bold per spec
- **Field Prefix:** None — data value
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
For Access Point shipments, this shows the UAP facility street address rather than the consignee's home address.

## Claude Confidence
HIGH — present in all label examples

## Review Status
- [ ] Reviewed by human