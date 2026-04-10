# Field: origin_service_area_code

## Display Name
Origin Service Area Code

## Field Description
A three-character code identifying the DHL service area (facility/station) at the origin that processes the shipment.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 3
- **Pattern/Regex:** `^[A-Z0-9]{3}$`
- **Allowed Values:** DHL-defined service area codes
- **Required:** yes

## Examples from Spec
No examples in spec.

## Position on Label
Typically shown in the routing information area of the label.

## Edge Cases & Notes
This code is determined by DHL based on the shipper's pickup address/postal code. It is used in the routing string and sortation logic.

## Claude Confidence
HIGH — Standard routing element on DHL Express labels.

## Review Status
- [ ] Reviewed by human