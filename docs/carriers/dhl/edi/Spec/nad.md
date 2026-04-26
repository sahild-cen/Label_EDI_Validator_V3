# Field: NAD

## Display Name
Name and Address

## Segment ID
NAD

## Required
yes

## Description
A segment with names and addresses of different party roles. Used at consolidation level (SG4, up to 2 occurrences) and at shipment/invoice level (SG43, up to 99 occurrences).

## Subfields

### party_qualifier
- **Element Position:** 1
- **Pattern/Regex:** .{1,3}
- **Required:** yes
- **Description:** Party qualifier (element 3035) — e.g. CZ = consignor, PW = dispatch party, CN = consignee, FP = freight payer, JD = port of entry

### party_identification
- **Element Position:** 2.1
- **Pattern/Regex:** .{1,17}
- **Required:** no
- **Description:** Party identification (element 3039 within composite C082) — e.g. account number. Conditional.

### building_name
- **Element Position:** 3.1
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Building name (element 3124 within composite C058, first occurrence). Conditional.

### district
- **Element Position:** 3.2
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** District / City District (element 3124 within composite C058, second occurrence). Conditional at SG4; conditional at SG43.

### address_line_1
- **Element Position:** 3.3
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Address Line 1 (element 3124 within composite C058, third occurrence). Only in SG43.

### address_line_2
- **Element Position:** 3.4
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Address Line 2 (element 3124 within composite C058, fourth occurrence). Only in SG43.

### address_line_3
- **Element Position:** 3.5
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Address Line 3 (element 3124 within composite C058, fifth occurrence). Only in SG43.

### party_name
- **Element Position:** 4.1
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Party name (element 3036 within composite C080). Required when C080 is present.

### street_name
- **Element Position:** 5.1
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Street name (element 3042 within composite C059, first occurrence). Mandatory when C059 is used.

### building_number
- **Element Position:** 5.2
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Building number (element 3042 within composite C059, second occurrence). Required at SG4; conditional at SG43.

### house_number
- **Element Position:** 5.3
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** House number (element 3042 within composite C059, third occurrence). Required at SG4; conditional at SG43.

### address_line_4
- **Element Position:** 5.4
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Address line 4 (element 3042 within composite C059, fourth occurrence). Conditional.

### city_name
- **Element Position:** 6
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** City name (element 3164). Conditional.

### state_code
- **Element Position:** 7.1
- **Pattern/Regex:** .{1,9}
- **Required:** no
- **Description:** State code (element 3229 within composite C819). Conditional.

### code_list_identification_code
- **Element Position:** 7.2
- **Pattern/Regex:** .{1,17}
- **Required:** no
- **Description:** Code list identification code (element 1131 within composite C819). Not used at SG4; present at SG43.

### province
- **Element Position:** 7.4
- **Pattern/Regex:** .{1,70}
- **Required:** no
- **Description:** Province (element 3228 within composite C819). Conditional. Only in SG4.

### postcode_identification
- **Element Position:** 8
- **Pattern/Regex:** .{1,9}
- **Required:** no
- **Description:** Postcode identification (element 3251). Conditional.

### country_name_code
- **Element Position:** 9
- **Pattern/Regex:** [A-Z]{2}
- **Required:** no
- **Description:** Country name code (element 3207). Though not explicitly listed in the tables shown, standard EDIFACT NAD includes country code in position 9.

## Edge Cases & Notes
At SG4 level (page 30), the first NAD is mandatory with CZ qualifier for consignor; the second is optional with PW for dispatch party. At SG43 level (page 50), NAD supports qualifiers CN (consignee), FP (freight payer), JD (port of entry), etc. The C058 composite has more sub-elements at SG43 level (5 repetitions of 3124) compared to SG4 (2 repetitions). For LBBX, NAD+FP uses FOC account prefix; NAD+JD is used for port of entry address.

## Claude Confidence
MEDIUM — composite structure varies between SG4 and SG43 contexts; some elements inferred from standard EDIFACT

## Review Status
- [ ] Reviewed by human