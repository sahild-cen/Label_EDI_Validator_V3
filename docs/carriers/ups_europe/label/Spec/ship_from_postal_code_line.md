# Field: ship_from_postal_code_line

## Display Name
Ship From Postal Code Line

## Field Description
The postal/ZIP code and city line for the shipper's address. May include city name, state/province, and postal code combined on one line.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
"POSTAL CODE LINE", "60386 FRANKFURT", "CHICAGO IL 60607", "KALAMAZOO MI 49009", "22525 HAMBURG", "1831 DIEGEM", "12099 BERLIN"

## Position on Label
Top-left area of label, in the ship-from address block below street address.

## ZPL Rendering
- **Typical Position:** Top-left, shipper address block
- **Font / Size:** 10 pt per spec
- **Field Prefix:** None — data value
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Format varies by country — US format includes state abbreviation and ZIP code, European format typically shows postal code followed by city name.

## Claude Confidence
HIGH — present in all label examples

## Review Status
- [ ] Reviewed by human