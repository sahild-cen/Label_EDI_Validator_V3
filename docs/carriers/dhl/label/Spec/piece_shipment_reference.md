# Field: piece_shipment_reference

## Display Name
Piece / Shipment Reference

## Field Description
Optional customer-defined reference identifier(s) for a package, such as reference codes consisting of alphanumeric characters. These are qualified by specific Reference Type Codes (ex-Reference Qualifiers) that give them specific meaning. May be printed on the label when DHL has received the references with the transport order.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable — all formats supported by the solution agreed with DHL
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted — customer-managed identifiers
- **Required:** no (optional)

## Examples from Spec
- Reference Type Codes qualify the references (e.g., Shipper's Reference is one type)
- Tax IDs (e.g., Brazil CNPJ/CPF, IE/RG) can be represented as Shipment References with associated Reference Types

## ZPL Rendering
- **Typical Position:** shipment information segment
- **Font / Size:** Not specified
- **Field Prefix:** May include reference type qualifier text
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
- Refers to DHL EXPRESS Piece/Shipment Reference Standard for Reference Type Codes.
- Can include Tax IDs when represented as a Shipment Reference with associated Reference Type.
- All formats supported by the agreed solution can be printed on the label.

## Claude Confidence
MEDIUM — described as optional with flexible format; references external standard for detail

## Review Status
- [ ] Reviewed by human