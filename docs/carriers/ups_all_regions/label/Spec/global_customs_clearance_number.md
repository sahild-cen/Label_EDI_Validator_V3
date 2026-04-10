# Field: global_customs_clearance_number

## Display Name
Global Customs Clearance Number (GCC#)

## Field Description
The shipment's customs clearance number, calculated from the virtual document box 1Z tracking number. Same as the Shipment Number. See Appendix D of the UPS Guide to Labeling for calculation.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 19 characters (including prefix and spaces)
- **Pattern/Regex:** `GCC #: [A-Z0-9]{6} [A-Z0-9]{5}`
- **Allowed Values:** Not restricted
- **Required:** yes — on summary labels

## Examples from Spec
- "GCC #: 1X2X3X 9WB3K"
- "GCC #: 1X2X3X 333WB"

## Position on Label
On the summary label. Font Size = 12 pt. Data content: positions 1-3 = "GCC", position 4 = space, positions 5-6 = "#:", position 7 = space, positions 8-13 = alphanumeric, position 14 = space, positions 15-19 = alphanumeric.

## Edge Cases & Notes
The GCC# is derived from the shipment's virtual document box 1Z tracking number. The calculation method is documented in Appendix D of the UPS Guide to Labeling, not in this supplement.

## Claude Confidence
HIGH — spec provides explicit positional format and multiple examples

## Review Status
- [ ] Reviewed by human