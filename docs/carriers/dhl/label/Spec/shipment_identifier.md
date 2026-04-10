# Field: shipment_identifier

## Display Name
Shipment Identifier (Waybill Number / Air Waybill Number)

## Field Description
A generic identifier at the shipment level for DHL Express. Implemented with a 10-digit numeric format: 9 digits plus a 10th check digit calculated using MOD7. Also known as Air Waybill number, Waybill number, Shipment number, or Consignment number.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 10 digits (9 base digits + 1 check digit)
- **Pattern/Regex:** `^\d{10}$` where the 10th digit = (9-digit number) MOD 7
- **Allowed Values:** Not restricted beyond format and check digit
- **Required:** yes

## Examples from Spec
- Waybill number: 310003290
  - 310003290 ÷ 7 = 44286184 remainder 2
  - Check digit = 2
  - Barcode content = 3100032902

## Position on Label
Appears in both human-readable text and as a barcode on the transport label. Barcode uses Code 39 symbology with standard start/stop character "*".

## Edge Cases & Notes
- The check digit is calculated using simple MOD 7: divide the 9-digit number by 7, the remainder is the check digit (10th digit).
- Code 39 barcode specifications: wide-to-narrow gap between 2.2 and 3.0, quiet zones not less than 6 mm.
- Multiple business terms refer to this same identifier: Air Waybill number (Air Express), Waybill number (Air and Road Express), Shipment number (Road Express), Consignment number (Road Express, Freight).

## Claude Confidence
HIGH — Spec clearly defines the 10 NUM format, MOD7 check digit algorithm, and provides a worked example.

## Review Status
- [ ] Reviewed by human