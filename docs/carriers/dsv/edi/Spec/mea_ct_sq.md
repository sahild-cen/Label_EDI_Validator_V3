# Field: MEA (Counts - Pallet Spaces)

## Display Name
Measurements - Pallet Spaces Count

## Segment ID
MEA

## Required
no

## Description
Measurement for number of pallet spaces at line item level. Not used for Air, Sea, or Courier shipments. Requires special pallet space agreement.

## Subfields

### measurement_purpose_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** CT
- **Required:** yes
- **Description:** Measurement purpose code qualifier — CT = Counts

### measured_attribute_code
- **Element Position:** 2.1
- **Pattern/Regex:** SQ
- **Required:** yes
- **Description:** Measured attribute code — SQ = Shipped quantity (first sub-component of C502)

### measurement_unit_code
- **Element Position:** 3.1
- **Pattern/Regex:** PLL
- **Required:** yes
- **Description:** Measurement unit code — PLL = Pallet spaces (first sub-component of C174 Value/range)

### measure
- **Element Position:** 3.2
- **Pattern/Regex:** .{1,18}
- **Required:** yes
- **Description:** Number of pallet spaces

## Edge Cases & Notes
Pallet spaces not used for Air, Sea, or Courier shipments. A special pallet space agreement is needed. On Road, qualifier SQ updates on item level/goods row; if no information in CNT then values are calculated and moved. Example: MEA+CT+SQ+PLL:3'

## Claude Confidence
HIGH — spec clearly defines all elements

## Review Status
- [ ] Reviewed by human