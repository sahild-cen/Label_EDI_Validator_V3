# Field: maxicode_ship_to_city

## Display Name
Ship To City (MaxiCode)

## Field Description
The destination city name encoded in the MaxiCode data string.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 1-20 characters (variable)
- **Pattern/Regex:** `[A-Za-z0-9 ]{1,20}`
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- `ATLANTA`
- `SALT LAKE CITY`
- `COLOGNE`

## Position on Label
Encoded within MaxiCode barcode (secondary message).

## Edge Cases & Notes
- Maximum of 20 characters.

## Claude Confidence
HIGH — spec clearly defines format and provides examples

## Review Status
- [x] Reviewed by human