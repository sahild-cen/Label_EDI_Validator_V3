# Field: shipment_weight

## Display Name
Shipment Weight

## Field Description
The total weight of a shipment, rounded up to the next whole pound or half kilogram. Appears directly beneath the shipment number.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 18 positions
- **Pattern/Regex:** `SHP WT: ` followed by up to six numeric (inclusive of decimal point) + space + KG or LBS
- **Allowed Values:** Numeric weight value followed by "KG" or "LBS"
- **Required:** yes (for shipments with shipment number)

## Examples from Spec
- `SHP WT: 120.5 KG`
- `SHP WT: 50 LBS`
- `SHP WT: 50.5 KG`
- `SHP WT: 25 KG`

## Position on Label
Directly beneath the shipment number in the Package Information Block. Font size = 8 pt.

## Edge Cases & Notes
- If there is available space on the label, the numeric value can be greater than six characters.
- Weight is rounded up to the next whole pound or half kilogram.

## Claude Confidence
HIGH — spec provides detailed format with examples

## Review Status
- [x] Reviewed by human