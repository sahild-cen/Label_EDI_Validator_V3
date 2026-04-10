# Field: ship_to_contact_name

## Display Name
Ship To Contact Name

## Field Description
The contact name of the consignee/recipient of the package.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
`CONTACT NAME` (shown on label examples in the "SHIP TO:" section)

## Position on Label
In the Ship To address block, prefixed with "SHIP TO:" label.

## Edge Cases & Notes
For Hold for Pickup shipments, the text "HOLD FOR PICKUP" must print before the consignee's name, separated by a dash (e.g., "HOLD FOR PICKUP - D SCHMIDT").

## Claude Confidence
HIGH — Consistently shown on all label examples.

## Review Status
- [ ] Reviewed by human