# Field: LOC (SG31 Invoice Level)

## Display Name
Place/Location Identification (Terms of Delivery)

## Segment ID
LOC

## Required
no

## Description
To specify a location related to the terms of Delivery. Place of Incoterms at the Invoice level. Part of Segment Group 31.

## Subfields

### location_function_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** 1
- **Required:** yes
- **Description:** Location function code qualifier (element 3227). Use '1' = Place of Incoterms.

### location_name_code
- **Element Position:** 2.1
- **Pattern/Regex:** [A-Z]{2,3}
- **Required:** yes
- **Description:** Location name code (element 3225 within C517 composite). DHL Express Service Area code for the location where the Incoterms were applied. List available on request.

### code_list_identification_code
- **Element Position:** 2.2
- **Pattern/Regex:** .*
- **Required:** no
- **Description:** Code List Identification Code (element 1131). Not used.

### code_list_responsible_agency_code
- **Element Position:** 2.3
- **Pattern/Regex:** .*
- **Required:** no
- **Description:** Code List Responsible agency Code (element 3055). Not used.

### location_name
- **Element Position:** 2.4
- **Pattern/Regex:** .{1,256}
- **Required:** yes
- **Description:** Location Name (element 3244). The location name text.

## Edge Cases & Notes
Example: LOC+1+AH:::liege'. Elements 2.2 and 2.3 are not used (empty between colons). DHL Express Service Area codes with corresponding Facility codes by location name, post code and country are available on request.

## Claude Confidence
HIGH — spec provides clear example and element definitions

## Review Status
- [ ] Reviewed by human