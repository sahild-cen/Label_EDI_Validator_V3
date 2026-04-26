# Field: shipment_dimensional_weight

## Display Name
Shipment Dimensional Weight

## Group Description
The shipment dimensional weight, printed when applicable. The weight is rounded to the next whole pound or half kilogram. Not applicable for 10 KG and 25 KG boxes.

## Sub-Fields

### shipment_dimensional_weight
- **Data Type:** alphanumeric
- **Length:** 18 (8 prefix + space + up to 5 numeric + space + KG/LBS)
- **Pattern/Regex:** `^SHP DWT:\s[\d.]{1,5}\s(LBS|KG)$`
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Total dimensional weight of the shipment, applicable for all movements except U.S. Domestic and Puerto Rico to the U.S.
- **Detect By:** text_prefix:SHP DWT:
- **Position on Label:** top-right area, beneath shipment weight
- **ZPL Font:** 8pt
- **Field Prefix:** "SHP DWT:"
- **ZPL Command:** ^FD (text field)

## Examples from Spec
- `SHP DWT: 1000 LBS`
- `SHP DWT: 189.5 KG`
- `SHP DWT: 50.5 KG`

## Edge Cases & Notes
- Positions 1-8 = "SHP DWT:", Position 9 = space, Positions 10-14 = up to five numeric, Position 15 = space, Positions 16-18 = LBS or KG
- Dimensional weight will not apply for 10 KG and 25 KG boxes

## Claude Confidence
HIGH — spec clearly defines format with positional data and examples

## Review Status
- [x] Reviewed by human