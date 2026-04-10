# Field: piece_shipment_reference

## Display Name
Piece / Shipment Reference

## Field Description
Customer-defined identifier(s) for a package, such as reference codes consisting of alphanumeric characters. These are qualified by specific Reference Type Codes that give them specific meaning.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable — all formats supported by the solution agreed with DHL
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted — under customer's responsibility to manage
- **Required:** no — optional

## Examples from Spec
No specific examples in spec beyond mentioning "reference codes, which consist of sets of alphanumeric chars."

## Position on Label
Printed in the Shipment Information section of the label.

## Edge Cases & Notes
- Ideally printed when DHL has received those references with the transport order
- Qualified by Reference Type Codes (ex-Reference Qualifiers) per DHL EXPRESS Piece/Shipment Reference Standard
- Tax IDs (e.g., Brazil CNPJ/CPF) can also be represented as a Shipment Reference with associated Reference Type

## Claude Confidence
MEDIUM — spec describes the field conceptually but provides limited format detail

## Review Status
- [ ] Reviewed by human