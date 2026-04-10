# Field: accompanying_documents

## Display Name
Accompanying Documents for Customs Clearance

## Field Description
A segment (SG34 - DOC) to indicate accompanying documents for customs clearance at both shipment and invoice levels. At invoice level, includes Invoice Number and Customs Documents.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — at SG34, 1 occurrence of DOC per SG34 group

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
DTM segment follows DOC to indicate date and time related to the document (e.g., invoice date). Appears at both shipment and invoice levels.

## Claude Confidence
MEDIUM — Clearly described in both shipment and invoice declarations.

## Review Status
- [ ] Reviewed by human