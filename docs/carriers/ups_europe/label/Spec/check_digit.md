# Field: check_digit

## Display Name
Check Digit (Modified MOD 10)

## Group Description
A mathematically derived check digit appended to the end of the UPS Tracking Number for validation purposes.

## Sub-Fields

### check_digit
- **Data Type:** numeric
- **Length:** 1
- **Pattern/Regex:** Calculated via Modified MOD 10 algorithm
- **Allowed Values:** 0-9
- **Required:** yes
- **Description:** The final character of the UPS Tracking Number, calculated using the Modified MOD 10 algorithm. Used to validate the integrity of the encoded barcode data.
- **Detect By:** Last character of tracking number
- **Position on Label:** Embedded as last digit of tracking number
- **ZPL Font:** Not applicable (part of tracking number)
- **Field Prefix:** None
- **ZPL Command:** Part of tracking number ^FD

## Examples from Spec
No examples in spec (this extract).

## Edge Cases & Notes
- Modified MOD 10 is a UPS-specific check digit calculation, distinct from standard MOD 10.
- The check digit is integral to the tracking number and its barcode — it is not displayed separately.

## Claude Confidence
MEDIUM — Algorithm name is defined; calculation method details not provided in this extract.

## Review Status
- [x] Reviewed by human