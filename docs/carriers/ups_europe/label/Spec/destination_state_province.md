# Field: destination_state_province

## Display Name
Destination State/Province/County

## Field Description
The state, province, or county in the consignee/destination address. Part of the postal code line format along with city and postal code.

## Format & Validation Rules
- **Data Type:** string
- **Length:** Variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted — valid state/province/county for the destination country
- **Required:** conditional — depends on destination country requirements

## Examples from Spec
No examples in spec.

## Position on Label
Within the consignee address block as part of the postal code line:
- Address Format 1: Postal Code, City, State/Province/County
- Address Format 2: City, State/Province/County, Postal Code

## ZPL Rendering
- **Typical Position:** Consignee address block
- **Font / Size:** Not specified
- **Field Prefix:** None — part of address line
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
- Not all countries require a state/province field.

## Claude Confidence
MEDIUM — Referenced in address format matrix but no independent field specification in extracted text.

## Review Status
- [ ] Reviewed by human