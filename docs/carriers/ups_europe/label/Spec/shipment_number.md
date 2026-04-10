# Field: shipment_number

## Display Name
UPS Shipment Number

## Field Description
For international shipments, a number calculated from the tracking number of the first package in the shipment. Must print on all packages within the shipment.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 13 characters (positions 7-19 after prefix)
- **Pattern/Regex:** `SHP#:\s[A-Z0-9]{4}\s[A-Z0-9]{4}\s[A-Z0-9]{3}`
- **Allowed Values:** 13 alphanumeric characters with spacing pattern 1234 5678 901
- **Required:** conditional — required for international shipments

## Examples from Spec
- `SHP#: 1234 5E7R CDG`
- `SHP#: 1X2X 3X33 3VP`
- `SHP#: 1X2X 3X7R CDG`

## Position on Label
Directly beneath the package weight and count in the Package Information Block (top right area).

## ZPL Rendering
- **Typical Position:** Top-right area, below package weight/count
- **Font / Size:** 8pt
- **Field Prefix:** "SHP#:"
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
- Calculated from the tracking number of the first package in the shipment.
- See Appendix D for detailed calculation method.
- Text spacing format: groups of 4-4-3 characters.

## Claude Confidence
HIGH — spec provides detailed data content, position descriptions, and examples

## Review Status
- [ ] Reviewed by human