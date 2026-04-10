# Field: ship_from_phone_number

## Display Name
Ship From Phone Number

## Field Description
The telephone number of the shipper/sender.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
Label examples show "PHONE NUMBER" as placeholder in the ship-from section.

## Position on Label
Top-left area of the label, below the ship-from contact name.

## ZPL Rendering
- **Typical Position:** Top-left, second line of ship-from block
- **Font / Size:** Not specified
- **Field Prefix:** None (appears as data only within the address block)
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
On the 4x4.25 second label, this is part of the shipper information block. Font size specified as 8 pt. bold for the second label.

## Claude Confidence
HIGH — Visible in all label examples

## Review Status
- [ ] Reviewed by human