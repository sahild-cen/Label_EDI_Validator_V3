# Field: RFF (Packing List Number)

## Display Name
Reference - Packing List Number

## Segment ID
RFF

## Required
no

## Description
Reference segment at line item level (SG23) for packing list number.

## Subfields

### reference_code_qualifier
- **Element Position:** 1.1
- **Pattern/Regex:** PK
- **Required:** yes
- **Description:** Reference code qualifier — PK = Packing list number (first sub-component of C506)

### reference_identifier
- **Element Position:** 1.2
- **Pattern/Regex:** .{1,70}
- **Required:** no
- **Description:** Packing list number identifier

## Edge Cases & Notes
Example: RFF+PK:123456'

## Claude Confidence
HIGH — spec clearly defines all elements

## Review Status
- [ ] Reviewed by human