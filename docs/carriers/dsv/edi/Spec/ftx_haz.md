# Field: FTX (Hazard Information)

## Display Name
Free Text - Hazard Information

## Segment ID
FTX

## Required
no

## Description
Free text segment within DGS group (SG33) for Technical Name and International Technical Name of dangerous goods.

## Subfields

### text_subject_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** HAZ
- **Required:** yes
- **Description:** Text subject code qualifier — HAZ = Hazard information

### free_text_function_code
- **Element Position:** 2
- **Pattern/Regex:** .{1,3}
- **Required:** no
- **Description:** Free text function code

### text_literal_1
- **Element Position:** 4.1
- **Pattern/Regex:** .{1,512}
- **Required:** yes
- **Description:** Technical Name (first sub-component of C108)

### text_literal_2
- **Element Position:** 4.2
- **Pattern/Regex:** .{1,512}
- **Required:** no
- **Description:** International Technical Name

## Edge Cases & Notes
Text lines 3-5 are not used. Example: FTX+HAZ+++BISPHENOL A EPOXY RESIN:BISPHENOL A EPOXY RESIN'

## Claude Confidence
HIGH — spec clearly defines all elements

## Review Status
- [ ] Reviewed by human