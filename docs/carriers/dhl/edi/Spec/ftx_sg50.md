# Field: FTX (SG50 Invoice Line Item)

## Display Name
Free Text (Invoice Line Item — Description)

## Segment ID
FTX

## Required
yes

## Description
A segment to specify processable supplementary information relating to the line item (i.e. Line Item Description). Part of Segment Group 50. Up to 2 occurrences.

## Subfields

### text_subject_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** (LIN|AAA|Y|N)
- **Required:** yes
- **Description:** Text Subject code qualifier (element 4451). Use 'LIN' = Line Item indicator for GID (mandatory), 'AAA' = Line Item Description. For low value shipments to Singapore, 'Y' or 'N' indicates whether GST has been paid in exporting country.

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
- **Pattern/Regex:** .{1,512}
- **Required:** no
- **Description:** Free text value (element 4440 within C108 composite). Line Item Description text. Required when qualifier is 'AAA'.

## Edge Cases & Notes
Examples: FTX+LIN' (mandatory line item indicator), FTX+AAA+++DESCRIPTION LINE ITEM1' (line item description), FTX+Y' or FTX+N' (GST flag for Singapore). Each line item should have a GST flag/indicator for low value Singapore shipments. Max 512 characters.

## Claude Confidence
HIGH — spec provides multiple examples and detailed usage rules

## Review Status
- [ ] Reviewed by human