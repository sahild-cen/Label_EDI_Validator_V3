# Field: ship_to_postal_code_city

## Display Name
Ship To Postal Code and City

## Field Description
The postal code and city of the consignee/recipient destination.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- `60386  FRANKFURT`
- `TOKYO  1000004`
- `22525 HAMBURG`

## Position on Label
Ship-to address block, after street address.

## ZPL Rendering
- **Typical Position:** Ship-To block
- **Font / Size:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Format varies by country — some have postal code before city, others after.

## Claude Confidence
HIGH — shown on all label examples

## Review Status
- [ ] Reviewed by human