# Field: LOC (SG50 Invoice Line Item)

## Display Name
Place/Location Identification (Line Item Country of Manufacture)

## Segment ID
LOC

## Required
yes

## Description
A segment to specify a country associated with a line item (i.e. Line Item Country of Manufacture). Part of Segment Group 50 at Invoice Line Item level.

## Subfields

### location_function_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** 27
- **Required:** yes
- **Description:** Location function code qualifier (element 3227). Use '27' = Line Item Country of Manufacture.

### location_name_code
- **Element Position:** 2.1
- **Pattern/Regex:** [A-Z]{2,3}
- **Required:** yes
- **Description:** Location name code (element 3225 within C517 composite). Codes available on request from Sales Representative.

### code_list_identification_code
- **Element Position:** 2.2
- **Pattern/Regex:** .*
- **Required:** no
- **Description:** Code List Identification Code (element 1131). Not used in example but present in structure.

### code_list_responsible_agency_code
- **Element Position:** 2.3
- **Pattern/Regex:** \d{1,3}
- **Required:** no
- **Description:** Code List Responsible agency Code (element 3055). Example shows value '6'.

## Edge Cases & Notes
Example: LOC+27+AMS::6'. Elements 2.2 is empty in the example.

## Claude Confidence
MEDIUM — spec shows example with agency code '6' but does not elaborate on its meaning

## Review Status
- [ ] Reviewed by human