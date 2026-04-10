# Field: tracking_number

## Display Name
Tracking Number (1Z Number)

## Field Description
The unique UPS tracking number assigned to each package, prefixed with the "1Z" data identifier. This is the primary identifier for tracking a package through the UPS network.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 18 characters (including "1Z" prefix)
- **Pattern/Regex:** `1Z[A-Z0-9]{6}[A-Z0-9]{2}[0-9]{8}[0-9]` (1Z + 6-char account number + 2-char service level indicator + 8 digits + 1 check digit)
- **Allowed Values:** Not restricted (but must follow Modified MOD 10 check digit calculation)
- **Required:** yes

## Examples from Spec
- `1Z 123 X56 03 1463 8500` (Check Digit Example 1)
- `1Z 123 X56 03 1463 8608` (Check Digit Example 2)
- `1Z 123 X56 66 2075 4864` (Shipment Number Calculation Example 1)
- `1Z 123 X56 Y6 4400 0050` (Shipment Number Calculation Example 2)
- `1Z12345675` (MaxiCode examples - 10-char truncated form without 1Z prefix duplication)

## Position on Label
Encoded in the Code 128 tracking number barcode and printed as human-readable text beneath/near the barcode. Also encoded within the MaxiCode data string (without the "1Z" prefix to avoid duplication with the service level indicator fields).

## Edge Cases & Notes
- The "1Z" data identifier is excluded when performing the check digit calculation.
- Alpha characters are converted to numeric equivalents for check digit computation using a specific cross-reference table.
- If the check digit remainder is 10, the check digit is 0.
- In the MaxiCode data string, only 10 characters of the tracking number are encoded (excluding the "1Z" prefix to avoid duplication of service level and shipper number already encoded elsewhere).
- The Code 128 barcode uses subset A for the "1Z" prefix and shifts to subset C after the last alpha character when an even number of numeric characters remain.

## Claude Confidence
HIGH — spec provides detailed check digit calculation, multiple examples, and barcode encoding instructions.

## Review Status
- [ ] Reviewed by human