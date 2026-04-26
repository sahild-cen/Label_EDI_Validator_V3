# Field: TDT

## Display Name
Details of Transport

## Segment ID
TDT

## Required
no

## Description
A segment to indicate information related to a certain stage of the transport within the consolidation.

## Subfields

### transport_stage_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** \d{1,3}
- **Required:** yes
- **Description:** Transport stage code qualifier — e.g. 20 = Main transport

### means_of_transport_journey_identifier
- **Element Position:** 2
- **Pattern/Regex:** .{0,17}
- **Required:** no
- **Description:** Means of transport journey identifier — conveyance reference number

### mode_of_transport_code
- **Element Position:** 3
- **Pattern/Regex:** \d{1,3}
- **Required:** no
- **Description:** Mode of transport code

### transport_means_description_code
- **Element Position:** 4
- **Pattern/Regex:** .{0,17}
- **Required:** no
- **Description:** Transport means description code (composite element)

### carrier_name
- **Element Position:** 5
- **Pattern/Regex:** .{0,35}
- **Required:** no
- **Description:** Carrier identification and name (composite element)

## Edge Cases & Notes
TDT appears in SG9 (max 1 occurrence). Used to indicate transport details of the consolidation.

## Claude Confidence
MEDIUM — spec mentions TDT but provides limited element-level detail

## Review Status
- [ ] Reviewed by human