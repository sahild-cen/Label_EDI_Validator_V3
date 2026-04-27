# Field: MEA (Weight - Net)

## Display Name
Measurements - Net Weight

## Segment ID
MEA

## Required
yes

## Description
Measurement for net weight in kilograms at line item level. Only required for customs declaration purposes.

## Subfields

### measurement_purpose_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** WT
- **Required:** yes
- **Description:** Measurement purpose code qualifier — WT = Weights

### measured_attribute_code
- **Element Position:** 2.1
- **Pattern/Regex:** ADZ
- **Required:** yes
- **Description:** Measured attribute code — ADZ = Declared net weight (first sub-component of C502)

### measurement_unit_code
- **Element Position:** 3.1
- **Pattern/Regex:** KGM
- **Required:** yes
- **Description:** Measurement unit code — KGM = kilogram (first sub-component of C174 Value/range)

### measure
- **Element Position:** 3.2
- **Pattern/Regex:** .{1,18}
- **Required:** yes
- **Description:** The measured value (net weight in kilograms)

## Edge Cases & Notes
MEA segment with Net weight only required for customs declaration. Example: MEA+WT+ADZ+KGM:240'

## Claude Confidence
HIGH — spec clearly defines all elements

## Review Status
- [ ] Reviewed by human