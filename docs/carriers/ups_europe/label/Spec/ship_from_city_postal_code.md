# Field: ship_from_city_postal_code

## Display Name
Ship From City and Postal Code

## Field Description
The city and postal code of the shipper/sender location.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- `1831 DIEGEM`
- `7317 STEINSEL`
- `92140 CLAMART`

## Position on Label
Top-left area of the label, within the ship-from address block, after street address.

## ZPL Rendering
- **Typical Position:** Top-left, within ship-from block
- **Font / Size:** Not specified
- **Field Prefix:** None (part of address block)
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Format varies by country. European format typically places postal code before city name.

## Claude Confidence
HIGH — Multiple examples shown in label diagrams

## Review Status
- [ ] Reviewed by human