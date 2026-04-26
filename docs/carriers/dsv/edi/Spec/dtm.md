# Field: DTM

## Display Name
Date Time Period

## Segment ID
DTM

## Required
yes (at least one occurrence with qualifier 137 is mandatory)

## Description
Specifies date/time/period information. Used for delivery date requested, document issue date, collection date, reference date, and transport dates.

## Subfields

### date_time_period_function_code_qualifier
- **Element Position:** 1.1
- **Pattern/Regex:** (2|137|234|132|133|171|189|232)
- **Required:** yes
- **Description:** Date/time/period function code qualifier — 2 = Delivery date/time requested, 137 = Document issue date time, 234 = Collection date/time earliest, 132 = Transport means arrival estimated, 133 = Transport means departure estimated, 171 = Reference date/time, 189 = Transport means departure scheduled, 232 = Transport means arrival scheduled

### date_time_period_text
- **Element Position:** 1.2
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Date or time or period value in the format specified by element 1.3

### date_time_period_format_code
- **Element Position:** 1.3
- **Pattern/Regex:** (102|203|719)
- **Required:** no
- **Description:** Date/time/period format code — 102 = CCYYMMDD, 203 = CCYYMMDDHHMM, 719 = CCYYMMDDHHMM-CCYYMMDDHHMM

## Edge Cases & Notes
Multiple DTM segments used per message with different qualifiers.
DTM+137 (document issue date) is mandatory.
DTM+2 (delivery date requested) is conditional.
DTM+234 (collection date earliest) is conditional; for Road, collection date is required and date range not accepted.
Format 719 not used for Air/Sea.
Examples: DTM+2:20240820:102', DTM+137:202408201000:203', DTM+234:202408201000-202408201200:719'

## Claude Confidence
HIGH — spec clearly specifies all elements and qualifiers

## Review Status
- [ ] Reviewed by human