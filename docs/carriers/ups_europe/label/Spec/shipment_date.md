# Field: shipment_date

## Display Name
Shipment Date

## Group Description
The date the shipment is tendered to UPS. Required for international movements, printed immediately below the dimensional weight.

## Sub-Fields

### shipment_date
- **Data Type:** date
- **Length:** 17 (5 prefix + space + 11 date)
- **Pattern/Regex:** `^DATE:\s\d{2}\s(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\s\d{4}$`
- **Allowed Values:** Valid dates with month abbreviations: JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
- **Required:** yes
- **Description:** Shipment date in DD MMM YYYY format
- **Detect By:** text_prefix:DATE:
- **Position on Label:** top-right area, immediately below dimensional weight
- **ZPL Font:** 8pt
- **Field Prefix:** "DATE:"
- **ZPL Command:** ^FD (text field)

## Examples from Spec
- `DATE: 28 JAN 2018`
- `DATE: 11 JAN 2020`

## Edge Cases & Notes
- Positions 1-5 = "DATE:", Position 6 = space, Positions 7-17 = date in DD MMM YYYY format
- Month abbreviation table: JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC

## Claude Confidence
HIGH — spec clearly defines format, regex-compatible pattern, and examples

## Review Status
- [x] Reviewed by human