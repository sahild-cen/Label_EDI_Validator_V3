# Field: package_weight

## Display Name
Package Weight

## Group Description
The individual package weight displayed in the top-right corner of the label. The actual package weight, rounded up to the next whole pound or half kilogram.

## Sub-Fields

### package_weight
- **Data Type:** alphanumeric
- **Length:** 8 (positions 1-8: up to 4 alphanumeric + space + KG/LBS)
- **Pattern/Regex:** `^\d{1,4}(\.\d)?\s(KG|LBS)$`
- **Allowed Values:** Not restricted (weight value + unit KG or LBS)
- **Required:** conditional — not required for Europe and Asia origins
- **Description:** The actual weight of the individual package, rounded up to the next whole pound or half kilogram
- **Detect By:** spatial:top_right, numeric value followed by KG or LBS
- **Position on Label:** top-right corner, immediately to the left of the package count
- **ZPL Font:** 12pt bold
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Examples from Spec
- `12.5 KG`
- `5 LBS`
- `50.5 KG`
- `12 KG`

## Edge Cases & Notes
- Positions 1-4 = up to four alphanumeric, Position 5 = space, Positions 6-8 = KG or LBS
- When a UPS PAK is used, the weight and PAK indicator replace this field (e.g., `5.5 KG PAK`, `2.4 LBS PAK`)
- When UPS Envelope/UPS Letter is used, weight with one decimal point plus ENV or LTR replaces this field (e.g., `0.3 KG ENV`, `0.5 LBS LTR`)
- When UPS 25 KG BOX or 10 KG BOX is used, text `25 KG BOX` or `10 KG BOX` replaces this field
- If actual weight exceeds the selected shipping option, the actual package weight must print
- Not required for Europe and Asia origins

## Claude Confidence
HIGH — spec provides detailed positional data content and examples

## Review Status
- [x] Reviewed by human