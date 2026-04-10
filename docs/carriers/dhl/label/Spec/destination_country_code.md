# Field: destination_country_code

## Display Name
Destination Country Code

## Field Description
The ISO 2-letter country code for the shipment destination, displayed prominently on the label for sortation purposes.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 2
- **Pattern/Regex:** `^[A-Z]{2}$`
- **Allowed Values:** ISO 3166-1 alpha-2 country codes
- **Required:** yes

## Examples from Spec
No examples in spec.

## Position on Label
Often displayed prominently in the routing/sortation area of the label, separate from the address block.

## Edge Cases & Notes
This is a key sortation element displayed in large text for quick visual identification by handlers.

## Claude Confidence
HIGH — Standard DHL label element for international shipments.

## Review Status
- [ ] Reviewed by human