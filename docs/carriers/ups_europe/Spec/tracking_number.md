# Field: tracking_number

## Display Name
Tracking Number

## Field Description
The unique UPS tracking number for the package, prefixed with "TRACKING #:" on the label. Always begins with "1Z" followed by the shipper account number, service indicator, and package identifier with a check digit.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 18 characters (displayed with spaces for readability)
- **Pattern/Regex:** `1Z[A-Z0-9]{6}[A-Z0-9]{2}\d{8}` (1Z + 6-char shipper number + 2-char service indicator + 7-digit package ID + 1 check digit)
- **Allowed Values:** Must begin with "1Z"
- **Required:** yes

## Examples from Spec
"1Z 1X2 X3X 86 0000 5401", "1Z 1X2 X3X 66 0000 5627", "1Z 1X2 X3X 85 0000 9383", "1Z 1X2 X3X 85 0000 5770", "1Z 1X2 X3X 54 0000 6489", "1Z 1X2 X3X 54 0000 5408", "1Z 1X2 X3X Q4 3112 3201", "1Z 1X2 X3X G9 0000 5405", "1Z 1X2 X3X 04 0000 5403", "1Z 1X2 X3X 67 0000 5401", "1Z 1X2 X3X FX 0000 5404", "1Z 1X2 X3X 68 0000 5409", "1Z 1X2 X3X 01 1234 5672", "1Z 1X2 X3X NT 1234 5677", "1Z 1X2 X3X E1 0000 5403", "1Z 1X2 X3X E5 0000 5405", "1Z 1X2 X3X EA 0000 5401", "1Z 1X2 X3X EV 1234 5618", "1Z 1X2 X3X QE 8712 5626", "1Z 1X2 X3X C7 0000 5403", "1Z 1X2 X3X Z4 0000 5406", "1Z 1X2 X3X Z2 0000 5400", "1Z 1X2 X3X Z7 0000 5777", "1Z 1X2 X3X 75 0000 5404"

## Position on Label
Center-lower section, displayed as human-readable text and also encoded in the 1D barcode. Prefixed with "TRACKING #:".

## Edge Cases & Notes
The tracking number structure is: "1Z" (prefix) + shipper number (6 chars, page 15 shows "1X2X3X") + service type code (2 chars) + package identifier (7 digits) + check digit (1 digit). The check digit is calculated using a modulo-7 algorithm per the remainder table on page 69. Displayed with spaces for human readability but the barcode encodes it without spaces. The tracking number also includes information per page 15 showing the component breakdown: "1Z", "1X2X3X", service indicator, and package sequence.

## Claude Confidence
HIGH — extensively documented with many examples and structural breakdown on page 15

## Review Status
- [x] Reviewed by human