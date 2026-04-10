# Field: ups_pak_indicator

## Display Name
UPS PAK Indicator

## Field Description
When a UPS PAK is used as the packaging type, the weight and PAK indicator must replace the standard package weight field. One decimal point must be added to the weight when using pounds.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Weight value + space + "KG" or "LBS" + space + "PAK"
- **Allowed Values:** Weight followed by "PAK"
- **Required:** conditional — only when UPS PAK packaging is used

## Examples from Spec
- `5.5 KG PAK`
- `2.4 LBS PAK`

## Position on Label
Replaces the package weight field in the top right corner (Package Information Block).

## ZPL Rendering
- **Typical Position:** Top-right corner, same position as package weight
- **Font / Size:** 12pt bold
- **Field Prefix:** None — displayed as weight value with "PAK" suffix
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
- One decimal point must be added to the weight when using pounds.
- Replaces the standard package weight field entirely.

## Claude Confidence
HIGH — spec provides clear format rules and examples

## Review Status
- [ ] Reviewed by human