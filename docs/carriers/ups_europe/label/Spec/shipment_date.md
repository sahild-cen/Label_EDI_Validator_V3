# Field: shipment_date

## Display Name
Shipment Date

## Field Description
The date the shipment is created/tendered to UPS. Must print for international movements.

## Format & Validation Rules
- **Data Type:** date
- **Length:** 17 positions (including prefix)
- **Pattern/Regex:** `DATE:\s\d{2}\s(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\s\d{4}`
- **Allowed Values:** Valid date with month abbreviations: JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
- **Required:** conditional — required for international movements

## Examples from Spec
- `DATE: 28 JAN 2018`
- `DATE: 11 JAN 2020`

## Position on Label
Prints immediately below the dimensional weight in the Package Information Block area.

## ZPL Rendering
- **Typical Position:** Top-right area, below dimensional weight
- **Font / Size:** 8pt
- **Field Prefix:** "DATE:"
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
- Date format is DD MMM YYYY (e.g., 28 JAN 2018).
- Three-letter month abbreviations are used.
- Required for international movements only.

## Claude Confidence
HIGH — spec provides clear format, examples, and month abbreviation table

## Review Status
- [ ] Reviewed by human