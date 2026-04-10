# Field: human_readable_tracking_number

## Display Name
Human-Readable Tracking Number Interpretation

## Field Description
The text representation of the data content of the tracking number barcode, printed in human-readable form adjacent to or below the barcode symbol.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 18 characters (matching tracking number)
- **Pattern/Regex:** Same as tracking number
- **Allowed Values:** Must exactly match the encoded barcode data
- **Required:** yes

## Examples from Spec
No examples in spec.

## Position on Label
Below or adjacent to the Code 128 tracking number barcode.

## ZPL Rendering
- **Typical Position:** Directly below the tracking number barcode
- **Font / Size:** Not specified in extracted text — typically OCR quality fonts
- **Field Prefix:** "TRACKING #:" or none
- **ZPL Command:** ^FD (text field) — may also use ^BCN with interpretation line enabled

## Edge Cases & Notes
- The spec defines "Human-Readable Interpretation" as the text representing the data content of a barcode, and "Human-Readable Text" as all text NOT representing encoded barcode data — these are distinct concepts.
- OCR Quality Fonts are referenced in the spec: print settings readable by humans as well as machines.

## Claude Confidence
MEDIUM — Concept is clearly defined in glossary but specific rendering details not in extracted text.

## Review Status
- [ ] Reviewed by human