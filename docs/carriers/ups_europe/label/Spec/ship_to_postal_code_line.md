# Field: ship_to_postal_code_line

## Display Name
Ship To Postal Code Line

## Field Description
The postal/ZIP code and city line for the destination address. May include city name, state/province, and postal code.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
"POSTAL CODE LINE", "60386 FRANKFURT", "PARIS 75002", "TOKYO 1000004", "MESA AZ 85206-4802", "22525 HAMBURG", "12099 BERLIN", "WINDSOR ON N8N2M1", "75008 PARIS", "9000 GHENT", "2970 LUXEMBOUG CITY"

## Position on Label
Middle-left area of label, in the ship-to address block near the bottom of the address.

## ZPL Rendering
- **Typical Position:** Middle-left, ship-to address block
- **Font / Size:** 12 pt Bold per spec
- **Field Prefix:** None — data value
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Format varies by country. This line may be the last line before the country in the ship-to block.

## Claude Confidence
HIGH — present in all label examples

## Review Status
- [ ] Reviewed by human