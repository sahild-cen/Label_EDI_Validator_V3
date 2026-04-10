# Field: ship_to_city_state_postal

## Display Name
Ship To City, State/Province, Postal Code

## Field Description
The city, state/province, and postal/ZIP code of the delivery destination.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- `MESA AZ 85206-4802`
- `ROSWELL GA 30076`
- `CHICAGO IL 60607`
- `KALAMAZOO MI 49009`
- `ALPHARETTA GA 30005-4177`
- `FLINT MI US 48502`
- `TORONTO ON M5X1K7`
- `WINDSOR ON N8N2M1`
- `CAGUAS 00725`
- `12099 BERLIN` (international)
- `710082 XIAN` (international)
- `TOKYO 1000004`
- `PARIS 75002`
- `51147 KOLN`
- `60386 FRANKFURT`
- `FRIEDBURG 61169`
- `28033 MADRID`
- `75008 PARIS`

## Position on Label
Middle section of the label in the ship-to address block, below the street address.

## Edge Cases & Notes
Format varies significantly by country. US uses CITY STATE ZIP+4 format. Canada uses CITY PROVINCE POSTALCODE. German/European addresses often place postal code before city. Japanese addresses may place city before postal code.

## Claude Confidence
HIGH — Consistently present in all label examples with clear regional format variations.

## Review Status
- [ ] Reviewed by human