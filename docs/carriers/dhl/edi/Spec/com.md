# Field: COM

## Display Name
Communication Contact

## Segment ID
COM

## Required
no

## Description
To identify a communication number of a person or department to whom communication should be directed. Used in SG5 (shipper/consignor) and SG44 (consignee/receiver).

## Subfields

### communication_address_identifier
- **Element Position:** 1.1
- **Pattern/Regex:** .{1,70}
- **Required:** yes
- **Description:** Communication address identifier (phone number, email, fax). If phone number begins with '+' sign, the '?' release character must immediately precede it. Max 70 characters accepted by DHL.

### communication_address_code_qualifier
- **Element Position:** 1.2
- **Pattern/Regex:** (EM|FX|TE|AL)
- **Required:** yes
- **Description:** Communication address code qualifier. 'EM' = Electronic Mail, 'FX' = Telefax, 'TE' = Telephone, 'AL' = Cellular phone (Mobile).

## Edge Cases & Notes
If the phone number begins with '+', the EDIFACT release character '?' must be placed immediately before it to avoid translation problems (e.g., COM+?+31 653 123 456:TE'). Only 70 characters will be accepted by DHL.

## Claude Confidence
HIGH — spec is clear with examples including the release character edge case

## Review Status
- [ ] Reviewed by human