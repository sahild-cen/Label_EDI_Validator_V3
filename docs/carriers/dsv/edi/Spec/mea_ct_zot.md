# Field: MEA (Counts - Outturn Packages)

## Display Name
Measurements - Outturn Packages Count

## Segment ID
MEA

## Required
yes

## Description
Measurement for number of outturn packages at line item level. DSV-specific code, use as agreed.

## Subfields

### measurement_purpose_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** CT
- **Required:** yes
- **Description:** Measurement purpose code qualifier — CT = Counts

### measured_attribute_code
- **Element Position:** 2.1
- **Pattern/Regex:** ZOT
- **Required:** yes
- **Description:** Measured attribute code — ZOT = DSV specific code for Outturn Packages (first sub-component of C502)

### measurement_unit_code
- **Element Position:** 3.1
- **Pattern/Regex:** NMP
- **Required:** yes
- **Description:** Measurement unit code — NMP = number of packs (first sub-component of C174 Value/range)

### measure
- **Element Position:** 3.2
- **Pattern/Regex:** .{1,18}
- **Required:** yes
- **Description:** Number of outturn packages

## Edge Cases & Notes
DSV-specific code ZOT, use as agreed with DSV. Example: MEA+CT+ZOT+NMP:3'

## Claude Confidence
HIGH — spec clearly defines all elements

## Review Status
- [ ] Reviewed by human