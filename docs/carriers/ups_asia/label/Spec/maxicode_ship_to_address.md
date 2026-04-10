# Field: maxicode_ship_to_address

## Display Name
Ship To Address (MaxiCode)

## Field Description
The street address of the consignee/recipient, encoded in the MaxiCode data string.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 1-35 characters (full address format) or 1-10 + FS + 1-8 (primary/secondary address format)
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** UPPERCASE characters only
- **Required:** yes

## Examples from Spec
- `123<FS>567` (validated address with primary address number 123 and secondary/suite number 567)
- `19 SOUTH ST` (non-validated full street address)
- `5 WALDSTRASSE` (international full street address)
- `1 MAIN ST` (Letter/Envelope example)

## Position on Label
Encoded within the MaxiCode barcode (secondary message).

## Edge Cases & Notes
- Two formats available: `(an 1...35)` for full street address, or `(an 1...10<FS>an1...8)` for primary + secondary address numbers separated by non-printable FS character.
- When using the primary/secondary format, Address Validation must be set to "Y".
- When address is blank or not available, a `<GS>` placeholder must be provided.

## Claude Confidence
HIGH — spec clearly defines both address formats with examples.

## Review Status
- [ ] Reviewed by human