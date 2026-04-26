# Field: NAD

## Display Name
Name and Address

## Segment ID
NAD

## Required
yes

## Description
Identifies parties involved in the shipment by function (consignor, consignee, delivery party, etc.) with their identification and address details.

## Subfields

### party_function_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** (AG|AJ|CA|CN|CZ|DP|FP|NI|OY|PW|FW)
- **Required:** yes
- **Description:** Party function code qualifier. AG=Agent, AJ=Party issuing mutually agreed codes, CA=Carrier, CN=Consignee, CZ=Consignor, DP=Delivery party, FP=Freight/charges payer, NI=Notify party, OY=Ordering customer, PW=Despatch party, FW=Freight forwarder

### party_identifier
- **Element Position:** 2.1
- **Pattern/Regex:** .{1,35}
- **Required:** yes
- **Description:** Customer number / reference (composite C082, sub-element 3039)

### code_list_identification_code
- **Element Position:** 2.2
- **Pattern/Regex:** .{0,17}
- **Required:** no
- **Description:** Code list identification code (composite C082, sub-element 1131) — Not used

### code_list_responsible_agency_code
- **Element Position:** 2.3
- **Pattern/Regex:** (9|87|91|Z87)
- **Required:** no
- **Description:** Code list responsible agency code (composite C082, sub-element 3055). 87=Assigned by carrier (DSV customer number for CZ/PW), 91=Assigned by seller (for CN and other addresses), 9=GS1, Z87=DSV specific value to generate unique party ID

### party_name_1
- **Element Position:** 4.1
- **Pattern/Regex:** .{1,70}
- **Required:** yes
- **Description:** Party name — first occurrence (composite C080, sub-element 3036). DSV only uses 35 characters in first and second occurrences.

### party_name_2
- **Element Position:** 4.2
- **Pattern/Regex:** .{0,70}
- **Required:** no
- **Description:** Party name — second occurrence (composite C080, sub-element 3036)

### party_name_3
- **Element Position:** 4.3
- **Pattern/Regex:** .{0,70}
- **Required:** no
- **Description:** Party name — third occurrence (composite C080, sub-element 3036)

### party_name_format_code
- **Element Position:** 4.6
- **Pattern/Regex:** (ZAO)?
- **Required:** no
- **Description:** Party name format code (composite C080, sub-element 3045). ZAO=Address override

### street_and_number_1
- **Element Position:** 5.1
- **Pattern/Regex:** .{1,35}
- **Required:** yes
- **Description:** Street name and number (composite C059, sub-element 3042, first occurrence). P.O. Box not acceptable for NAD+PW or NAD+DP.

### street_and_number_2
- **Element Position:** 5.2
- **Pattern/Regex:** .{0,35}
- **Required:** no
- **Description:** Additional address info — gate or building (composite C059, sub-element 3042, second occurrence)

### street_and_number_3
- **Element Position:** 5.3
- **Pattern/Regex:** .{0,35}
- **Required:** no
- **Description:** Street and number or post office box identifier — third occurrence (composite C059, sub-element 3042)

### city_name
- **Element Position:** 6
- **Pattern/Regex:** .{1,35}
- **Required:** yes
- **Description:** City name (without postal code). Required for Road.

### country_subdivision_identifier
- **Element Position:** 7.1
- **Pattern/Regex:** .{0,9}
- **Required:** no
- **Description:** Province or State (composite C819, sub-element 3229)

### postal_identification_code
- **Element Position:** 8
- **Pattern/Regex:** .{0,17}
- **Required:** no
- **Description:** Postal code (without country code)

### country_identifier
- **Element Position:** 9
- **Pattern/Regex:** [A-Z]{2}
- **Required:** yes
- **Description:** Country code, ISO 3166 - Alpha 2 code. Required for Road.

## Edge Cases & Notes
NAD+CZ and NAD+CN are mandatory. NAD+DP is used when delivery party differs from consignee. NAD+PW is used when despatch party differs from consignor. NAD+FP is used for freight payer in connection with CPI segment. NAD+NI used for notify party. NAD+AJ only used for Masterlabel information. NAD+OY only used for Air&Sea. Structured address is required (C058 unstructured not used). For Road: at least one of Incoterm (TOD+6) or Freight Payer (NAD+FP) is required; NAD+DP and NAD+PW are required.

## Claude Confidence
HIGH — spec provides detailed element-level information with examples

## Review Status
- [ ] Reviewed by human