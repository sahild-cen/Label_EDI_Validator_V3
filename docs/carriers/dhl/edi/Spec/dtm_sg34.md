# Field: DTM (SG34 Invoice Level)

## Display Name
Date, Time or Period (Document Date)

## Segment ID
DTM

## Required
no

## Description
A segment to indicate date and time for documents. Part of Segment Group 34 at Invoice Level.

## Subfields

### date_time_period_function_code_qualifier
- **Element Position:** 1.1
- **Pattern/Regex:** 3
- **Required:** yes
- **Description:** Date/Time/Period function code qualifier (element 2005 within C507 composite). Use '3' = Commercial Invoice date/time.

### date_time_period_value
- **Element Position:** 1.2
- **Pattern/Regex:** \d{12}
- **Required:** yes
- **Description:** Date/Time/Period value (element 2380). Invoice Date of the Commercial Invoice in format CCYYMMDDHHMM. The specified format is mandatory.

### date_time_period_format_code
- **Element Position:** 1.3
- **Pattern/Regex:** 203
- **Required:** yes
- **Description:** Date/Time/Period format code (element 2379). Use '203' for the date time mask CCYYMMDDHHMM.

## Edge Cases & Notes
Example: DTM+3:200906011500:203'. The format code 203 (CCYYMMDDHHMM) is mandatory.

## Claude Confidence
HIGH — spec provides clear example and format requirements

## Review Status
- [ ] Reviewed by human