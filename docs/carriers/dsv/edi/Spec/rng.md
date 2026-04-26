# Field: RNG

## Display Name
Range Details

## Segment ID
RNG

## Required
no

## Description
Specifies temperature range details for goods items requiring temperature control.

## Subfields

### range_type_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** 1
- **Required:** yes
- **Description:** Range type code qualifier. 1=Allowance range

### measurement_unit_code
- **Element Position:** 2.1
- **Pattern/Regex:** CEL
- **Required:** yes
- **Description:** Measurement unit code (composite C280, sub-element 6411). CEL=degree Celsius. Only Celsius is used, not Fahrenheit.

### range_minimum_quantity
- **Element Position:** 2.2
- **Pattern/Regex:** -?\d{1,18}
- **Required:** no
- **Description:** Minimum temperature (composite C280, sub-element 6162)

### range_maximum_quantity
- **Element Position:** 2.3
- **Pattern/Regex:** -?\d{1,18}
- **Required:** no
- **Description:** Maximum temperature (composite C280, sub-element 6152)

## Edge Cases & Notes
Not used for Air, Sea, or Courier shipments. Can indicate transport product: Heated (RNG+1+CEL:0:99') or Cooled (RNG+1+CEL:99:0'). Example: RNG+1+CEL:10:25'

## Claude Confidence
HIGH — spec provides clear structure and examples

## Review Status
- [ ] Reviewed by human