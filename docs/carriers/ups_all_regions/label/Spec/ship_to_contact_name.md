# Field: ship_to_contact_name

## Display Name
Ship To Contact Name

## Field Description
The contact name of the consignee/recipient at the destination.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- `CONTACT NAME` (placeholder)
- For Hold for Pickup with Express Freight: `HOLD FOR PICKUP - D SCHMIDT`

## Position on Label
Printed in the "SHIP TO:" address block.

## Edge Cases & Notes
For Hold for Pickup shipments with UPS Trade Direct / Express Freight, the text "HOLD FOR PICKUP" must print before the consignee's name separated by a dash. Example: "HOLD FOR PICKUP - D SCHMIDT".

## Claude Confidence
HIGH — Consistently shown on all labels with special Hold for Pickup formatting noted.

## Review Status
- [ ] Reviewed by human