# Field: GOR

## Display Name
Governmental Requirements

## Segment ID
GOR

## Required
no

## Description
Specifies governmental requirements related to the transport, such as export, import, or transit declarations.

## Subfields

### transport_movement_code
- **Element Position:** 1
- **Pattern/Regex:** (1|2|3)
- **Required:** no
- **Description:** Transport movement code. 1=Export, 2=Import, 3=Transit

### government_action_1
- **Element Position:** 2
- **Pattern/Regex:** N/A
- **Required:** no
- **Description:** Government action composite (not used in implementation)

### government_action_2
- **Element Position:** 3
- **Pattern/Regex:** N/A
- **Required:** no
- **Description:** Government action composite (not used in implementation)

### government_action_3
- **Element Position:** 4
- **Pattern/Regex:** N/A
- **Required:** no
- **Description:** Government action composite (not used in implementation)

### government_action_4
- **Element Position:** 5
- **Pattern/Regex:** N/A
- **Required:** no
- **Description:** Government action composite (not used in implementation)

## Edge Cases & Notes
Only the transport movement code (element 1) is used in the DSV implementation. All four Government action composites (C232) are marked as Not used. Example: GOR+1'

## Claude Confidence
HIGH — spec clearly shows only element 1 is used, all composites are Not used

## Review Status
- [ ] Reviewed by human