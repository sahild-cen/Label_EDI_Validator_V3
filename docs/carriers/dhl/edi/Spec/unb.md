# Field: UNB

## Display Name
Interchange Header

## Segment ID
UNB

## Required
yes

## Description
Identifies the interchange sender, recipient, date/time of preparation, and interchange control reference.

## Subfields

### syntax_identifier
- **Element Position:** 1
- **Pattern/Regex:** UNOA:2|UNOC:4
- **Required:** yes
- **Description:** Syntax identifier and version number (e.g. UNOA:2 or UNOC:4)

### interchange_sender
- **Element Position:** 2
- **Pattern/Regex:** .{1,35}
- **Required:** yes
- **Description:** Interchange sender identification (e.g. CIT, TVHBEPCO1)

### interchange_recipient
- **Element Position:** 3
- **Pattern/Regex:** .{1,35}
- **Required:** yes
- **Description:** Interchange recipient identification (e.g. DHLEUAPGW, DHL)

### date_time_of_preparation
- **Element Position:** 4
- **Pattern/Regex:** \d{6}:\d{4}
- **Required:** yes
- **Description:** Date and time of preparation in YYMMDD:HHMM format

### interchange_control_reference
- **Element Position:** 5
- **Pattern/Regex:** .{1,14}
- **Required:** yes
- **Description:** Unique interchange control reference number

## Edge Cases & Notes
UNB is the envelope header. Syntax identifier UNOA:2 or UNOC:4 observed in examples. Recipient for DHL is typically DHLEUAPGW or DHL.

## Claude Confidence
HIGH — multiple examples confirm structure

## Review Status
- [ ] Reviewed by human