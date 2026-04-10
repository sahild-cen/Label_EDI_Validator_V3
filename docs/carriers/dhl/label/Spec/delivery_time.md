# Field: delivery_time

## Display Name
Delivery Time

## Field Description
Shows the time window code for delivery, indicating a specific delivery time commitment. This value is always mandatorily coded in the routing barcode.

## Format & Validation Rules
- **Data Type:** numeric (in routing barcode); alphanumeric display on label
- **Length:** 1 numeric digit in routing barcode (fixed length)
- **Pattern/Regex:** `[0-9]` in routing barcode
- **Allowed Values:** 0 (no fixed time), 1 (pre 09:00), 2 (pre 12:00), 3 (pre 10:30), plus others
- **Required:** conditional — mandatory in routing barcode (zero if no time); conditional on label display

## Examples from Spec
- "0" in routing barcode = no fixed delivery time (nothing on label)
- "1" = Pre 09:00, displayed as "X09" on label
- "3" = Pre 10:30, displayed as "X10" on label
- "2" = Pre 12:00, displayed as "X12" on label

## Position on Label
Displayed in the delivery date/time segment with a "Time" header, adjacent to the delivery date field.

## Edge Cases & Notes
- In routing barcode, must be populated with zero if no delivery time is specified — field may not remain empty
- The separator "-" between Date and Time field is required whenever at least one feature is chosen
- Header "Time" may be in local language for domestic but must include English for international shipments

## Claude Confidence
HIGH — spec provides clear mapping table and routing barcode rules

## Review Status
- [ ] Reviewed by human