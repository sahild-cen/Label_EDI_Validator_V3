# Field: EQN

## Display Name
Number of Units

## Segment ID
EQN

## Required
yes

## Description
A segment to specify the number of pieces of equipment required. The total number of pallets etc. of all shipments in the message. Part of Segment Group 70.

## Subfields

### number_of_units
- **Element Position:** 1
- **Pattern/Regex:** \d{1,15}
- **Required:** yes
- **Description:** Number of Units (element 6350 within C523 composite). Represents the number of pallets/boxes.

## Edge Cases & Notes
Example: EQN+10'. The value represents the total count of pallets or boxes across all shipments in the message.

## Claude Confidence
HIGH — spec is explicit about structure and meaning

## Review Status
- [ ] Reviewed by human