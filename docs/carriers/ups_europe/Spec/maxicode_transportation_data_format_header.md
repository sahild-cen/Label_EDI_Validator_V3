# Field: maxicode_transportation_data_format_header

## Display Name
Transportation Data Format Header (MaxiCode)

## Field Description
The format header that identifies the transportation data format type within the MaxiCode data string, always "01<GS>96".

## Format & Validation Rules
- **Data Type:** string (with non-printable characters)
- **Length:** Fixed
- **Pattern/Regex:** `01<GS>96`
- **Allowed Values:** `01<GS>96` (constant)
- **Required:** yes

## Examples from Spec
- `01<GS>96`

## Position on Label
Encoded within MaxiCode barcode (secondary message), immediately after the message header.

## Edge Cases & Notes
- `<GS>` is the group separator character (decimal 29).

## Claude Confidence
HIGH — spec consistently uses this constant value across all examples

## Review Status
- [x] Reviewed by human