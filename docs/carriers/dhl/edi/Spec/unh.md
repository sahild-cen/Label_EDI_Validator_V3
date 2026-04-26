# Field: UNH

## Display Name
Message Header

## Segment ID
UNH

## Required
yes

## Description
To head, identify and specify a message. Contains the message reference number and message identifier details.

## Subfields

### message_reference_number
- **Element Position:** 1
- **Pattern/Regex:** .{1,14}
- **Required:** yes
- **Description:** An application generated unique message reference number. Must be unique for a period of 3 months.

### message_type_identifier
- **Element Position:** 2.1
- **Pattern/Regex:** IFCSUM
- **Required:** yes
- **Description:** Message type identifier — Use 'IFCSUM'

### message_type_version_number
- **Element Position:** 2.2
- **Pattern/Regex:** D
- **Required:** yes
- **Description:** Message type version number — Use 'D'

### message_type_release_number
- **Element Position:** 2.3
- **Pattern/Regex:** 01B
- **Required:** yes
- **Description:** Message type release number — Use '01B'

### controlling_agency
- **Element Position:** 2.4
- **Pattern/Regex:** UN
- **Required:** yes
- **Description:** Controlling agency — Use 'UN'

### common_access_reference
- **Element Position:** 3
- **Pattern/Regex:** .{1,35}
- **Required:** yes
- **Description:** DHL Express determined identification for recognizing the source shipping system platform. Format: 'GM2/' followed by the name of the source shipping platform (bilaterally agreed). E.g. GM2/ACMESHIPPINGPLATFORM_V1.6

## Edge Cases & Notes
The common_access_reference (element 0068) must start with 'GM2/' followed by the source shipping platform name which must be bilaterally agreed between the party generating the message and DHL Express.

## Claude Confidence
HIGH — spec clearly defines all elements with examples

## Review Status
- [ ] Reviewed by human