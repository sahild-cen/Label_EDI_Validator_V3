# Field: routing_code_human_readable

## Display Name
Routing Code (Human Readable)

## Field Description
Human-readable text representation of the routing barcode content, showing destination country, postcode, product code, and associated features.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable — mirrors routing barcode content
- **Pattern/Regex:** Same structure as routing barcode with parentheses around Data Identifier
- **Allowed Values:** Same as routing barcode content
- **Required:** yes — mandatory (appears alongside routing barcode)

## Examples from Spec
- "(2L)BE3500+11311002123456"
- "(2L)DE81541+05000000556677"

## Position on Label
Adjacent to the routing barcode, in the Routing Information segment.

## Edge Cases & Notes
- Parentheses around Data Identifier ("2L" or "403") appear ONLY in human-readable format, not in the barcode itself
- All routing information must appear in both human and bar-coded format

## Claude Confidence
HIGH — spec explicitly states both formats are required and provides examples

## Review Status
- [ ] Reviewed by human