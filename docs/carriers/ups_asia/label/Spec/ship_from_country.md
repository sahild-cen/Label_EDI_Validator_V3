# Field: ship_from_country

## Display Name
Ship From Country

## Field Description
The country name of the shipper/sender address, displayed in the ship-from address block.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted — full country name
- **Required:** yes — for international shipments

## Examples from Spec
"COUNTRY", "SINGAPORE", "UNITED STATES", "GERMANY", "ITALY"

## Position on Label
Upper left portion of the label, last line of the ship-from address block.

## Edge Cases & Notes
For domestic shipments, the country may be implied by the postal code line format. For international shipments it is always explicitly shown.

## Claude Confidence
HIGH — field appears consistently across international label examples

## Review Status
- [ ] Reviewed by human