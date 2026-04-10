# Field: shipment_date

## Display Name
Shipment Date

## Field Description
The date the shipment was tendered, displayed on the label in DD MMM YYYY format.

## Format & Validation Rules
- **Data Type:** date
- **Length:** 11 characters (DD MMM YYYY)
- **Pattern/Regex:** `[0-9]{2} (JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC) [0-9]{4}`
- **Allowed Values:** Valid dates with month abbreviations: JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
- **Required:** yes

## Examples from Spec
- "DATE: 11 JAN 2020"
- "DATE: 28 JUN 2017"

## Position on Label
For World Ease: in the shipment information area. For Trade Direct LTL/TL: below the shipment weight. Data content: positions 1-5 = "DATE:", position 6 = space, positions 7-17 = DD MMM YYYY. Font Size = 8 pt.

## Edge Cases & Notes
Month abbreviation table explicitly provided: JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC.

## Claude Confidence
HIGH — spec provides explicit format, month abbreviation table, and examples

## Review Status
- [ ] Reviewed by human