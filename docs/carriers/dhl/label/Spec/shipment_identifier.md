# Field: shipment_identifier

## Display Name
Shipment Identifier (Waybill Number)

## Field Description
The shipment-level identifier for DHL Express, implemented in a 10-digit numeric format consisting of 9 digits plus a 10th check digit calculated using MOD7. This identifier is also known as the Air Waybill number, Waybill number, Shipment number, or Consignment number. It is encoded in a Code 39 barcode on the label.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 10 digits (9 base digits + 1 MOD7 check digit)
- **Pattern/Regex:** `\d{10}` where the 10th digit = remainder of (first 9 digits ÷ 7)
- **Allowed Values:** Not restricted beyond the MOD7 check digit validation
- **Required:** yes

## Examples from Spec
- Waybill number: 310003290
  - 310003290 ÷ 7 = 44286184 remainder 2
  - Check digit = 2
  - Full barcode content = 3100032902

## ZPL Rendering
- **Typical Position:** Barcode area of the label, typically near piece identifier
- **Font / Size:** Human-readable text printed alongside barcode; font not specified
- **Field Prefix:** Start/stop character "*" for Code 39 encoding
- **ZPL Command:** ^B3 (Code 39) — with start/stop "*" characters, wide-to-narrow ratio 2.2–3.0

## Edge Cases & Notes
- MOD7 check digit calculation: divide 9-digit number by 7, take the remainder as the 10th digit.
- Code 39 barcode requires standard start and stop character "*".
- Wide-to-narrow gap must be between 2.2 and 3.0.
- Minimum barcode height is 25 mm, but 28 mm recommended.
- X-dimension must be between 0.36 mm and 0.425 mm for Code 39.
- Also known as: Air Waybill number, Waybill number, Shipment number, Consignment number.

## Claude Confidence
HIGH — explicitly defined with full format, check digit algorithm, and barcode specifications

## Review Status
- [ ] Reviewed by human