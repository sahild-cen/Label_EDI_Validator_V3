# Field: shipper_number

## Display Name
Shipper Number (SHP#)

## Field Description
The UPS shipper number identifying the shipping account, displayed in the ship-from information area of the label.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
"SHP#: 1X2X 3X33 3VP", "SHP#: 1X2X 3X33 3TT", "SHP #: 12 3XX 3WB"

## Position on Label
Top-right area of the label, in the package information block adjacent to the ship-from address.

## ZPL Rendering
- **Typical Position:** Top-right area, package information block
- **Font / Size:** Not specified
- **Field Prefix:** "SHP#:" or "SHP #:"
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
The prefix format varies slightly between examples ("SHP#:" vs "SHP #:").

## Claude Confidence
HIGH — multiple examples clearly shown in spec

## Review Status
- [ ] Reviewed by human