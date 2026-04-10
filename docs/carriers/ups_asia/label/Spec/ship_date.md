# Field: ship_date

## Display Name
Ship Date (DATE)

## Field Description
The date the shipment is tendered to UPS, prefixed with "DATE:" on the label.

## Format & Validation Rules
- **Data Type:** date
- **Length:** 11 characters (DD MMM YYYY)
- **Pattern/Regex:** `\d{1,2}\s+[A-Z]{3}\s+\d{4}`
- **Allowed Values:** Valid date in DD MMM YYYY format (e.g., 11 JAN 2020)
- **Required:** yes

## Examples from Spec
"DATE: 11 JAN 2020"

## Position on Label
Upper right portion of the label, in the shipment details block, typically the last line of that block.

## Edge Cases & Notes
All examples in the spec use the same date "11 JAN 2020". The month is a 3-letter uppercase abbreviation.

## Claude Confidence
HIGH — field appears consistently across all label examples with clear format

## Review Status
- [ ] Reviewed by human