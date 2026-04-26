# Field: MEA (SG67)

## Display Name
Measurements (Dangerous Goods)

## Segment ID
MEA

## Required
yes

## Description
Measurements of goods items within Segment Group 67 (Dangerous Goods measurements context). Note: Not to be used for Dangerous Goods when shipping with DHL Express.

## Subfields

### measurement_purpose_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** [A-Z]{2,3}
- **Required:** yes
- **Description:** Measurement purpose code qualifier (element 6311)

### measured_attribute_code
- **Element Position:** 2
- **Pattern/Regex:** .*
- **Required:** no
- **Description:** MEASUREMENTS DETAILS composite (C502) — not specified in detail for this context

### measure_unit_qualifier
- **Element Position:** 3.1
- **Pattern/Regex:** [A-Z]{2,3}
- **Required:** yes
- **Description:** Measure unit qualifier (element 6411) within VALUE/RANGE composite (C174)

### measurement_value
- **Element Position:** 3.2
- **Pattern/Regex:** \d{1,18}
- **Required:** yes
- **Description:** Measurement value (element 6314) within VALUE/RANGE composite (C174)

## Edge Cases & Notes
This section is not to be used to describe a shipment as including Dangerous Goods when shipping with DHL Express. When commodities categorized as Dangerous Goods or Restricted Commodities are sent, particular values are given in SG25–FTX, SG31–TOD and SG32–RFF.

## Claude Confidence
MEDIUM — segment structure is clear but usage is restricted for DHL Express

## Review Status
- [ ] Reviewed by human