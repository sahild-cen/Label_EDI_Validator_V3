# Field: tracking_number_barcode

## Display Name
Tracking Number Barcode (Code 128)

## Field Description
A 1D Code 128 barcode encoding the full 1Z tracking number. This is the primary barcode used for scanning and tracking the package.

## Format & Validation Rules
- **Data Type:** barcode (Code 128)
- **Length:** 18 characters (full 1Z tracking number); 15 encoded characters after subset C compression
- **Pattern/Regex:** Starts with subset A for "1Z" and alpha characters, shifts to subset C for numeric compression
- **Allowed Values:** Full 1Z tracking number
- **Required:** yes

## Examples from Spec
- Encoded tracking number: `1Z 123 X56 03 1463 8500` (from check digit examples)

## Position on Label
Not specified in spec (typically in the main barcode area of the label).

## Edge Cases & Notes
- Start with subset A, use uppercase for all alpha characters.
- Shift to subset C after "1Z" if no alpha characters in shipper number or service level indicator.
- Shift to subset C after the last occurrence of an alpha character when an even number of numeric characters remain.
- Example shift: `Start A 1Z 123 4X5 Shift C 01 1234 5679`
- The total number of encoded characters is 15 after compression.

## Claude Confidence
HIGH — spec provides detailed Code 128 encoding rules and shift logic

## Review Status
- [x] Reviewed by human