# Field: service_area_code_origin

## Display Name
Service Area Code of Origin

## Field Description
A 3-digit code identifying the locally defined and globally recognized area where DHL services are provided at the origin. This data is maintained in DHL Global Reference Databases.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 3 characters (exact)
- **Pattern/Regex:** [A-Z]{3}
- **Allowed Values:** DHL Service Area Codes as maintained in Global Reference Databases
- **Required:** yes

## Examples from Spec
No specific examples provided in extracted text, but described as "3-digit, upper-case letter" code.

## ZPL Rendering
- **Typical Position:** between Ship From and Ship To address sections
- **Font / Size:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
This is a globally recognized code maintained centrally. It is part of the origin identification on the label.

## Claude Confidence
HIGH — clearly specified as mandatory with format

## Review Status
- [ ] Reviewed by human