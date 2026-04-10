# Field: maxicode_ship_to_city

## Display Name
Ship To City (MaxiCode)

## Field Description
The destination city name encoded in the MaxiCode data string.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 1-20 characters (variable)
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** UPPERCASE characters only
- **Required:** yes

## Examples from Spec
- `ATLANTA`
- `SALT LAKE CITY`
- `COLOGNE`

## Position on Label
Encoded within the MaxiCode barcode (secondary message).

## Edge Cases & Notes
- Must use UPPERCASE characters as required for all MaxiCode data.

## Claude Confidence
HIGH — spec clearly defines as 1-20 character alphanumeric field with multiple examples.

## Review Status
- [ ] Reviewed by human