# Field: consignee_country

## Display Name
Consignee Country (Destination Country)

## Field Description
The country of the shipment destination/receiver.

## Format & Validation Rules
- **Data Type:** string
- **Length:** 2 characters (ISO code) or full country name
- **Pattern/Regex:** ISO 3166-1 alpha-2 code
- **Allowed Values:** Valid ISO country codes
- **Required:** yes

## Examples from Spec
No examples in spec.

## Position on Label
Within the consignee address block and potentially in the routing area.

## Edge Cases & Notes
International shipments require the full country name. The destination country drives customs requirements and service availability.

## Claude Confidence
HIGH — Standard required element.

## Review Status
- [ ] Reviewed by human