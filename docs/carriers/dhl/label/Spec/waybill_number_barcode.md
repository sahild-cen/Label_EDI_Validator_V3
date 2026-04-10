# Field: waybill_number_barcode

## Display Name
Shipment Identifier / Waybill Number Barcode

## Field Description
Barcode representation of the Waybill Number, always printed in Code 39 symbology with DHL-specific syntax.

## Format & Validation Rules
- **Data Type:** barcode (Code 39)
- **Length:** 10 digits (9-digit waybill + MOD 7 check digit)
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Encoded waybill number with check digit
- **Required:** conditional — printed when present on label

## Examples from Spec
- Barcode content "3100032902" for waybill 310003290 with check digit 2

## Position on Label
In the Waybill barcode segment of the label.

## Edge Cases & Notes
- Uses Code 39 symbology specifically (not Code 128)
- Requires standard start/stop character "*"
- MOD 7 check digit calculation: divide 9-digit number by 7, remainder is check digit
- Minimum barcode height of 25 mm (28 mm recommended)

## Claude Confidence
HIGH — spec clearly defines symbology, check digit algorithm, and provides example

## Review Status
- [ ] Reviewed by human