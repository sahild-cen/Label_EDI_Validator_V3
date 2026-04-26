# Field: PIA

## Display Name
Additional Product ID

## Segment ID
PIA

## Required
no

## Description
Provides additional product identification for customs purposes, specifically Harmonised System codes with optional country codes.

## Subfields

### product_identifier_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** 5
- **Required:** yes
- **Description:** Product identifier code qualifier. 5=Product identification

### item_identifier_1
- **Element Position:** 2.1
- **Pattern/Regex:** .{1,35}
- **Required:** yes
- **Description:** Item identifier — statistical number in accordance with Harmonised system (composite C212 first occurrence, sub-element 7140). For Road, if more than 8 characters a space must be inserted after position 8.

### item_type_identification_code_1
- **Element Position:** 2.2
- **Pattern/Regex:** HS
- **Required:** yes
- **Description:** Item type identification code (composite C212 first occurrence, sub-element 7143). HS=Harmonised system

### code_list_identification_code_1
- **Element Position:** 2.3
- **Pattern/Regex:** [A-Z]{2}
- **Required:** no
- **Description:** Code list identification code — ISO 3166-1 alpha-2 country code (composite C212 first occurrence, sub-element 1131). Required for Air/Sea with country code.

### code_list_responsible_agency_code_1
- **Element Position:** 2.4
- **Pattern/Regex:** 5
- **Required:** no
- **Description:** Code list responsible agency code (composite C212 first occurrence, sub-element 3055). 5=ISO

### item_identifier_2
- **Element Position:** 3.1
- **Pattern/Regex:** .{0,35}
- **Required:** no
- **Description:** Item identifier — second HS code (composite C212 second occurrence, sub-element 7140)

### item_type_identification_code_2
- **Element Position:** 3.2
- **Pattern/Regex:** HS
- **Required:** no
- **Description:** Item type identification code (composite C212 second occurrence, sub-element 7143). HS=Harmonised system

### code_list_identification_code_2
- **Element Position:** 3.3
- **Pattern/Regex:** [A-Z]{2}
- **Required:** no
- **Description:** Code list identification code — ISO 3166-1 alpha-2 country code (composite C212 second occurrence, sub-element 1131)

### code_list_responsible_agency_code_2
- **Element Position:** 3.4
- **Pattern/Regex:** 5
- **Required:** no
- **Description:** Code list responsible agency code (composite C212 second occurrence, sub-element 3055). 5=ISO

### item_identifier_3
- **Element Position:** 4.1
- **Pattern/Regex:** .{0,35}
- **Required:** no
- **Description:** Item identifier — third HS code (composite C212 third occurrence, sub-element 7140)

### item_type_identification_code_3
- **Element Position:** 4.2
- **Pattern/Regex:** HS
- **Required:** no
- **Description:** Item type identification code (composite C212 third occurrence, sub-element 7143)

### code_list_identification_code_3
- **Element Position:** 4.3
- **Pattern/Regex:** [A-Z]{2}
- **Required:** no
- **Description:** Code list identification code (composite C212 third occurrence, sub-element 1131)

### code_list_responsible_agency_code_3
- **Element Position:** 4.4
- **Pattern/Regex:** 5
- **Required:** no
- **Description:** Code list responsible agency code (composite C212 third occurrence, sub-element 3055)

### item_identifier_4
- **Element Position:** 5.1
- **Pattern/Regex:** .{0,35}
- **Required:** no
- **Description:** Item identifier — fourth HS code (composite C212 fourth occurrence, sub-element 7140)

### item_type_identification_code_4
- **Element Position:** 5.2
- **Pattern/Regex:** HS
- **Required:** no
- **Description:** Item type identification code (composite C212 fourth occurrence, sub-element 7143)

### code_list_identification_code_4
- **Element Position:** 5.3
- **Pattern/Regex:** [A-Z]{2}
- **Required:** no
- **Description:** Code list identification code (composite C212 fourth occurrence, sub-element 1131)

### code_list_responsible_agency_code_4
- **Element Position:** 5.4
- **Pattern/Regex:** 5
- **Required:** no
- **Description:** Code list responsible agency code (composite C212 fourth occurrence, sub-element 3055)

### item_identifier_5
- **Element Position:** 6.1
- **Pattern/Regex:** .{0,35}
- **Required:** no
- **Description:** Item identifier — fifth HS code (composite C212 fifth occurrence, sub-element 7140)

### item_type_identification_code_5
- **Element Position:** 6.2
- **Pattern/Regex:** HS
- **Required:** no
- **Description:** Item type identification code (composite C212 fifth occurrence, sub-element 7143)

### code_list_identification_code_5
- **Element Position:** 6.3
- **Pattern/Regex:** [A-Z]{2}
- **Required:** no
- **Description:** Code list identification code (composite C212 fifth occurrence, sub-element 1131)

### code_list_responsible_agency_code_5
- **Element Position:** 6.4
- **Pattern/Regex:** 5
- **Required:** no
- **Description:** Code list responsible agency code (composite C212 fifth occurrence, sub-element 3055)

## Edge Cases & Notes
For customs purpose only (when relevant). Up to 5 C212 composites can be used per PIA segment, and up to 9 PIA segments per goods item. For Air/Sea, Harmonized Code is required with ISO 3166-1 alpha-2 country code. Example: PIA+5+90099001:HS:DK:5+90099002:HS:DK:5+90099003:HS:DK:5+90099004:HS:DK:5+90099005:HS:DK:5'

## Claude Confidence
HIGH — spec provides detailed examples and structure across multiple repetitions

## Review Status
- [ ] Reviewed by human