# Field: TSR

## Display Name
Transport Service Requirements

## Segment ID
TSR

## Required
no

## Description
Specifies transport service requirements including insurance services and additional service codes for DSV Road Booking Data Standard.

## Subfields

### contract_and_carriage_condition_code
- **Element Position:** 1.1
- **Pattern/Regex:** an..3
- **Required:** no
- **Description:** Contract and carriage condition code (C536/4065). Not used in standard implementation.

### contract_and_carriage_condition_code_list
- **Element Position:** 1.2
- **Pattern/Regex:** an..17
- **Required:** no
- **Description:** Code list identification code (C536/1131). Not used.

### contract_and_carriage_condition_agency
- **Element Position:** 1.3
- **Pattern/Regex:** an..3
- **Required:** no
- **Description:** Code list responsible agency code (C536/3055). Not used.

### service_requirement_code_1
- **Element Position:** 2.1
- **Pattern/Regex:** (29|R[0-9]{2})
- **Required:** yes
- **Description:** Service requirement code (C233/7273). Valid codes include 29 (Insure goods during transport) and R01-R52 for Road Booking Data Standard additional services (e.g., R23=Crane Load, R30=Delivery Before 07, R52=Cargo Insurance).

### service_requirement_code_1_code_list
- **Element Position:** 2.2
- **Pattern/Regex:** an..17
- **Required:** no
- **Description:** Code list identification code (C233/1131). Not used.

### service_requirement_code_1_agency
- **Element Position:** 2.3
- **Pattern/Regex:** an..3
- **Required:** no
- **Description:** Code list responsible agency code (C233/3055). Not used.

### service_requirement_code_2
- **Element Position:** 2.4
- **Pattern/Regex:** an..3
- **Required:** no
- **Description:** Second service requirement code (C233/7273). Not used.

### service_requirement_code_2_code_list
- **Element Position:** 2.5
- **Pattern/Regex:** an..17
- **Required:** no
- **Description:** Code list identification code for second service requirement (C233/1131). Not used.

### service_requirement_code_2_agency
- **Element Position:** 2.6
- **Pattern/Regex:** an..3
- **Required:** no
- **Description:** Code list responsible agency code for second service requirement (C233/3055). Not used.

### transport_service_priority_code
- **Element Position:** 3.1
- **Pattern/Regex:** an..3
- **Required:** no
- **Description:** Transport service priority code (C537/4219). Not used.

### transport_priority_code_list
- **Element Position:** 3.2
- **Pattern/Regex:** an..17
- **Required:** no
- **Description:** Code list identification code (C537/1131). Not used.

### transport_priority_agency
- **Element Position:** 3.3
- **Pattern/Regex:** an..3
- **Required:** no
- **Description:** Code list responsible agency code (C537/3055). Not used.

### cargo_type_classification_code
- **Element Position:** 4.1
- **Pattern/Regex:** (Z[1-5])
- **Required:** no
- **Description:** Cargo type classification code (C703/7085). Required for Insurance Service (TSR++29). Valid codes: Z1=Ordinary new commercial goods, Z2=Used trading goods, Z3=High Risk goods, Z4=Fragile goods, Z5=Household goods and motor vehicles.

### cargo_type_code_list
- **Element Position:** 4.2
- **Pattern/Regex:** an..17
- **Required:** no
- **Description:** Code list identification code (C703/1131). Not used.

### cargo_type_agency
- **Element Position:** 4.3
- **Pattern/Regex:** 87
- **Required:** no
- **Description:** Code list responsible agency code (C703/3055). Required for TSR++29. 87 = Assigned by carrier.

## Edge Cases & Notes
TSR can occur up to 9 times. Insurance (TSR++29) is always an additional service and never placed as the first service requirement. When element 7273=29, the Nature of cargo (C703) is required with cargo type classification and agency code 87. Road Booking Data Standard uses R01-R52 codes exclusively. Examples: TSR++29++Z1::87' (Insurance, Ordinary goods), TSR++R23' (Crane Load), TSR++R30' (Delivery before 07).

## Claude Confidence
HIGH — spec provides detailed code lists and composite element structure

## Review Status
- [ ] Reviewed by human