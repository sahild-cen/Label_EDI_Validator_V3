# Field: COM

## Display Name
Communication Contact

## Segment ID
COM

## Required
no

## Description
Provides communication contact details (phone, email, fax) for a party contact.

## Subfields

### communication_address_identifier
- **Element Position:** 1.1
- **Pattern/Regex:** .{1,512}
- **Required:** yes
- **Description:** Communication address identifier — phone number, email address, fax number, etc. (composite C076, sub-element 3148)

### communication_means_type_code
- **Element Position:** 1.2
- **Pattern/Regex:** (AL|EM|FX|TE)
- **Required:** yes
- **Description:** Communication means type code. AL=Cellular phone, EM=Electronic mail, FX=Telefax, TE=Telephone

## Edge Cases & Notes
Can occur up to 9 times per CTA. Example: COM+1111111111:TE'

## Claude Confidence
HIGH — spec clearly defines both sub-elements

## Review Status
- [ ] Reviewed by human