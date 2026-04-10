# Field: ups_service_title

## Display Name
UPS Service Title

## Field Description
The complete UPS service name printed in uppercase letters within the Tracking Number Barcode Block.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Service titles including: UPS EXPRESS PLUS, UPS EXPRESS (NA1), UPS EXPRESS, UPS SAVER, UPS EXPEDITED, UPS STANDARD, UPS 3 DAY SELECT, UPS NEXT DAY AIR, UPS EXPRESS FREIGHT
- **Required:** yes

## Examples from Spec
`UPS EXPRESS`, `UPS SAVER`, `UPS EXPEDITED`, `UPS NEXT DAY AIR`

## Position on Label
Left-justified and located beneath the top highlight bar in the Tracking Number Barcode Block. Font Size = 12 pt. bold. Printed in uppercase letters using the complete service title.

## Edge Cases & Notes
None noted.

## Claude Confidence
HIGH — spec clearly defines placement and examples; service titles listed in service indicator tables

## Review Status
- [ ] Reviewed by human