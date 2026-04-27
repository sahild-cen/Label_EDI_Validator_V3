# Field: maxicode_message_header

## Display Name
MaxiCode Message Header

## Field Description
The ANSI message header that begins the MaxiCode data string, identifying the start of the structured data format.

## Format & Validation Rules
- **Data Type:** string (with non-printable characters)
- **Length:** Fixed
- **Pattern/Regex:** `[)><RS>`
- **Allowed Values:** `[)><RS>` (constant)
- **Required:** yes

## Examples from Spec
- `[)><RS>`

## Position on Label
First element in MaxiCode barcode data string.

## Edge Cases & Notes
- `<RS>` is the record separator character (decimal 30), a non-printable character.

## Claude Confidence
HIGH — spec clearly defines this as the constant message header

## Review Status
- [x] Reviewed by human