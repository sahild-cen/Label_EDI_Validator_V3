# Field: shipment_dimensional_weight

## Display Name
Shipment Dimensional Weight (SHP DWT)

## Field Description
The dimensional weight of the shipment, printed when it applies. The weight is rounded to the next whole pound or half kilogram. Applies to all movements except U.S. Domestic and Puerto Rico to the U.S.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** `^SHP DWT:\s\d+(\.\d)?\s(LBS|KG)$`
- **Allowed Values:** Not restricted
- **Required:** conditional — prints when dimensional weight applies; does not apply for 10 KG and 25 KG boxes

## Examples from Spec
`SHP DWT: 1000 LBS`, `SHP DWT: 189.5 KG`, `SHP DWT: 50.5 KG`, `SHP DWT: 8 KG`, `SHP DWT: 45 KG`

## Position on Label
Package Information Block, below the shipment weight. Data content: Positions 1-8 = "SHP DWT:", Position 9 = Space, Positions 10-14 = Up to five numeric, Position 15 = Space, Positions 16-18 = LBS or KG.

## Edge Cases & Notes
- Dimensional weight will not apply for 10 KG and 25 KG boxes.
- Weight rounded to next whole pound or half kilogram.
- Font Size = 8 pt.

## Claude Confidence
HIGH — spec clearly defines format, data content positions, and examples

## Review Status
- [ ] Reviewed by human