# Field: ups_service_title

## Display Name
UPS Service Title

## Field Description
The full name of the UPS service selected for the shipment, printed in uppercase letters as the complete service title.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** UPS EXPRESS PLUS, UPS EXPRESS, UPS SAVER, UPS EXPEDITED, UPS STANDARD, UPS EXPRESS FREIGHT, UPS EXPRESS FREIGHT MIDDAY, UPS EXPRESS 12:00, UPS 3 DAY SELECT, and others
- **Required:** yes

## Examples from Spec
- `UPS EXPRESS`
- `UPS SAVER`
- `UPS EXPRESS FREIGHT`
- `UPS EXPRESS 12:00`

## Position on Label
Left-justified and located beneath the top highlight bar in the Tracking Number Barcode Block.

## Edge Cases & Notes
- Must be printed in uppercase letters using the complete service title
- Font Size = 12 pt. bold

## Claude Confidence
HIGH — spec clearly defines placement and formatting with multiple examples

## Review Status
- [x] Reviewed by human