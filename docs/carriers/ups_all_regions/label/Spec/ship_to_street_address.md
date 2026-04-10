# Field: ship_to_street_address

## Display Name
Ship To Street Address

## Field Description
The street address of the consignee/recipient at the destination. For SurePost labels, this appears in the USPS delivery section.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- `STREET ADDRESS` (placeholder used on sample labels)

## Position on Label
Printed in the "SHIP TO:" address block and/or the USPS delivery section for SurePost.

## Edge Cases & Notes
For SurePost labels, the ship-to address appears both in the UPS address block and in the USPS DELIVER TO section.

## Claude Confidence
HIGH — Consistently shown on all sample labels.

## Review Status
- [ ] Reviewed by human