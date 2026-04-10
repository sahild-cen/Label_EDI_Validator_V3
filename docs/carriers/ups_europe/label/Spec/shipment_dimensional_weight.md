# Field: shipment_dimensional_weight

## Display Name
Shipment Dimensional Weight (SHP DWT)

## Field Description
The shipment dimensional weight, printed when applicable. The weight is rounded to the next whole pound or half kilogram. Applies to all movements except U.S. domestic and Puerto Rico to the U.S.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 18 positions
- **Pattern/Regex:** Positions 1-8 = "SHP DWT:"; Position 9 = space; Positions 10-14 = up to five numeric; Position 15 = space; Positions 16-18 = LBS or KG
- **Allowed Values:** Numeric weight value with unit
- **Required:** conditional — only when dimensional weight applies

## Examples from Spec
- `SHP DWT: 1000 LBS`
- `SHP DWT: 189.5 KG`
- `SHP DWT: 50.5 KG`

## Position on Label
Prints in the Package Information Block area, below the shipment weight.

## ZPL Rendering
- **Typical Position:** Top-right area, below shipment weight
- **Font / Size:** 8pt
- **Field Prefix:** "SHP DWT:"
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
- Dimensional weight will not apply for 10 KG and 25 KG boxes.
- Only applies for movements other than U.S. domestic and Puerto Rico to the U.S.

## Claude Confidence
HIGH — spec provides detailed data content, conditions, and examples

## Review Status
- [ ] Reviewed by human