# Field: package_weight

## Display Name
Package Weight

## Field Description
The weight of the individual package, encoded in the MaxiCode data string and displayed as human-readable text on the shipping label.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 1-3 characters
- **Pattern/Regex:** `\d{1,3}`
- **Allowed Values:** Rounded up to next whole pound or kilogram; minimum 1 pound or 1 kilogram (except Letters/Envelopes)
- **Required:** yes (conditional — blank for Letters/Envelopes unless weight equals or exceeds published threshold; blank if weight exceeds maximum characters for Worldwide Express Freight)

## Examples from Spec
- `37` (MaxiCode validated address example)
- `10` (MaxiCode non-validated and international examples)
- `1` (MaxiCode Letter/Envelope example — though spec says leave blank for Letters)
- `20 KG` (label example showing "SHP WT: 20 KG")

## Position on Label
Encoded in the MaxiCode barcode. Human-readable "SHP WT: 20 KG" displayed on the label.

## Edge Cases & Notes
- Round up to next whole pound or kilogram.
- Minimum weight is 1 pound or 1 kilogram unless the package type is Letter or Envelope.
- Leave blank for Letters and Envelopes unless weight equals or exceeds published threshold.
- Leave blank if weight exceeds maximum number of characters (for UPS Worldwide Express Freight).

## Claude Confidence
HIGH — spec clearly defines format with conditional rules and multiple examples.

## Review Status
- [ ] Reviewed by human