# Field: maxicode_barcode

## Display Name
MaxiCode Barcode

## Field Description
A 2D MaxiCode barcode that encodes shipment information including tracking number, class of service, routing data, and other shipment details. Used by UPS for automated sorting and processing.

## Format & Validation Rules
- **Data Type:** barcode (2D MaxiCode symbology)
- **Length:** variable (per MaxiCode specification)
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Encodes class of service, tracking number, weight, and routing information
- **Required:** yes

## Examples from Spec
No examples in spec (barcode images shown on sample labels).

## Position on Label
Printed on the shipping label in a designated area (visible on sample labels).

## Edge Cases & Notes
For UPS Worldwide Economy labels, the MaxiCode's weight field must contain "1". The class of service encoded must match the service indicator used. The MaxiCode is referenced throughout the spec with specific class of service codes for each service type.

## Claude Confidence
HIGH — Referenced extensively throughout spec with class of service code tables.

## Review Status
- [ ] Reviewed by human