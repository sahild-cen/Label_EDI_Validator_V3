# Field: destination_service_area_code

## Display Name
Destination Service Area Code

## Field Description
A three-character code identifying the DHL service area (facility/station) at the destination responsible for final delivery of the shipment.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 3
- **Pattern/Regex:** `^[A-Z0-9]{3}$`
- **Allowed Values:** DHL-defined service area codes
- **Required:** yes

## Examples from Spec
No examples in spec.

## Position on Label
Prominently displayed in the routing/destination area of the label, often in large font.

## Edge Cases & Notes
This is a critical sortation element. It is determined by DHL routing tables based on the destination postal code and country. It often appears as part of the routing code string.

## Claude Confidence
HIGH — Core routing element on DHL labels.

## Review Status
- [ ] Reviewed by human