# Field: shipment_identifier_waybill_number

## Display Name
Shipment Identifier / Waybill Number

## Field Description
The unique shipment identifier that serves as a proxy for the Waybill Number. Mandatory for all DHL Express products on the Transport Label.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 10 digits (9-digit waybill number + 1 check digit)
- **Pattern/Regex:** Not specified in spec beyond numeric grouping
- **Allowed Values:** DHL 10-digit waybill numbering system
- **Required:** yes — mandatory for all DHL Express products; omission requires explicit DHL approval

## Examples from Spec
- Waybill number 310003290 with check digit 2 = barcode content "3100032902"

## Position on Label
Printed in the Waybill Number segment. Must be printed in groups of four digits, with grouping sequence starting at the end and built towards the left side.

## Edge Cases & Notes
- Check digit uses MOD 7: 9-digit number divided by 7, remainder forms the check digit (10th digit)
- Grouping in four digits is mandatory (same as Piece Identifier grouping)
- Human-readable format must match the grouped display

## Claude Confidence
HIGH — spec clearly defines format, check digit calculation with example, and mandatory status

## Review Status
- [ ] Reviewed by human