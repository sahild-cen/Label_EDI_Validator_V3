# Field: ship_to_phone_number

## Display Name
Ship To Phone Number

## Field Description
The phone number of the consignee/recipient at the destination address.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
"PHONE NUMBER", "CONSIGNEE PHONE NUMBER"

## Position on Label
Middle-left area of label, in the ship-to address block below the "TO:" line.

## ZPL Rendering
- **Typical Position:** Middle-left, ship-to address block
- **Font / Size:** 12 pt Bold per spec
- **Field Prefix:** None — data value (but preceded by "TO:" block header)
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
For Access Point shipments the field shows "CONSIGNEE PHONE NUMBER".

## Claude Confidence
HIGH — shown in all label examples

## Review Status
- [ ] Reviewed by human