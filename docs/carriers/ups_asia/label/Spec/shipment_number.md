# Field: shipment_number

## Display Name
UPS Shipment Number

## Field Description
For international shipments, the shipment number is calculated from the Tracking Number of the first package in the shipment and must print on all packages within the shipment.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 19 characters total (including prefix "SHP#: ")
- **Pattern/Regex:** `^SHP#:\s[A-Z0-9]{4}\s[A-Z0-9]{4}\s[A-Z0-9]{3}$`
- **Allowed Values:** Not restricted (calculated from tracking number)
- **Required:** conditional — Required for international shipments

## Examples from Spec
- `SHP#: 1234 5E7R CDG`
- `SHP#: 1X2X 3X33 3VP`
- `SHP#: 1X2X 3X7R CDG`

## Position on Label
Directly beneath the package weight and count, in the Package Information Block area.

## Edge Cases & Notes
- Data Content: Positions 1-5 = "SHP#:", Position 6 = Space, Positions 7-19 = 13 alphanumeric
- Text Spacing = 1234 5678 901 (groups of 4, 4, 3)
- Font Size = 8 pt.
- Calculation details are in Appendix D of the spec

## Claude Confidence
HIGH — spec clearly defines format, positions, and examples

## Review Status
- [ ] Reviewed by human