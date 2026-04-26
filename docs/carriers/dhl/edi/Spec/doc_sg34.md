# Field: DOC (SG34 Invoice Level)

## Display Name
Document Message Details (Invoice Level)

## Segment ID
DOC

## Required
yes

## Description
A segment to indicate accompanying documents for customs clearance (i.e. Invoice Number, Customs Document). Part of Segment Group 34 at Invoice Level. Up to 9 occurrences.

## Subfields

### document_name_code
- **Element Position:** 1.1
- **Pattern/Regex:** (380|325|861|[A-Z0-9]{1,3})
- **Required:** yes
- **Description:** Document name code (element 1001 within C002 composite). Use '380' = Commercial Invoice, '325' = Proforma Invoice, '861' = Certificate of Origin. Full list available from DHL Express.

### document_identifier
- **Element Position:** 2.1
- **Pattern/Regex:** .{1,35}
- **Required:** yes
- **Description:** Document identifier (element 1004 within C503 composite). Related document number.

## Edge Cases & Notes
Examples: DOC+861+COO1111199' (Certificate of Origin), DOC+380+INVNO11199' (Commercial Invoice). This segment is only to be used for identifying export-documents for dutiable shipments for customs clearance.

## Claude Confidence
HIGH — spec provides clear examples and element definitions

## Review Status
- [ ] Reviewed by human