# Field: ship_from_country

## Display Name
Ship From Country

## Field Description
The country of the shipping origin, typically displayed for international shipments.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Full country name (e.g., "UNITED STATES", "GERMANY", "FRANCE", "CHINA")
- **Required:** conditional — required for international shipments

## Examples from Spec
- `UNITED STATES`
- `GERMANY`
- `FRANCE`
- `CHINA`

## Position on Label
Top section of the label in the ship-from address block, on the line below the city/state/postal code.

## Edge Cases & Notes
For domestic US shipments, the country may be omitted from the ship-from section. For international shipments, the full country name is typically included.

## Claude Confidence
HIGH — Consistently shown for international shipments.

## Review Status
- [ ] Reviewed by human