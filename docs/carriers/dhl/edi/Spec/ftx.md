# Field: FTX

## Display Name
Free Text

## Segment ID
FTX

## Required
no

## Description
A segment used to indicate any additional information such as business party trader type for consignor, consignment remarks, reason for export, custom remarks/instructions, or dangerous goods technical name.

## Subfields

### text_subject_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** [A-Z]{3}
- **Required:** yes
- **Description:** Text subject code qualifier — identifies the type of free text (e.g. AAA = general remarks, AAU = duty free import remarks, CCI = custom remarks/instructions)

### free_text_function_code
- **Element Position:** 2
- **Pattern/Regex:** \d{1,3}
- **Required:** no
- **Description:** Free text function code

### text_reference_code
- **Element Position:** 3
- **Pattern/Regex:** .{1,17}
- **Required:** no
- **Description:** Text reference — composite element for coded text reference

### text_literal_1
- **Element Position:** 4
- **Pattern/Regex:** .{0,512}
- **Required:** no
- **Description:** Free text value — first line of free text (composite, may contain multiple sub-elements separated by colons for additional lines)

### text_literal_2
- **Element Position:** 4.1
- **Pattern/Regex:** .{0,512}
- **Required:** no
- **Description:** Free text value — second line of free text (composite sub-element)

### text_literal_3
- **Element Position:** 4.2
- **Pattern/Regex:** .{0,512}
- **Required:** no
- **Description:** Free text value — third line of free text (composite sub-element)

### text_literal_4
- **Element Position:** 4.3
- **Pattern/Regex:** .{0,512}
- **Required:** no
- **Description:** Free text value — fourth line of free text (composite sub-element)

### text_literal_5
- **Element Position:** 4.4
- **Pattern/Regex:** .{0,512}
- **Required:** no
- **Description:** Free text value — fifth line of free text (composite sub-element)

### language_name_code
- **Element Position:** 5
- **Pattern/Regex:** [A-Z]{2,3}
- **Required:** no
- **Description:** Language name code — ISO language code

## Edge Cases & Notes
FTX appears at multiple levels: Header (max 3), Shipment SG25 (max 99), Invoice SG25 (max 9), Invoice SG33 (max 9), Invoice Line Item SG50 (max 1), SG49 (max 1), and SG65 for DGS (max 1). Qualifier CCI is used for Custom Remarks/Instructions if DHL renders Invoice Image. Qualifier AAU is used for Duty Free Import Remarks (Return Shipments).

## Claude Confidence
HIGH — spec describes FTX usage extensively across multiple levels

## Review Status
- [ ] Reviewed by human