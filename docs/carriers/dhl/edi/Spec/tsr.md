# Field: TSR

## Display Name
Transport Service Requirements

## Segment ID
TSR

## Required
yes

## Description
To specify contract and carriage conditions and service and priority requirements for the transport. Used in SG25 (shipment-level product code) and SG49 (party-level product code).

## Subfields

### contract_and_carriage_condition
- **Element Position:** 1
- **Pattern/Regex:** .*
- **Required:** no
- **Description:** Contract and carriage condition — Not used.

### service
- **Element Position:** 2
- **Pattern/Regex:** .*
- **Required:** no
- **Description:** Service — Not used.

### transport_service_priority_code
- **Element Position:** 3.1
- **Pattern/Regex:** .{1,3}
- **Required:** yes
- **Description:** Transport service priority code. DHL product code (e.g., '189' = Express Worldwide EU, '110' = Economy Select EU at SG25; 'ECX' = Express Worldwide EU, 'ESU' = Economy Select EU at SG49). Consult Sales Representative for full list.

### code_list_identification_code
- **Element Position:** 3.2
- **Pattern/Regex:** 57
- **Required:** yes
- **Description:** Code list identification code — Use '57' for Product code.

### code_list_responsible_agency_code
- **Element Position:** 3.3
- **Pattern/Regex:** 87
- **Required:** yes
- **Description:** Code list responsible agency code — Use '87' for Assigned by carrier.

## Edge Cases & Notes
Elements 1 and 2 (C536 and C233) are not used, so the segment starts with '+++' before the transport priority composite. SG25 uses numeric product codes (e.g., 189, 110) while SG49 uses alphanumeric codes (e.g., ECX, ESU).

## Claude Confidence
HIGH — spec provides clear examples for both SG25 and SG49 usage

## Review Status
- [ ] Reviewed by human