# Field: EQD

## Display Name
Equipment Details

## Segment ID
EQD

## Required
yes

## Description
Identifies equipment used for transport, primarily containers for sea shipments and exchangeable EUR flat pallets.

## Subfields

### equipment_type_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** (CN|EFP)
- **Required:** yes
- **Description:** Equipment type code qualifier. CN = Container (only valid for Sea shipments), EFP = Exchangeable EUR flat pallet

### equipment_identifier
- **Element Position:** 2.1
- **Pattern/Regex:** .{0,17}
- **Required:** no
- **Description:** Equipment identifier (composite C237, first sub-component). For Sea: Container Number. Not used for Air, Road, Courier.

### equipment_code_list_id
- **Element Position:** 2.2
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Code list identification code — Not used

### equipment_agency_code
- **Element Position:** 2.3
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Code list responsible agency code — Not used

### equipment_country_id
- **Element Position:** 2.4
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Country identifier — Not used

### equipment_size_type_code
- **Element Position:** 3.1
- **Pattern/Regex:** .{1,10}
- **Required:** no
- **Description:** Equipment size and type description code (composite C224, first sub-component). DSV-defined container types or ISO codes. Examples: 20GP, 20HC, 40HC, 40RE, 45HC, 20FR, 20OT, 20RE, 40FR, 20DC_HT, EFP, etc. Only mapped when type is container (CN).

### equipment_iso_code
- **Element Position:** 3.2
- **Pattern/Regex:** .{0,17}
- **Required:** no
- **Description:** Code list identification code (composite C224, second sub-component). For Sea: Container type ISO code (e.g., 22G0, 22G1).

### equipment_agency_responsible
- **Element Position:** 3.3
- **Pattern/Regex:** 5?
- **Required:** no
- **Description:** Code list responsible agency code (composite C224, third sub-component). For Sea: Container size code type. 5 = ISO (International Organization for Standardization).

### equipment_size_type_description
- **Element Position:** 3.4
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Equipment size and type description — Not used

### equipment_supplier_code
- **Element Position:** 4
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Equipment supplier code — Not used

### equipment_status_code
- **Element Position:** 5
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Equipment status code — Not used

### full_empty_indicator_code
- **Element Position:** 6
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Full or empty indicator code — Not used

### marking_instructions_code
- **Element Position:** 7
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Marking instructions code — Not used

## Edge Cases & Notes
EQD appears within SG38, with max 999 occurrences. For simple pallet usage: EQD+EFP'. For containers with full details: EQD+CN+CAXU7290380+20GP:22G0:5'. Equipment identifier and size/type details are conditional and primarily used for Sea shipments. DSV defines an extensive list of proprietary container type codes beyond standard ISO codes.

## Claude Confidence
HIGH — spec provides detailed code lists and multiple examples

## Review Status
- [ ] Reviewed by human