# Field: shipment_date

## Display Name
Shipment Date (DATE)

## Field Description
The date the shipment is tendered. Must print for international movements, immediately below the dimensional weight.

## Format & Validation Rules
- **Data Type:** date
- **Length:** 17 characters total (DATE: DD MMM YYYY)
- **Pattern/Regex:** `^DATE:\s\d{2}\s(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\s\d{4}$`
- **Allowed Values:** Month abbreviations: JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
- **Required:** conditional — must print for international movements

## Examples from Spec
`DATE: 28 JAN 2017`, `DATE: 11 JAN 2020`

## Position on Label
Package Information Block, immediately below the dimensional weight. Data content: Positions 1-5 = "DATE:", Position 6 = Space, Positions 7-17 = DD MMM YYYY format.

## Edge Cases & Notes
- Font Size = 8 pt.
- Required for international movements; spec does not specify requirement for domestic.

## Claude Confidence
HIGH — spec clearly defines format with positions, month abbreviation table, and examples

## Review Status
- [ ] Reviewed by human