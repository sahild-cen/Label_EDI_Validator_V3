# Field: ship_to_country

## Display Name
Ship To Country

## Field Description
The country of the delivery destination, displayed for international shipments.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Full country name (e.g., "GERMANY", "JAPAN", "CHINA PEOPLES REPUBLIC OF", "CANADA", "FRANCE", "SPAIN", "UNITED STATES", "PUERTO RICO")
- **Required:** conditional — required for international shipments

## Examples from Spec
- `GERMANY`
- `JAPAN`
- `CHINA PEOPLES REPUBLIC OF`
- `CANADA`
- `FRANCE`
- `SPAIN`
- `UNITED STATES`
- `PUERTO RICO`

## Position on Label
Middle section of the label in the ship-to address block, below the city/postal code line.

## Edge Cases & Notes
Country name may use non-standard formatting (e.g., "CHINA PEOPLES REPUBLIC OF" instead of "People's Republic of China"). For domestic US shipments, the country may be omitted.

## Claude Confidence
HIGH — Consistently shown on international label examples.

## Review Status
- [ ] Reviewed by human