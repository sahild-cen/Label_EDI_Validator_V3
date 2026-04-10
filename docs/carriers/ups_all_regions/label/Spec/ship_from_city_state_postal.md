# Field: ship_from_city_state_postal

## Display Name
Ship From City, State/Province, Postal Code

## Field Description
The city, state/province, and postal/ZIP code of the shipping origin location.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- `CHICAGO IL 60607`
- `KALAMAZOO MI 49009`
- `MESA AZ 85206`
- `ROSWELL GA 30076`
- `LOS ANGELES CA 90001`
- `TIMONIUM MD 21093`
- `ALPHARETTA GA 30005`
- `MISSISSAUGA ON L4V1X5`
- `60386 FRANKFURT` (international format - postal code first)
- `75008 PARIS`
- `SHANGHAI 200120`

## Position on Label
Top section of the label in the ship-from address block, below the street address.

## Edge Cases & Notes
Format varies by country. US addresses use CITY STATE ZIP format. International addresses may place postal code before or after city name depending on country convention. For German origins, postal code precedes the city name.

## Claude Confidence
HIGH — Consistently present in all label examples with clear regional format variations.

## Review Status
- [ ] Reviewed by human