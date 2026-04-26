# Field: UNH

## Display Name
Message Header

## Segment ID
UNH

## Required
yes

## Description
Identifies the beginning of a message and contains the message reference number and message type identification.

## Subfields

### message_reference_number
- **Element Position:** 1
- **Pattern/Regex:** .{1,14}
- **Required:** yes
- **Description:** Unique message reference number

### message_type
- **Element Position:** 2.1
- **Pattern/Regex:** IFTMIN
- **Required:** yes
- **Description:** Message type — IFTMIN = Instruction message

### message_version_number
- **Element Position:** 2.2
- **Pattern/Regex:** D
- **Required:** yes
- **Description:** Message version number — D = Draft version/UN/EDIFACT Directory

### message_release_number
- **Element Position:** 2.3
- **Pattern/Regex:** 10B
- **Required:** yes
- **Description:** Message release number — 10B = Release 2010 - B

### controlling_agency
- **Element Position:** 2.4
- **Pattern/Regex:** UN
- **Required:** yes
- **Description:** Controlling agency — UN = UN/CEFACT

### association_assigned_code
- **Element Position:** 2.5
- **Pattern/Regex:** .{1,6}
- **Required:** no
- **Description:** Association assigned code

## Edge Cases & Notes
Example: UNH+123+IFTMIN:D:10B:UN:X'
Must contain 0065=IFTMIN, 0052=D, 0054=10B, 0051=UN.

## Claude Confidence
HIGH — spec clearly specifies all required elements with example

## Review Status
- [ ] Reviewed by human