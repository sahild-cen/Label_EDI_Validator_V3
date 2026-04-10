# Field: shipment_number

## Display Name
Shipment Number (SHP#)

## Field Description
The shipment identification number displayed on the label, prefixed with "SHP #:".

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** `SHP #: [A-Z0-9]+ [A-Z0-9]+`
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- "SHP #: 1X2X3X 19K"
- "SHP #: 1X2X3X 9VM"

## Position on Label
On the World Ease label, appears in the shipper information area.

## Edge Cases & Notes
This appears to be the same as or derived from the GCC# / Shipment Number used for customs clearance purposes.

## Claude Confidence
MEDIUM — visible in label examples but not explicitly described in the extracted spec text with format rules

## Review Status
- [ ] Reviewed by human