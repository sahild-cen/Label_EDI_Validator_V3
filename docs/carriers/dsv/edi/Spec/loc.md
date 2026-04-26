# Field: LOC

## Display Name
Place Location Identification

## Segment ID
LOC

## Required
no

## Description
Identifies locations relevant to the shipment, including booking office location (SG1) and place of terms of delivery (SG2).

## Subfields

### location_function_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** (ZBO|1)
- **Required:** yes
- **Description:** Location function code qualifier (3227). Valid codes: ZBO=Booking office (use to be agreed), 1=Place of terms of delivery.

### location_identifier
- **Element Position:** 2.1
- **Pattern/Regex:** an..35
- **Required:** no
- **Description:** Location identifier (C517/3225). Used for Branch code (Air/Sea) or Booking Office code (Road). UN Location Code when used for terms of delivery.

### location_code_list
- **Element Position:** 2.2
- **Pattern/Regex:** an..17
- **Required:** no
- **Description:** Code list identification code (C517/1131).

### location_agency
- **Element Position:** 2.3
- **Pattern/Regex:** (3|6|87)
- **Required:** no
- **Description:** Code list responsible agency code (C517/3055). Valid codes: 3=IATA, 6=UN/ECE, 87=Assigned by carrier.

### location_name
- **Element Position:** 2.4
- **Pattern/Regex:** .{1,256}
- **Required:** no
- **Description:** Location name (C517/3224). Term Location name required for Road when LOC qualifier is 1.

### first_related_location_identifier
- **Element Position:** 3.1
- **Pattern/Regex:** an..35
- **Required:** no
- **Description:** First related location identifier (C519/3223). Used for Department code (Air/Sea). Not used for Road or Courier.

### first_related_location_code_list
- **Element Position:** 3.2
- **Pattern/Regex:** an..17
- **Required:** no
- **Description:** Code list identification code (C519/1131). Not used.

### first_related_location_agency
- **Element Position:** 3.3
- **Pattern/Regex:** an..3
- **Required:** no
- **Description:** Code list responsible agency code (C519/3055). Not used.

### first_related_location_name
- **Element Position:** 3.4
- **Pattern/Regex:** an..70
- **Required:** no
- **Description:** First related location name (C519/3222). Not used.

### second_related_location_identifier
- **Element Position:** 4.1
- **Pattern/Regex:** an..35
- **Required:** no
- **Description:** Second related location identifier (C553/3233). Used for Country code. Not used for Road, Solutions, or Courier.

### second_related_location_code_list
- **Element Position:** 4.2
- **Pattern/Regex:** an..17
- **Required:** no
- **Description:** Code list identification code (C553/1131). Not used.

### second_related_location_agency
- **Element Position:** 4.3
- **Pattern/Regex:** an..3
- **Required:** no
- **Description:** Code list responsible agency code (C553/3055). Not used.

### second_related_location_name
- **Element Position:** 4.4
- **Pattern/Regex:** an..70
- **Required:** no
- **Description:** Second related location name (C553/3232). Not used.

### relation_code
- **Element Position:** 5
- **Pattern/Regex:** an..3
- **Required:** no
- **Description:** Relation code (5479). Not used.

## Edge Cases & Notes
LOC appears in multiple segment groups: SG1 (with qualifier ZBO for booking office, max 99 occurrences) and SG2 (with qualifier 1 for place of terms of delivery, max 9 occurrences). For ZBO: used for Autoimport functionality (Air/Sea) or specific booking office (Road). Examples: LOC+ZBO+DKNOR::6', LOC+ZBO+2BO::6+ROA+US', LOC+1+SESTO::6:STOCKHOLM', LOC+1+:::STOCKHOLM'.

## Claude Confidence
HIGH — spec provides detailed usage for both LOC contexts

## Review Status
- [ ] Reviewed by human