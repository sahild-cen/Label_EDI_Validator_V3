# Field: DOC

## Display Name
Document Message Details

## Segment ID
DOC

## Required
no

## Description
Specifies document or message details, particularly for sea transport documentation types.

## Subfields

### document_name_code
- **Element Position:** 1.1
- **Pattern/Regex:** (706|712|710|NON)
- **Required:** no
- **Description:** Document name code (C002/1001). Valid codes: 706=Bill of lading original, 712=Non-negotiable maritime transport document (generic), 710=Sea waybill, NON=Non-controlled shipment.

### document_name_code_list
- **Element Position:** 1.2
- **Pattern/Regex:** an..17
- **Required:** no
- **Description:** Code list identification code (C002/1131). Not used.

### document_name_agency
- **Element Position:** 1.3
- **Pattern/Regex:** an..3
- **Required:** no
- **Description:** Code list responsible agency code (C002/3055). Not used.

### document_name
- **Element Position:** 1.4
- **Pattern/Regex:** an..35
- **Required:** no
- **Description:** Document name (C002/1000). Not used.

### document_identifier
- **Element Position:** 2.1
- **Pattern/Regex:** an..70
- **Required:** no
- **Description:** Document identifier (C503/1004). Not used.

### document_status_code
- **Element Position:** 2.2
- **Pattern/Regex:** an..3
- **Required:** no
- **Description:** Document status code (C503/1373). Not used.

### document_source_description
- **Element Position:** 2.3
- **Pattern/Regex:** an..70
- **Required:** no
- **Description:** Document source description (C503/1366). Not used.

### language_name_code
- **Element Position:** 2.4
- **Pattern/Regex:** an..3
- **Required:** no
- **Description:** Language name code (C503/3453). Not used.

### version_identifier
- **Element Position:** 2.5
- **Pattern/Regex:** an..9
- **Required:** no
- **Description:** Version identifier (C503/1056). Not used.

### revision_identifier
- **Element Position:** 2.6
- **Pattern/Regex:** an..6
- **Required:** no
- **Description:** Revision identifier (C503/1060). Not used.

### communication_medium_type_code
- **Element Position:** 3
- **Pattern/Regex:** an..3
- **Required:** no
- **Description:** Communication medium type code (3153). Not used.

### document_copies_required_quantity
- **Element Position:** 4
- **Pattern/Regex:** n..2
- **Required:** no
- **Description:** Document copies required quantity (1220). Number of document copies needed.

### document_originals_required_quantity
- **Element Position:** 5
- **Pattern/Regex:** n..2
- **Required:** no
- **Description:** Document originals required quantity (1218). Number of original documents needed.

## Edge Cases & Notes
DOC can occur up to 9 times. Examples: DOC+706+++1' (Bill of lading, 1 original), DOC+710+++2+1' (Sea waybill, 2 copies, 1 original), DOC+712+++2+1' (Non-negotiable maritime transport document), DOC+NON' (Non-controlled shipment).

## Claude Confidence
HIGH — spec clearly defines the structure and valid codes

## Review Status
- [ ] Reviewed by human