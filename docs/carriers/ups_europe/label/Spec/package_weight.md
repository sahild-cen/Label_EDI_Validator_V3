# Field: package_weight

## Display Name
Package Weight

## Field Description
The weight of the package in whole pounds or kilograms (rounded up to the next whole unit). This is encoded in the MaxiCode secondary message.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 1-3 digits
- **Pattern/Regex:** `^[0-9]{1,3}$`
- **Allowed Values:** 1-999 (minimum 1 pound or 1 kilogram unless Letter/Envelope)
- **Required:** conditional — required for most packages; leave blank for Letters/Envelopes unless weight meets published threshold; leave blank if weight exceeds maximum characters allowed (for UPS Worldwide Express Freight)

## Examples from Spec
- `37` (validated address example)
- `10` (non-validated and international examples)
- Blank/empty (letter/envelope example)

## Position on Label
Encoded within MaxiCode secondary message. Also typically printed as human-readable text on the label.

## ZPL Rendering
- **Typical Position:** Encoded within MaxiCode; human-readable typically in shipment info area
- **Font / Size:** Not specified
- **Field Prefix:** Not specified in this extract
- **ZPL Command:** Encoded within ^BD (MaxiCode); ^FD (text field) for human-readable

## Edge Cases & Notes
- Round up to next whole pound or kilogram.
- Minimum weight is 1 pound or 1 kilogram.
- For Letters and Envelopes, the weight field must be left blank unless weight equals or exceeds the published threshold.
- For UPS Worldwide Express Freight, leave blank if weight exceeds the maximum number of characters (3 digits = 999).

## Claude Confidence
HIGH — spec provides clear rules and multiple examples including edge cases

## Review Status
- [ ] Reviewed by human