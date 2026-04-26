# Field: routing_code_human_readable

## Display Name
Routing Code (Human Readable)

## Field Description
The human-readable representation of the routing information printed on the label alongside the routing barcode. All routing information appears in both human-readable and barcoded format. The human-readable version includes parentheses around the Data Identifier which do not appear in the barcode itself.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** Variable
- **Pattern/Regex:** `\(2L\)[A-Z]{2}.{0,12}\+\d{8}.*` or `\(403\)\d{3}.{0,12}\+\d{8}.*`
- **Allowed Values:** Must match routing barcode content with added parentheses
- **Required:** yes — when routing barcode is printed

## Examples from Spec
- `(2L)BE3500+11311002123456`
- `(2L)DE81541+05000000556677`
- `(2L)CH3000+57520001`
- `(2L)NL1023FG+48101081`

## ZPL Rendering
- **Typical Position:** Directly below or above the routing barcode
- **Font / Size:** Not specified
- **Field Prefix:** Parentheses around Data Identifier: "(2L)" or "(403)"
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
- Parentheses around Data Identifier are ONLY in human-readable form, not encoded in the barcode.
- Must always match the data encoded in the routing barcode.

## Claude Confidence
HIGH — spec explicitly states all routing info appears in both human and barcoded format

## Review Status
- [ ] Reviewed by human