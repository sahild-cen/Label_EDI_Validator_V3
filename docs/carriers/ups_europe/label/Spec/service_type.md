# Field: service_type

## Display Name
Service Type

## Field Description
The UPS service level for the shipment. Referenced throughout the spec as driving label requirements including service icons and service indicators. Services include UPS Standard, UPS Express, UPS Expedited, and others.

## Format & Validation Rules
- **Data Type:** string
- **Length:** Variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** UPS Standard, UPS Express, UPS Expedited, and other UPS General Service Offerings
- **Required:** yes

## Examples from Spec
From the label certification table: "UPS® Standard, UPS Express, UPS Expedited, etc."

## Position on Label
Represented by the Service Icon and encoded in the Service Indicator (positions 9-10 of tracking number).

## ZPL Rendering
- **Typical Position:** Upper portion of label as service icon graphic; may also appear as text
- **Font / Size:** Not specified
- **Field Prefix:** None — represented as graphic icon
- **ZPL Command:** ^GFA or ^IM (graphic for service icon)

## Edge Cases & Notes
- Adding a new UPS service requires label re-certification.
- The certification process requires labels to be distributed across all supported services (e.g., 2 services = 2 sets of 5 labels each; 3 services = sets of 3/3/4; 5 services = 2 labels each).

## Claude Confidence
MEDIUM — Service types are referenced but detailed list of allowed values and rendering specs not in extracted text.

## Review Status
- [ ] Reviewed by human