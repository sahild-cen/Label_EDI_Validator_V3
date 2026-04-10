# Field: ship_from_postal_code_line

## Display Name
Ship From Postal Code Line

## Field Description
The city, state/province, and postal code line for the shipper's address. For international shipments, may also include the country name.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- `CHICAGO IL  60607` (domestic US)
- `60386  FRANKFURT` (Germany origin)
- `ROSWELL GA  30076`
- `KALAMAZOO MI  49009`
- `MESA AZ 85206`
- `MISSISSAUGA ON L4V1X5` (Canada)

## Position on Label
Printed in the ship-from address block, below the street address.

## Edge Cases & Notes
Format varies by country. US format is City + State + ZIP. International formats may have postal code before city name.

## Claude Confidence
HIGH — Multiple examples shown across various label types.

## Review Status
- [ ] Reviewed by human