# Field: barcode_title

## Display Name
Barcode Title (Tracking # Label)

## Field Description
The human-readable text label "TRACKING #:" followed by the formatted tracking number, printed beneath the UPS Service Title to identify the tracking number barcode.

## Format & Validation Rules
- **Data Type:** string
- **Length:** 35 characters (positions 1-35)
- **Pattern/Regex:** `TRACKING #: 1Z [A-Z0-9]{3} [A-Z0-9]{3} [A-Z0-9]{2} [0-9]{4} [0-9]{4}`
- **Allowed Values:** Positions 1-11 = "TRACKING #:", Position 12 = Space, Positions 13-35 = Tracking number formatted with spaces
- **Required:** yes

## Examples from Spec
- `TRACKING #: 1Z 123 X56 66 0000 5628`
- `TRACKING #: 1Z 1X2 X3X 85 0000 9383`

## Position on Label
Left-justified beneath the UPS Service Title, in uppercase characters.

## Edge Cases & Notes
- Font size = 10 pt. as specified in the spec

## Claude Confidence
HIGH — spec clearly defines data content with positional layout

## Review Status
- [x] Reviewed by human