# Field: ship_date

## Display Name
Ship Date

## Field Description
The date the shipment is tendered to UPS for transport.

## Format & Validation Rules
- **Data Type:** date
- **Length:** fixed format
- **Pattern/Regex:** `\d{2} [A-Z]{3} \d{4}` (e.g., DD MMM YYYY)
- **Allowed Values:** Valid dates
- **Required:** yes

## Examples from Spec
"11 JAN 2020"

## Position on Label
Top-right area, in the shipment information block, typically the last line of that block.

## ZPL Rendering
- **Typical Position:** Top-right information block, below SHP DWT or SHP WT
- **Font / Size:** 8 pt per spec
- **Field Prefix:** "DATE:"
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Date format uses 3-letter month abbreviation in uppercase (JAN, FEB, etc.). Consistent across all label examples in the spec.

## Claude Confidence
HIGH — clearly labeled with "DATE:" prefix, consistent format across all examples

## Review Status
- [ ] Reviewed by human