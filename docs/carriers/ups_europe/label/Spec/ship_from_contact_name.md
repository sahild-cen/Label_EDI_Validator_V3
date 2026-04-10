# Field: ship_from_contact_name

## Display Name
Ship From Contact Name

## Field Description
The contact name of the person at the shipping origin/sender location.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
Label examples show "CONTACT NAME" as placeholder in the ship-from section.

## Position on Label
Top-left area of the label in the ship-from address block.

## ZPL Rendering
- **Typical Position:** Top-left corner, first line of ship-from block
- **Font / Size:** Not specified
- **Field Prefix:** "SHIP FROM:" label appears to the left of the shipper information block
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
On the 4x4.25 second label, "SHIP FROM" text must be printed to the left of the shippers information.

## Claude Confidence
HIGH — Clearly visible in multiple label examples

## Review Status
- [ ] Reviewed by human