# Field: shipper_postal_code

## Display Name
Shipper Postal Code

## Field Description
The postal/ZIP code of the shipment origin/sender.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable (depends on country, typically 3-10 characters)
- **Pattern/Regex:** Country-dependent
- **Allowed Values:** Valid postal codes for the origin country
- **Required:** conditional — required where postal code system exists

## Examples from Spec
No examples in spec.

## Position on Label
Within the shipper address block.

## Edge Cases & Notes
Some countries do not have postal code systems. Format varies significantly by country.

## Claude Confidence
HIGH — Standard address component.

## Review Status
- [ ] Reviewed by human