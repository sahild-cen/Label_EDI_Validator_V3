# Field: service_area_code_of_origin

## Display Name
Service Area Code of Origin

## Field Description
A 3-digit, upper-case letter code representing a locally defined and globally recognized area where DHL services are provided.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** exactly 3 characters
- **Pattern/Regex:** `[A-Z]{3}`
- **Allowed Values:** Maintained in DHL Global Reference Databases
- **Required:** yes — mandatory

## Examples from Spec
No specific examples given in extracted text, though "SIN" (Singapore) is referenced in the Destination Facility Code context.

## Position on Label
Dedicated segment on the transport label (section referenced near the Ship From address area).

## Edge Cases & Notes
- Data is maintained in DHL Global Reference Databases
- This is a 3-digit code consisting of upper-case letters only

## Claude Confidence
HIGH — spec clearly defines format and mandatory status

## Review Status
- [ ] Reviewed by human