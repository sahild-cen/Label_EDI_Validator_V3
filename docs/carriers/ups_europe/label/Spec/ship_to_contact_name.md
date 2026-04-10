# Field: ship_to_contact_name

## Display Name
Ship To Contact Name

## Field Description
The contact name at the destination/consignee address. For Access Point shipments, this may be the consignee name rather than the facility contact.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
"SHIP CONTACT NAME", "SHIP HOLD FOR PICKUP - CONTACT NAME", "SHIP CONSIGNEE NAME"

## Position on Label
Middle-left area of label, first line of the ship-to address block, preceded by "TO:" prefix on the same or preceding line.

## ZPL Rendering
- **Typical Position:** Middle-left, ship-to address block
- **Font / Size:** 12 pt Bold per spec
- **Field Prefix:** "TO:" — appears before or above the consignee address block
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
For UPS Access Point shipments, the label shows "SHIP CONSIGNEE NAME" and the Access Point name/address replaces the standard consignee address. For Hold for Pickup, the prefix becomes "SHIP HOLD FOR PICKUP -".

## Claude Confidence
HIGH — consistently shown across all label examples

## Review Status
- [ ] Reviewed by human