# Field: FTX (SG25 Invoice Level)

## Display Name
Free Text (Invoice Level — Reason for Export)

## Segment ID
FTX

## Required
yes

## Description
A segment to specify free form or processable supplementary information within an Invoice, such as Reason for Export. Part of Segment Group 25 at Invoice Level.

## Subfields

### text_subject_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** (CEX|AAU)
- **Required:** yes
- **Description:** Text Subject code qualifier (element 4451). Use 'CEX' = Reason for Export (mandatory for all shipments), 'AAU' = Duty Free Import Remark (may be used with Return shipments).

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
- **Pattern/Regex:** .{1,5}
- **Required:** yes
- **Description:** Free text value (element 4440 within C108 composite). For Reason for Export values, refer to DHL Express Integrated Solution Reference Information.

## Edge Cases & Notes
Example: FTX+CEX+++C'. Elements 2 and 3 are not used (empty). 'CEX' is mandatory for all shipments. Max length of free text value is 5 characters at this level.

## Claude Confidence
HIGH — spec explicitly states mandatory usage and provides example

## Review Status
- [ ] Reviewed by human