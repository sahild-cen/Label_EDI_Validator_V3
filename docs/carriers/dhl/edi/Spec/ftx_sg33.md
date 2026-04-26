# Field: FTX (SG33 Invoice Level)

## Display Name
Free Text (Governmental Requirements — Trading Transaction Type)

## Segment ID
FTX

## Required
yes

## Description
A segment to specify free form or processable supplementary information within an Invoice, such as Trading Transaction Type. Part of Segment Group 33 at Invoice Level.

## Subfields

### text_subject_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** AAI
- **Required:** yes
- **Description:** Text Subject code qualifier (element 4451). Use 'AAI' = Trading Transaction Type.

### free_text_function_code
- **Element Position:** 2
- **Pattern/Regex:** .*
- **Required:** no
- **Description:** Free text function code (element 4453). Not used.

### text_reference
- **Element Position:** 3
- **Pattern/Regex:** .*
- **Required:** no
- **Description:** TEXT REFERENCE composite (C107). Not used.

### free_text_value
- **Element Position:** 4.1
- **Pattern/Regex:** .{1,15}
- **Required:** yes
- **Description:** Free text value (element 4440 within C108 composite). Trading Transaction Type value. Full list available from DHL Express.

## Edge Cases & Notes
Example: FTX+AAI+++Commercial'. Elements 2 and 3 are not used (empty). Max length is 15 characters at this level.

## Claude Confidence
HIGH — spec clearly defines the qualifier and provides example

## Review Status
- [ ] Reviewed by human