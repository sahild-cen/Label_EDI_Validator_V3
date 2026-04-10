# Field: tracking_number_human_readable

## Display Name
Human-Readable Tracking Number

## Field Description
The human-readable interpretation of the tracking number barcode, printed as formatted text below the UPS Service Title with specific spacing.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 35 characters (including prefix and spaces)
- **Pattern/Regex:** `^TRACKING #:\s1Z\s[A-Z0-9]{3}\s[A-Z0-9]{3}\s[A-Z0-9]{2}\s\d{4}\s\d{4}$`
- **Allowed Values:** Positions 1-11 = "TRACKING #:", Position 12 = Space, Positions 13-35 = Tracking Number formatted as: 1Z 123 456 78 1234 5678
- **Required:** yes

## Examples from Spec
`TRACKING #: 1Z 1X2 X3X 66 0000 5628`, `TRACKING #: 1Z 1X2 X3X 85 0000 5770`, `TRACKING #: 1Z 1X2 X3X 86 0000 5401`, `TRACKING #: 1Z 1X2 X3X NT 1234 5677`

## Position on Label
Left-justified beneath the UPS Service Title, in uppercase characters within the Tracking Number Barcode Block. Font Size = 10 pt.

## Edge Cases & Notes
- The tracking number is formatted with spaces for readability even though the barcode does not contain spaces.
- All characters must be uppercase.

## Claude Confidence
HIGH — spec clearly defines format with positional data and multiple examples

## Review Status
- [ ] Reviewed by human