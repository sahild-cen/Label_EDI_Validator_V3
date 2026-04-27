# Field: tracking_number_human_readable

## Display Name
Tracking Number (Human Readable)

## Field Description
The human-readable text representation of the tracking number barcode, printed with the prefix "TRACKING #:" on the label.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 18 characters (1Z + 16 alphanumeric)
- **Pattern/Regex:** `1Z [A-Z0-9]{3} [A-Z0-9]{3} [0-9]{2} [0-9]{4} [0-9]{4}` (spaced format for display)
- **Allowed Values:** Begins with "1Z"
- **Required:** yes

## Examples from Spec
- `1Z 1X2 X3X 86 0000 5401`
- `1Z 1X2 X3X 66 0000 5627`

## Position on Label
Below the tracking number barcode in the Carrier segment. Prefixed with "TRACKING #:".

## Edge Cases & Notes
- Human readable interpretation of the barcode must be printed in black.
- Includes check digit (see Appendix C).

## Claude Confidence
HIGH — multiple examples shown on label samples

## Review Status
- [x] Reviewed by human