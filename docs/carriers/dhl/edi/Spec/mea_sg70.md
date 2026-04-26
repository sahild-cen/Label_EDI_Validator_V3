# Field: MEA (SG70)

## Display Name
Measurements (Equipment/Load Meters)

## Segment ID
MEA

## Required
no

## Description
To specify the length in a vehicle, whereby the complete width and height over the length is needed for the shipment. Part of Segment Group 70.

## Subfields

### measurement_application_qualifier
- **Element Position:** 1
- **Pattern/Regex:** LMT
- **Required:** yes
- **Description:** Measurement Application Qualifier (element 6311). Use 'LMT' = Load Meters.

### measurement_details
- **Element Position:** 2
- **Pattern/Regex:** .*
- **Required:** no
- **Description:** MEASUREMENT DETAILS composite (C502) — not used (marked X)

### measure_unit_qualifier
- **Element Position:** 3.1
- **Pattern/Regex:** (CMT|MTR|INH)
- **Required:** yes
- **Description:** Measure Unit Qualifier (element 6411) within VALUE RANGE composite (C174). Confirm with DHL Express which units can be supported: 'CMT', 'MTR' or 'INH'.

### measurement_value
- **Element Position:** 3.2
- **Pattern/Regex:** \d{1,18}(\.\d+)?
- **Required:** yes
- **Description:** Measurement Value (element 6314). The total loading meters needed for the entire shipment with decimals.

## Edge Cases & Notes
Example: MEA+LMT++MTR:20'. The empty element between LMT and the value range indicates C502 is not used. Confirm supported units with DHL Express for shipment origin country.

## Claude Confidence
HIGH — spec provides clear example and element descriptions

## Review Status
- [ ] Reviewed by human