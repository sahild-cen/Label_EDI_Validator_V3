# Field: DIM

## Display Name
Dimensions

## Segment ID
DIM

## Required
no

## Description
Dimensions (length, width, height) at line item level (SG22). Part of the alternative measurement requirement alongside volume and loading meters.

## Subfields

### dimension_type_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** 1
- **Required:** yes
- **Description:** Dimension type code qualifier — 1 = Gross dimensions

### measurement_unit_code
- **Element Position:** 2.1
- **Pattern/Regex:** (CMT|MTR)
- **Required:** yes
- **Description:** Measurement unit code — CMT = centimetre, MTR = metre. For Road, dimensions must be in MTR.

### length_measure
- **Element Position:** 2.2
- **Pattern/Regex:** .{1,15}
- **Required:** yes
- **Description:** Length measure

### width_measure
- **Element Position:** 2.3
- **Pattern/Regex:** .{1,15}
- **Required:** yes
- **Description:** Width measure

### height_measure
- **Element Position:** 2.4
- **Pattern/Regex:** .{1,15}
- **Required:** yes
- **Description:** Height measure

## Edge Cases & Notes
For Road shipments, dimensions must be in MTR. Part of the alternative requirement: at least one of shipment level volume (CNT+15), shipment level loading meters (CNT+57), each line item volume (MEA+VOL), each line item loading meters (MEA+LMT), or each line item dimensions (DIM) is required. Example: DIM+1+MTR:0.2:0.1:0.1' or DIM+1+CMT:9:9:9'

## Claude Confidence
HIGH — spec clearly defines all elements

## Review Status
- [ ] Reviewed by human