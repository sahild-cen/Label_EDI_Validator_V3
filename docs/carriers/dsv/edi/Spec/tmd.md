# Field: TMD

## Display Name
Transport Movement Details

## Segment ID
TMD

## Required
no

## Description
Specifies transport movement type details, primarily for container stuffing/stripping arrangements (LCL/FCL combinations) and door-to-door service types.

## Subfields

### movement_type_description_code
- **Element Position:** 1.1
- **Pattern/Regex:** (2|3|4|5|11|12|13|19|21|22|23|31|32|33)
- **Required:** no
- **Description:** Movement type description code (composite C219, first sub-component). Valid codes: 2=LCL/LCL, 3=FCL/FCL, 4=FCL/LCL, 5=LCL/FCL, 11=House to house, 12=House to terminal, 13=House to pier, 19=Consignee transportation provided, 21=Terminal to house, 22=Terminal to terminal, 23=Terminal to pier, 31=Pier to house, 32=Pier to terminal, 33=Pier to pier

### movement_type_description
- **Element Position:** 1.2
- **Pattern/Regex:** .{0,35}
- **Required:** no
- **Description:** Movement type description (composite C219, second sub-component). Free text description of movement type (e.g., "LCL/LCL")

### equipment_plan_description
- **Element Position:** 1.3
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Equipment plan description — Not used

### haulage_arrangements_code
- **Element Position:** 2
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Haulage arrangements code — Not used

## Edge Cases & Notes
TMD is conditional, max 1 occurrence within SG38. Not used for Road mode. Example: TMD+2:LCL/LCL'.

## Claude Confidence
HIGH — spec clearly defines valid codes and structure

## Review Status
- [ ] Reviewed by human