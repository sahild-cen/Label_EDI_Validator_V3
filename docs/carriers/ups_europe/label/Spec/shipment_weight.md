# Field: shipment_weight

## Display Name
Shipment Weight (SHP WT)

## Field Description
The total weight of all packages in the shipment, rounded up to the next whole pound or half kilogram.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 18 positions
- **Pattern/Regex:** Positions 1-7 = "SHP WT:"; Position 8 = space; Positions 9-14 = up to six numeric inclusive of decimal point; Position 15 = space; Positions 16-18 = KG or LBS
- **Allowed Values:** Numeric weight value with unit
- **Required:** yes (for shipments)

## Examples from Spec
- `SHP WT: 120.5 KG`
- `SHP WT:  50 LBS`
- `SHP WT: 50.5 KG`
- `SHP WT: 25 KG`

## Position on Label
Directly beneath the shipment number in the Package Information Block.

## ZPL Rendering
- **Typical Position:** Top-right area, below shipment number
- **Font / Size:** 8pt
- **Field Prefix:** "SHP WT:"
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
- If there is available space on the label, the numeric value can be greater than six characters.
- Weight is rounded up to next whole pound or half kilogram.

## Claude Confidence
HIGH — spec provides detailed data content positions and examples

## Review Status
- [ ] Reviewed by human