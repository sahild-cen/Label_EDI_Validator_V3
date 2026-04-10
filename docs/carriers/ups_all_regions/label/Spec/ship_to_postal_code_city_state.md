# Field: ship_to_postal_code_city_state

## Display Name
Ship To City, State/Province, Postal Code

## Field Description
The destination city, state/province, and postal code for the consignee. For SurePost, the USPS five-digit postal code is also shown separately.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- `MIDDLETON WI 53562` (SurePost USPS delivery)
- `USPS 53562` (SurePost UPS address block)

## Position on Label
Printed in the "SHIP TO:" address block. For SurePost, the USPS 5-digit zip also appears in the UPS Address Block.

## Edge Cases & Notes
For SurePost labels, the USI number must print right justified on the same line as the USPS Ship To five digit postal code in the UPS Address Block.

## Claude Confidence
HIGH — Shown on sample labels with specific SurePost formatting notes.

## Review Status
- [ ] Reviewed by human