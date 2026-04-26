# Field: DTM

## Display Name
Date, Time or Period

## Segment ID
DTM

## Required
yes

## Description
A segment to indicate date and time. Used at message level for processing date/time and dispatch date. Also used at shipment level (SG25) for estimated delivery date and at document level (SG34) for invoice date.

## Subfields

### date_time_period_function_code_qualifier
- **Element Position:** 1.1
- **Pattern/Regex:** (9|11|191|3)
- **Required:** yes
- **Description:** Date/Time/Period function code qualifier. '9' = Processing date/time (file creation/send to DHL), '11' = Dispatch date of shipment, '191' = Expected/Estimated Delivery date/time (SG25), '3' = Commercial Invoice date/time (SG34)

### date_time_period_value
- **Element Position:** 1.2
- **Pattern/Regex:** .{1,35}
- **Required:** yes
- **Description:** Date/Time/Period value. Format depends on format code: CCYYMMDDHHMM for '203', CCYYMMDD for '102'.

### date_time_period_format_code
- **Element Position:** 1.3
- **Pattern/Regex:** (203|102)
- **Required:** yes
- **Description:** Date/Time/Period format code. '203' = CCYYMMDDHHMM, '102' = CCYYMMDD. Use '102' when date refers to a dispatch date, otherwise use '203'.

## Edge Cases & Notes
At message level, DTM occurs at least twice: once for processing date/time (qualifier '9') and once for dispatch date (qualifier '11'). At SG25 shipment level, qualifier '191' is used for estimated delivery. At SG34 document level, qualifier '3' is used for commercial invoice date.

## Claude Confidence
HIGH — spec provides clear definitions and examples for all contexts

## Review Status
- [ ] Reviewed by human