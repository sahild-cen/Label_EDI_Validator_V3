# Field: maxicode_ship_to_postal_code

## Display Name
Ship To Postal Code (MaxiCode)

## Field Description
The destination postal code encoded in the MaxiCode primary message, used for automated sorting and routing of the package.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 1-9 characters variable; US addresses: 5 or 9 numeric digits (Mode 2); Non-US addresses: up to 6 alphanumeric characters (Mode 3)
- **Pattern/Regex:** US (Mode 2): `[0-9]{5}` or `[0-9]{9}`; Non-US (Mode 3): `[A-Za-z0-9]{1,6}`
- **Allowed Values:** Not restricted (actual postal code of destination)
- **Required:** yes — if the country does not have a postal code, leave the field empty

## Examples from Spec
- `303281483` (US ZIP+4, 9 digits)
- `841706672` (US ZIP+4, 9 digits)
- `51147` (Germany, numeric non-US)

## Position on Label
Encoded within MaxiCode barcode (primary message).

## Edge Cases & Notes
- Encode actual postal code without spaces or special characters (e.g., no dashes).
- Postal code in MaxiCode must match the one in the postal barcode.
- Include trailing spaces when value does not meet minimum length requirements.
- If greater than the character limit, truncate from the right.
- For all-numeric postal codes, use Mode 2 with up to 9 characters.

## Claude Confidence
HIGH — spec clearly defines format, length, and encoding rules with footnotes and examples

## Review Status
- [x] Reviewed by human