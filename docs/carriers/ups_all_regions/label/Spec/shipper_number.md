# Field: shipper_number

## Display Name
Shipper Number (SHP#)

## Field Description
The UPS account/shipper number identifying the shipper's UPS account.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable (up to approximately 13 characters with spaces)
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Valid UPS shipper account numbers
- **Required:** yes

## Examples from Spec
- `SHP#: 1X2X 3X33 3TT`
- `SHP #: 1X2X 3X7R CDG`
- `SHP #: 1X2X3X 9TT`
- `SHP #: 1X2X3X 9X4`
- `SHP#: 1X2X3X33 3TS`

## Position on Label
In the upper portion of the label, typically to the right of or below the ship-from address block.

## Edge Cases & Notes
The label prefix alternates between "SHP#:" and "SHP #:" in examples but represents the same field.

## Claude Confidence
HIGH — Consistently shown across all label examples.

## Review Status
- [ ] Reviewed by human