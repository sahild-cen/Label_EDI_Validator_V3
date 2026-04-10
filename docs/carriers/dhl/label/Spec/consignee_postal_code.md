# Field: consignee_postal_code

## Display Name
Consignee Postal Code

## Field Description
The postal/ZIP code of the shipment destination/receiver. This is a critical sortation element.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable (depends on country, typically 3-10 characters)
- **Pattern/Regex:** Country-dependent
- **Allowed Values:** Valid postal codes for the destination country
- **Required:** conditional — required where postal code system exists

## Examples from Spec
No examples in spec.

## Position on Label
Within the consignee address block; may also appear separately in the routing section.

## Edge Cases & Notes
The destination postal code is used to determine the destination service area code and routing. Some countries do not have postal code systems.

## Claude Confidence
HIGH — Critical routing and address element.

## Review Status
- [ ] Reviewed by human