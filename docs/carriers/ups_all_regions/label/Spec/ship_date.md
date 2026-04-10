# Field: ship_date

## Display Name
Ship Date

## Field Description
The date the shipment is tendered to UPS.

## Format & Validation Rules
- **Data Type:** date
- **Length:** 11 characters (DD MMM YYYY)
- **Pattern/Regex:** `\d{2} [A-Z]{3} \d{4}`
- **Allowed Values:** Valid dates
- **Required:** yes

## Examples from Spec
- `DATE: 11 JAN 2020`

## Position on Label
In the upper right portion of the label, near the shipper number and weight fields.

## Edge Cases & Notes
Consistently formatted as "DATE: DD MMM YYYY" across all examples. The month is abbreviated to 3 uppercase letters.

## Claude Confidence
HIGH — Consistently shown across all label examples with clear format.

## Review Status
- [ ] Reviewed by human