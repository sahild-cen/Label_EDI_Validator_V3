# Field: ship_to_city_state_postal

## Display Name
Ship To City, State/Province, Postal Code

## Field Description
The destination city, state/province, and postal code displayed as human-readable text in the consignee address block on the shipping label.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- `SINGAPORE  486064` (label example)

## Position on Label
In the "TO:" address block on the label, below the street address.

## Edge Cases & Notes
- Format varies by destination country.

## Claude Confidence
MEDIUM — visible on label example but format rules not detailed in extracted text.

## Review Status
- [ ] Reviewed by human