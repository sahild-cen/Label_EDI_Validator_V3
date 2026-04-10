# Field: ship_to_street_address

## Display Name
Ship To Street Address

## Field Description
The street address of the destination/consignee, displayed as human-readable text on the shipping label.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- `STREET ADDRESS` (shown on label example)

## Position on Label
In the "TO:" address block on the label.

## Edge Cases & Notes
- Separate from the MaxiCode-encoded address field which has specific length constraints.

## Claude Confidence
MEDIUM — shown on label example but no detailed format specification in extracted text.

## Review Status
- [ ] Reviewed by human