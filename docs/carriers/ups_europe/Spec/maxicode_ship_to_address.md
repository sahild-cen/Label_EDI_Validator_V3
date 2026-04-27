# Field: maxicode_ship_to_address

## Display Name
Ship To Address (MaxiCode)

## Field Description
The street address of the destination/consignee encoded in the MaxiCode data string. Can be provided as a full street address or as primary and secondary address numbers separated by a field separator character.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 1-35 characters (full address format) or 1-10 + <FS> + 1-8 characters (primary/secondary address format)
- **Pattern/Regex:** Format A: `[A-Za-z0-9 ]{1,35}` or Format B: `[A-Za-z0-9]{1,10}<FS>[A-Za-z0-9]{1,8}`
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- `123<FS>567` (validated address with primary address number 123 and secondary address number 567)
- `19 SOUTH ST`
- `5 WALDSTRASSE`
- `1 MAIN ST`

## Position on Label
Encoded within MaxiCode barcode (secondary message).

## Edge Cases & Notes
- Format B (primary <FS> secondary) is allowed only for CASS-certified addresses within uncompressed MaxiCode. The Address Validation field must be set to `Y`.
- The address may be truncated if it reaches the character limit.
- If MaxiCode exceeds maximum length and Shipment ID has already been cleared, shorten the Ship-To Address field (delete only the characters still needed, preserving as much of the field as possible).
- <FS> is the non-printable field separator character (decimal 28).

## Claude Confidence
HIGH — spec provides two format options with clear rules and examples

## Review Status
- [x] Reviewed by human