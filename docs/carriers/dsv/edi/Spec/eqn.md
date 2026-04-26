# Field: EQN

## Display Name
Number of Units

## Segment ID
EQN

## Required
no

## Description
Specifies the number of equipment units (EUR pallets or containers).

## Subfields

### units_quantity
- **Element Position:** 1.1
- **Pattern/Regex:** \d{1,15}
- **Required:** yes
- **Description:** Number of equipment units, EUR pallet or Container (composite C523, first sub-component)

### unit_type_code_qualifier
- **Element Position:** 1.2
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Unit type code qualifier — Not used

## Edge Cases & Notes
EQN is conditional, max 1 occurrence within SG38. Not used for Air, Sea, or Courier modes. Example: EQN+2' or EQN+9'.

## Claude Confidence
HIGH — spec is clear with examples

## Review Status
- [ ] Reviewed by human