# Field: EQD

## Display Name
Equipment Details

## Segment ID
EQD

## Required
yes

## Description
To identify a unit of equipment such as pallets and boxes used for transporting goods. Part of Segment Group 70.

## Subfields

### equipment_type_code
- **Element Position:** 1
- **Pattern/Regex:** (EFP|EYP|FPN|BPN)
- **Required:** yes
- **Description:** Equipment Type code (element 8053). Values: 'EFP' = Changeable Pallet, 'EYP' = Changeable Box, 'FPN' = Pallet, 'BPN' = Box Pallet

## Edge Cases & Notes
Example: EQD+EFP'. Only the equipment type code element is used; no other elements are populated.

## Claude Confidence
HIGH — spec clearly lists valid codes and structure

## Review Status
- [ ] Reviewed by human