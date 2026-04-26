# Field: package_weight_and_count

## Display Name
Package Weight and Piece Count

## Group Description
The package-level weight and piece count information displayed in the upper-right corner of the label, showing the individual package weight and the piece number relative to total piece count.

## Sub-Fields

### package_weight
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** `^\d+(\.\d+)?\s+(KG|LBS)(\s+LTR)?$`
- **Allowed Values:** Numeric value followed by unit (KG or LBS), optionally followed by LTR for letter shipments
- **Required:** yes
- **Description:** Weight of the individual package with unit of measure
- **Detect By:** spatial:top-right, numeric value with KG/LBS
- **Position on Label:** top-right corner
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### piece_count
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** `^\d+\sOF\s\d+$`
- **Allowed Values:** Format "X OF Y" where X is current piece and Y is total pieces
- **Required:** yes
- **Description:** Piece number out of total pieces in the shipment (e.g., "1 OF 1")
- **Detect By:** text_pattern:X OF Y
- **Position on Label:** top-right corner, adjacent to package weight
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Examples from Spec
```
50.5 KG    1 OF 1
```
```
5 KG    1 OF 1
```
```
8 KG    1 OF 1
```
```
0.6 LBS LTR    1 OF 1
```
```
203 KG    1 OF 1
```
```
542 LBS    1 OF 1
```
```
3 KG    1 OF 1
```

## Edge Cases & Notes
- "LTR" suffix appears for letter/envelope shipments (e.g., "0.6 LBS LTR").
- Weight unit varies by origin country (KG for Europe, LBS for U.S. origin).

## Claude Confidence
HIGH — multiple label examples consistently show this format in the top-right area.

## Review Status
- [x] Reviewed by human