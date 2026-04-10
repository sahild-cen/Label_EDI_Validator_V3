# Field: maxicode_ship_to_postal_code

## Display Name
Ship To Postal Code (MaxiCode)

## Field Description
The destination postal code encoded in the MaxiCode data string as part of the primary message. Used for automated sortation.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 1-9 characters (numeric Mode 2) or 1-6 characters (alphanumeric Mode 3)
- **Pattern/Regex:** Not specified in spec (varies by country)
- **Allowed Values:** Valid postal codes without spaces or special characters
- **Required:** yes

## Examples from Spec
- `303281483` (U.S. ZIP+4, Mode 2)
- `841706672` (U.S. ZIP+4, Mode 2)
- `51147` (Germany, Mode 2)

## Position on Label
Encoded within the MaxiCode barcode (primary message, first data field).

## Edge Cases & Notes
- For all-numeric postal codes, use Mode 2 (up to 9 characters). If greater than 9, truncate from right.
- For alphanumeric postal codes, use Mode 3 (up to 6 characters). If greater than 6, truncate from right.
- Encode without spaces or special characters such as dashes.
- Must match the postal code encoded in the postal barcode.
- Some software providers interpret Mode 2 exclusively for U.S. destinations and Mode 3 for non-U.S., but this is not strictly correct per spec.

## Claude Confidence
HIGH — spec clearly defines format, mode selection, and provides multiple examples.

## Review Status
- [ ] Reviewed by human