# Field: ship_to_postal_code

## Display Name
Ship To Postal Code

## Field Description
The postal code of the destination (ship-to) address. This field is encoded in the MaxiCode primary message and must match the postal barcode value.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 1-9 characters; US addresses require 5 or 9 numeric characters (Mode 2); non-US addresses require up to 6 alphanumeric characters (Mode 3)
- **Pattern/Regex:** US: `^[0-9]{5}([0-9]{4})?$`; Non-US: `^[A-Z0-9]{1,6}$` (spaces padded to 6 chars)
- **Allowed Values:** Valid postal code for destination country
- **Required:** yes (if the country does not have a postal code, leave the field empty)

## Examples from Spec
- `303281483` (US ZIP+4, Atlanta GA)
- `841706672` (US ZIP+4, Salt Lake City UT)
- `51147` (Germany, Cologne)

## Position on Label
Encoded within MaxiCode and postal barcode. Also appears as part of the ship-to address block on the label.

## ZPL Rendering
- **Typical Position:** Within ship-to address block (middle/center of label)
- **Font / Size:** Not specified
- **Field Prefix:** None (part of address block)
- **ZPL Command:** ^FD (text field) for human-readable; encoded within ^BD (MaxiCode) and ^BC (postal barcode)

## Edge Cases & Notes
- Encode actual postal code value without spaces or special characters (e.g., no dashes).
- Postal codes must match between MaxiCode data string and postal barcode.
- Include trailing spaces for non-US postal codes when the value does not meet the 6-character minimum length.
- If greater than the character limit, truncate from the right.
- For all-numeric postal codes, use Mode 2 up to 9 characters; if greater than 9, truncate from right.

## Claude Confidence
HIGH — spec provides clear rules, examples, and edge cases for postal code encoding

## Review Status
- [ ] Reviewed by human