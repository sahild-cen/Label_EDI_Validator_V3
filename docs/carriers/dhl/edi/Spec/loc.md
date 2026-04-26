# Field: LOC

## Display Name
Place/Location Identification

## Segment ID
LOC

## Required
no

## Description
A segment to specify locations. Used within SG31 (related to incoterms), SG43 (related to NAD party), and at invoice line item level (country of manufacture).

## Subfields

### location_function_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** .{1,3}
- **Required:** yes
- **Description:** Location function code qualifier (element 3227)

### location_name_code
- **Element Position:** 2.1
- **Pattern/Regex:** .{1,25}
- **Required:** yes
- **Description:** Location name code (element 3225 within composite C517) — e.g. country code, DHL facility code. Max length varies: 3 chars in SG31/invoice LOC, 25 chars in SG43.

### code_list_identification_code
- **Element Position:** 2.2
- **Pattern/Regex:** .{1,17}
- **Required:** no
- **Description:** Code list identification code (element 1131 within composite C517) — not used (marked X) in SG31 shipment level; present in invoice level LOC

### code_list_responsible_agency_code
- **Element Position:** 2.3
- **Pattern/Regex:** .{1,3}
- **Required:** no
- **Description:** Code list responsible agency code (element 3055 within composite C517) — not used (marked X) in SG31 shipment level; present in invoice level LOC

### related_location_name_code
- **Element Position:** 3.1
- **Pattern/Regex:** .{1,25}
- **Required:** no
- **Description:** Related location name code (element 3223 within composite C519) — optional; used in SG31 shipment level and SG43

### location_name
- **Element Position:** 2.4
- **Pattern/Regex:** .{1,256}
- **Required:** no
- **Description:** Location name (element 3244 within composite C517) — only used in invoice-level LOC (page 75)

## Edge Cases & Notes
LOC usage varies across contexts. In SG31 shipment level (page 44), C519 is optional. In SG43 (page 52), LOC is mandatory with up to 9 occurrences and C517 location name code is up to 25 chars. In SG31 invoice level (page 75), C517 includes location name (3244) up to 256 chars. In SG50 invoice line item level (page 82), LOC is required for country of manufacture. DHL Express Facility Codes should be given per version 1.3.8.

## Claude Confidence
MEDIUM — LOC structure varies significantly across contexts

## Review Status
- [ ] Reviewed by human