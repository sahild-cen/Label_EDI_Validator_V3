# Field: ship_from_street_address

## Display Name
Ship From Street Address

## Field Description
The street address of the shipper/sender location.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
Label examples show "STREET ADDRESS" as placeholder. Manifest example: "WOLUWELAAN 156"

## Position on Label
Top-left area of the label, within the ship-from address block.

## ZPL Rendering
- **Typical Position:** Top-left, within ship-from block
- **Font / Size:** Not specified
- **Field Prefix:** None (part of address block)
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
May include extended address lines.

## Claude Confidence
HIGH — Clearly shown in label examples

## Review Status
- [ ] Reviewed by human