# Field: tracking_number_human_readable

## Display Name
Tracking Number (Human Readable)

## Field Description
The human-readable text representation of the tracking number printed near the tracking number barcode, prefixed with "TRACKING #:".

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 18 characters (displayed with spaces as 1Z XXX XXX XX XXXX XXXX)
- **Pattern/Regex:** `1Z\s[A-Z0-9]{3}\s[A-Z0-9]{3}\s[A-Z0-9]{2}\s[0-9]{4}\s[0-9]{4}`
- **Allowed Values:** Valid UPS tracking number format starting with 1Z
- **Required:** yes

## Examples from Spec
- `1Z 1X2 X3X 86 0000 5401`
- `1Z 1X2 X3X 66 0000 5627`

## Position on Label
Adjacent to or below the tracking number barcode in the Tracking Number Barcode Block.

## ZPL Rendering
- **Typical Position:** Below or adjacent to tracking number barcode
- **Font / Size:** 10pt for "TRACKING #:" label
- **Field Prefix:** "TRACKING #:"
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
- The human-readable interpretation of the barcode must be printed in black.
- Spaces are used in the display format but may not be encoded in the barcode itself.

## Claude Confidence
HIGH — spec clearly shows this in label samples with consistent formatting

## Review Status
- [ ] Reviewed by human