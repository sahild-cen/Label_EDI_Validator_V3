# Field: UNZ

## Display Name
Interchange Trailer

## Segment ID
UNZ

## Required
yes

## Description
Identifies the end of the interchange and provides a count of messages within the interchange.

## Subfields

### interchange_control_count
- **Element Position:** 1
- **Pattern/Regex:** \d{1,6}
- **Required:** yes
- **Description:** Number of messages in the interchange

### interchange_control_reference
- **Element Position:** 2
- **Pattern/Regex:** .{1,14}
- **Required:** yes
- **Description:** Interchange control reference — must match the reference in UNB

## Edge Cases & Notes
UNZ appears exactly once per interchange. Example: UNZ+1+321654'. The interchange control reference must match the value in the UNB segment.

## Claude Confidence
HIGH — spec is clear and standard EDIFACT

## Review Status
- [ ] Reviewed by human