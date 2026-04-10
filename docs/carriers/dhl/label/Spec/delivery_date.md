# Field: delivery_date

## Display Name
Delivery Date

## Field Description
Shows the delivery date feature for the shipment, indicating the specific day of the month or a special delivery instruction. This value is also mandatorily coded in the routing barcode.

## Format & Validation Rules
- **Data Type:** numeric or alphanumeric (on label); 2 numeric digits in routing barcode
- **Length:** 2 digits in routing barcode (fixed length); 2 characters on label display
- **Pattern/Regex:** `[0-9]{2}` in routing barcode; label may show numeric 01-31, or alpha codes A, S, H
- **Allowed Values:** 00 (no fixed date), 01-31 (day of month), 50 (Saturday only), 51 (appointment), 52 (hold at depot)
- **Required:** conditional — mandatory in routing barcode (zeroes if no date); conditional on label display

## Examples from Spec
- "00" in routing barcode = no fixed date delivery (nothing on label)
- "01" ... "31" = fixed day delivery (day of month shown on label)
- "51" = delivery on appointment ("A" on label)
- "50" = Saturday only delivery ("S" on label)
- "52" = hold at depot ("H" on label)

## Position on Label
Displayed in the delivery date/time segment with a "Day" header. The header may be in local language for domestic shipments but must include English words "Day" and "Time" for international shipments.

## Edge Cases & Notes
- The day of month is represented in 2-digit numeric format with leading zeroes
- May contain non-numeric values representing delivery instructions that cannot be combined with a certain delivery date
- A separator "-" between Date and Time fields is required whenever at least one of both features is chosen
- In routing barcode, field must be populated with zeroes ("00") if no valid date information is available — field may not remain empty

## Claude Confidence
HIGH — spec provides detailed table of values, routing barcode encoding, and display rules

## Review Status
- [ ] Reviewed by human