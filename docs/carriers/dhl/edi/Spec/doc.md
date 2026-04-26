# Field: DOC

## Display Name
Document/Message Details

## Segment ID
DOC

## Required
yes

## Description
A segment to indicate accompanying documents for customs clearance, such as invoice number or customs documents.

## Subfields

### document_name_code
- **Element Position:** 1
- **Pattern/Regex:** .{1,3}
- **Required:** yes
- **Description:** Document name code — identifies the type of document (composite element)

### document_name_code_list
- **Element Position:** 1.1
- **Pattern/Regex:** .{0,17}
- **Required:** no
- **Description:** Code list identification code (composite sub-element)

### document_name_responsible_agency
- **Element Position:** 1.2
- **Pattern/Regex:** .{0,3}
- **Required:** no
- **Description:** Code list responsible agency code (composite sub-element)

### document_identifier
- **Element Position:** 2
- **Pattern/Regex:** .{0,35}
- **Required:** no
- **Description:** Document identifier — the document or invoice number (composite element)

### document_source_description
- **Element Position:** 3
- **Pattern/Regex:** .{0,70}
- **Required:** no
- **Description:** Document source description

## Edge Cases & Notes
DOC appears in SG34 at Shipment level (max 1), Invoice level (max 1), and SG56 at Invoice Line Item level (max 9). Accompanied by DTM to indicate date/time related to the document.

## Claude Confidence
HIGH — spec describes DOC clearly

## Review Status
- [ ] Reviewed by human