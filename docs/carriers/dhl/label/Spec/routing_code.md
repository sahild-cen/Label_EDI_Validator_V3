# Field: routing_code

## Display Name
Routing Code

## Field Description
A composite routing identifier used by DHL for operational sorting and routing within the global network. This typically combines origin, destination, service area, and facility codes into a single routing string displayed on the label.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable, typically 8-20 characters
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** DHL system-generated routing codes
- **Required:** yes

## Examples from Spec
No examples in extracted spec text.

## ZPL Rendering
- **Typical Position:** upper portion of label, often in a large bold font; may appear in dedicated routing code box
- **Font / Size:** Large, bold; designed for quick visual identification during sorting
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
The routing code is a key operational field that DHL uses for hub sorting. It may include a combination of destination country, service area, facility code, and sort code segments. This field is system-generated and must not be manually modified.

## Claude Confidence
MEDIUM — known DHL operational field

## Review Status
- [ ] Reviewed by human