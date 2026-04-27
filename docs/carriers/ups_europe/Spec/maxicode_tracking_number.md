# Field: maxicode_tracking_number

## Display Name
Tracking Number (MaxiCode Field)

## Field Description
The tracking number as encoded within the MaxiCode data string secondary message. This is a 10-character alphanumeric field that represents a portion of the full 1Z tracking number.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 10 characters exactly
- **Pattern/Regex:** `[A-Z0-9]{10}` (typically starts with `1Z`)
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- `1Z12345675`
- `1Z12345679`

## Position on Label
Encoded within MaxiCode barcode (secondary message).

## Edge Cases & Notes
- The class of service and shipper number fields from the 1Z number have been omitted in the MaxiCode tracking number field to avoid duplication with the separate class of service and account number fields.

## Claude Confidence
HIGH — spec explicitly states format and reason for omission of duplicated fields

## Review Status
- [x] Reviewed by human