# Field: SEL

## Display Name
Seal Number

## Segment ID
SEL

## Required
no

## Description
Specifies seal numbers applied to transport equipment (containers).

## Subfields

### transport_unit_seal_identifier
- **Element Position:** 1
- **Pattern/Regex:** .{1,35}
- **Required:** yes
- **Description:** Transport unit seal identifier — the seal number

### sealing_party_name_code
- **Element Position:** 2.1
- **Pattern/Regex:** SH
- **Required:** no
- **Description:** Sealing party name code (composite C215, first sub-component). SH = Shipper

### seal_code_list_id
- **Element Position:** 2.2
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Code list identification code — Not used

### seal_agency_code
- **Element Position:** 2.3
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Code list responsible agency code — Not used

### sealing_party_name
- **Element Position:** 2.4
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Sealing party name — Not used

### seal_condition_code
- **Element Position:** 3
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Seal condition code — Not used

### object_identifier_1
- **Element Position:** 4.1
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Object identifier (composite C208, first sub-component) — Not used

### object_identifier_2
- **Element Position:** 4.2
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Object identifier (composite C208, second sub-component) — Not used

### seal_type_code
- **Element Position:** 5
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Seal type code — Not used

## Edge Cases & Notes
SEL is conditional, max 99 occurrences within SG38. Example: SEL+Z12800+SH'.

## Claude Confidence
HIGH — spec clearly defines structure and example

## Review Status
- [ ] Reviewed by human