# Field: UNT

## Display Name
Message Trailer

## Segment ID
UNT

## Required
yes

## Description
Identifies the end of the message and provides a count of segments within the message.

## Subfields

### number_of_segments
- **Element Position:** 1
- **Pattern/Regex:** \d{1,10}
- **Required:** yes
- **Description:** Number of segments in a message, including UNH and UNT

### message_reference_number
- **Element Position:** 2
- **Pattern/Regex:** .{1,14}
- **Required:** yes
- **Description:** Message reference number — must match the reference in UNH

## Edge Cases & Notes
UNT appears exactly once per message. Example: UNT+82+123'. The message reference number must correspond to the value in the UNH segment.

## Claude Confidence
HIGH — spec is clear and standard EDIFACT

## Review Status
- [ ] Reviewed by human