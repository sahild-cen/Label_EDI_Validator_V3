# Field: BGM

## Display Name
Beginning of Message

## Segment ID
BGM

## Required
yes

## Description
Identifies the beginning of the message and its type. Specifies document type, identifier and message function.

## Subfields

### document_name_code
- **Element Position:** 1.1
- **Pattern/Regex:** (335|610|ZEB|ZBJ)
- **Required:** yes
- **Description:** Document name code — 335 = Pre booking (Air/Sea), 610 = Forwarding instructions, ZEB = ExternalBookingRequest, ZBJ = BrokerageJob

### document_identifier
- **Element Position:** 2.1
- **Pattern/Regex:** .{1,70}
- **Required:** no
- **Description:** Waybill number or another reference to the message. Must be unique for at least 1 year. Required on all messages.

### message_function_code
- **Element Position:** 3
- **Pattern/Regex:** (1|5|9)
- **Required:** no
- **Description:** Message function — 1 = Cancellation, 5 = Replace, 9 = Original. For Air/Sea only code 9 is used.

## Edge Cases & Notes
Example: BGM+610+1081340877+9'
For Air and Sea bookings, only use 335. Codes 1 and 5 not used for Air/Sea.
Document identifier is required on all messages even though marked conditional.

## Claude Confidence
HIGH — spec clearly specifies all elements with valid codes

## Review Status
- [ ] Reviewed by human