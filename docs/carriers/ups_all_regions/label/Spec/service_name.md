# Field: service_name

## Display Name
Service Name / UPS Service

## Field Description
The name of the UPS service being used for the shipment, printed prominently on the label to identify the level of service.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** UPS EXPRESS FREIGHT, UPS EXPRESS FREIGHT MIDDAY, UPS SUREPOST, UPS STANDARD, UPS NEXT DAY AIR EARLY, UPS NEXT DAY AIR, UPS EXPRESS, UPS EXPRESS PLUS, UPS SAVER, UPS EXPRESS 12:00, UPS ECONOMY DDP, UPS ECONOMY DDU, and others per service code tables
- **Required:** yes

## Examples from Spec
- `UPS EXPRESS FREIGHT`
- `UPS SUREPOST`
- `UPS STANDARD`
- `UPS NEXT DAY AIR EARLY`
- `UPS NEXT DAY AIR`
- `UPS EXPRESS`

## Position on Label
Printed in the UPS Service box area of the label, typically in the middle section.

## Edge Cases & Notes
The service name on the label must correspond to the correct service indicator and MaxiCode class of service code. For UPS Trade Direct shipments, additional text like "UPS Trade Direct™ - UPS Worldwide Express Freight™" may need to precede the consignee name.

## Claude Confidence
HIGH — Multiple examples clearly shown on sample labels throughout the spec.

## Review Status
- [ ] Reviewed by human