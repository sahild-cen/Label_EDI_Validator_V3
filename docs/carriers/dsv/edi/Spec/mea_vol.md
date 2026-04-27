# Field: MEA (Volume)

## Display Name
Measurements - Volume

## Segment ID
MEA

## Required
yes

## Description
Measurement for volume in cubic meters at line item level (SG21). At least one of volume, loading meters, or dimensions is required.

## Subfields

### measurement_purpose_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** VOL
- **Required:** yes
- **Description:** Measurement purpose code qualifier — VOL = Volume

### measurement_details
- **Element Position:** 2
- **Pattern/Regex:** (empty)
- **Required:** no
- **Description:** C502 Measurement details composite — Not used for VOL variant

### measurement_unit_code
- **Element Position:** 3.1
- **Pattern/Regex:** MTQ
- **Required:** yes
- **Description:** Measurement unit code — MTQ = cubic metre (first sub-component of C174 Value/range)

### measure
- **Element Position:** 3.2
- **Pattern/Regex:** .{1,18}
- **Required:** yes
- **Description:** The measured value (volume quantity in cubic metres)

## Edge Cases & Notes
Gross Weight at Shipment level (CNT+7) or for each line item is required. At least one of: shipment level Volume (CNT+15), each line item volume (MEA+VOL), shipment level Loading Meters (CNT+57), each line item loading meters (MEA+LMT), or each line item Dimensions (DIM) is required. Example: MEA+VOL++MTQ:12.096'

## Claude Confidence
HIGH — spec clearly defines all elements

## Review Status
- [ ] Reviewed by human