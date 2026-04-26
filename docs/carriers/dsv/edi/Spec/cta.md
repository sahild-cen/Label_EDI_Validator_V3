# Field: CTA

## Display Name
Contact Information

## Segment ID
CTA

## Required
no

## Description
Identifies the contact person associated with a party (NAD). Mandatory if COM segment is present.

## Subfields

### contact_function_code
- **Element Position:** 1
- **Pattern/Regex:** IC
- **Required:** no
- **Description:** Contact function code. IC=Information contact

### contact_identifier
- **Element Position:** 2.1
- **Pattern/Regex:** .{0,17}
- **Required:** no
- **Description:** Contact identifier (composite C056, sub-element 3413) — Not used

### contact_name
- **Element Position:** 2.2
- **Pattern/Regex:** .{0,256}
- **Required:** no
- **Description:** Contact name (composite C056, sub-element 3412)

## Edge Cases & Notes
If information is found in COM segment then CTA is mandatory. Example: CTA+IC+:Contact person'

## Claude Confidence
HIGH — spec clearly defines segment structure

## Review Status
- [ ] Reviewed by human