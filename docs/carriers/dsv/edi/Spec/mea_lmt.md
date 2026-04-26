# Field: MEA (Loading Meters)

## Display Name
Measurements - Loading Meters

## Segment ID
MEA

## Required
no

## Description
Measurement for loading meters at line item level (SG21). Not used for Air, Sea, or Courier shipments.

## Subfields

### measurement_purpose_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** LMT
- **Required:** yes
- **Description:** Measurement purpose code qualifier — LMT = Loading meters

### measurement_details
- **Element Position:** 2
- **Pattern/Regex:** (empty)
- **Required:** no
- **Description:** C502 Measurement details composite — Not used for LMT variant

### measurement_unit_code
- **Element Position:** 3.1
- **Pattern/Regex:** MTR
- **Required:** yes
- **Description:** Measurement unit code — MTR = metre (first sub-component of C174 Value/range)

### measure
- **Element Position:** 3.2
- **Pattern/Regex:** .{1,18}
- **Required:** yes
- **Description:** The measured value (loading meters quantity in metres)

## Edge Cases & Notes
Loading meters not used for Air, Sea, or Courier shipments. Part of the alternative requirement: at least one of volume, loading meters, or dimensions must be provided. Example: MEA+LMT++MTR:4.8'

## Claude Confidence
HIGH — spec clearly defines all elements

## Review Status
- [ ] Reviewed by human