# Field: TDT

## Display Name
Transport Information

## Segment ID
TDT

## Required
no

## Description
Specifies transport stage details including mode of transport and carrier identification. Used in combination with TSR to determine the product/service.

## Subfields

### transport_stage_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** .{1,3}
- **Required:** yes
- **Description:** Transport stage code qualifier — typically 20 = Main carriage transport

### means_of_transport_journey_identifier
- **Element Position:** 2
- **Pattern/Regex:** .{1,17}
- **Required:** no
- **Description:** Means of transport journey identifier (e.g., voyage/flight number)

### mode_of_transport_code
- **Element Position:** 3.1
- **Pattern/Regex:** (3|4|5)
- **Required:** no
- **Description:** Mode of transport code — 3 = Road, 4 = Air, 5 = Sea (also used for Courier combinations)

### carrier_identifier
- **Element Position:** 5.1
- **Pattern/Regex:** .{1,17}
- **Required:** no
- **Description:** Carrier identification

### code_list_identification_code
- **Element Position:** 5.2
- **Pattern/Regex:** .{1,17}
- **Required:** no
- **Description:** Code list identification code for carrier

### code_list_responsible_agency_code
- **Element Position:** 5.3
- **Pattern/Regex:** .{1,3}
- **Required:** no
- **Description:** Code list responsible agency code for carrier

### carrier_name
- **Element Position:** 5.4
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Carrier name

### transit_direction_indicator_code
- **Element Position:** 6
- **Pattern/Regex:** .{1,3}
- **Required:** no
- **Description:** Transit direction indicator code

### excess_transportation_information
- **Element Position:** 7.1
- **Pattern/Regex:** .{1,3}
- **Required:** no
- **Description:** Excess transportation reason code

### transport_means_description_code
- **Element Position:** 8.1
- **Pattern/Regex:** .{1,8}
- **Required:** no
- **Description:** Transport means description code

## Edge Cases & Notes
Used within SG8 (up to 99 occurrences, two instances defined). Mandatory within SG8. Mode of transport code is critical for determining product: 3=Road, 4=Air, 5=Sea. Used in combination with TSR for Courier DK: TDT+20++3' with TSR++Z09+1' = DSV Priority.
Examples: TDT+20++3', TDT+20++4', TDT+20++5'

## Claude Confidence
HIGH — spec provides extensive notes on TDT/TSR combinations for product determination

## Review Status
- [ ] Reviewed by human