# Field: weight

## Display Name
Package Weight

## Group Description
The weight of the individual package displayed prominently in the upper-right area of the label. Can be in kilograms (KG) or pounds (LBS).

## Sub-Fields

### package_weight
- **Data Type:** numeric
- **Length:** variable
- **Pattern/Regex:** `^\d+(\.\d+)?\s*(KG|LBS)$`
- **Allowed Values:** Not restricted (positive numeric with unit)
- **Required:** yes
- **Description:** Weight of the individual package, displayed with unit of measure (KG or LBS)
- **Detect By:** spatial:top_right, numeric value followed by KG or LBS
- **Position on Label:** top-right area, prominently displayed
- **ZPL Font:** Not specified (appears bold/large)
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Examples from Spec
- "50.5 KG"
- "5 KG"
- "8 KG"
- "3 KG"
- "0.6 LBS"
- "203 KG"
- "542 LBS"
- "38 KG"
- "2.3 KG"
- "20 KG"

## Edge Cases & Notes
- Weight unit varies by origin/destination: KG for European shipments, LBS for US-origin shipments.
- May include decimals (e.g., "50.5 KG", "0.6 LBS").
- For UPS Express Freight, weights can be much larger (e.g., "203 KG", "1542 LBS").
- The "ENV" suffix may appear after weight for envelope shipments (e.g., "2.3 KG ENV").
- The "LTR" suffix may appear for letter shipments (e.g., "0.6 LBS LTR").

## Claude Confidence
HIGH — Weight appears consistently across all label examples in the same position.

## Review Status
- [x] Reviewed by human