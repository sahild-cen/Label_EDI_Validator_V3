# Field: shipper_country

## Display Name
Shipper Country

## Field Description
The country of the shipment origin/sender.

## Format & Validation Rules
- **Data Type:** string
- **Length:** 2 characters (ISO code) or full country name
- **Pattern/Regex:** ISO 3166-1 alpha-2 code
- **Allowed Values:** Valid ISO country codes
- **Required:** yes

## Examples from Spec
No examples in spec.

## Position on Label
Within the shipper address block.

## Edge Cases & Notes
International shipments typically require the full country name in addition to or instead of the ISO code.

## Claude Confidence
HIGH — Standard required element on international DHL labels.

## Review Status
- [ ] Reviewed by human