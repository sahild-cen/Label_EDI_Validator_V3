# Field: service_title

## Display Name
Service Title

## Field Description
The name of the UPS service level used for the shipment, printed prominently on the label to identify the speed and type of delivery service.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** "UPS EXPRESS PLUS", "UPS EXPRESS", "UPS SAVER", "UPS EXPEDITED", "UPS EXPRESS FREIGHT", "UPS EXPRESS FREIGHT MIDDAY" and variants with delivery confirmation/import control
- **Required:** yes

## Examples from Spec
- `UPS EXPRESS PLUS`
- `UPS EXPRESS`
- `UPS SAVER`
- `UPS EXPEDITED`
- `UPS EXPRESS FREIGHT`

## Position on Label
Printed in the service name area, typically appearing prominently above or near the tracking number block.

## Edge Cases & Notes
The service title corresponds to the service indicator embedded in the tracking number. Saturday Delivery is only valid in United States and Canada.

## Claude Confidence
HIGH — Clearly shown on every label example in the spec.

## Review Status
- [ ] Reviewed by human