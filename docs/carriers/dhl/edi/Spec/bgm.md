# Field: BGM

## Display Name
Beginning of Message

## Segment ID
BGM

## Required
yes

## Description
Identifies the beginning of the message, the document type, a unique document identifier, and the message function.

## Subfields

### document_name_code
- **Element Position:** 1.1
- **Pattern/Regex:** 785
- **Required:** yes
- **Description:** Document name code — 785 = Forwarding and consolidation summary message

### document_identifier
- **Element Position:** 1.2
- **Pattern/Regex:** .{1,35}
- **Required:** yes
- **Description:** Unique document/message identifier (typically matches the interchange control reference)

### message_function_code
- **Element Position:** 1.3
- **Pattern/Regex:** 9
- **Required:** yes
- **Description:** Message function code — 9 = Original

## Edge Cases & Notes
BGM appears once per message. Document name code is always 785 for DHL IFCSUM. The document identifier typically matches the UNH message reference number.

## Claude Confidence
HIGH — all examples consistently show BGM+785+{id}+9

## Review Status
- [x] Reviewed by human