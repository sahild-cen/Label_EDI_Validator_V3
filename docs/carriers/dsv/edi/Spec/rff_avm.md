# Field: RFF (Goods Item Information)

## Display Name
Reference - Goods Item Information

## Segment ID
RFF

## Required
no

## Description
Reference segment at line item level (SG23) for goods item information.

## Subfields

### reference_code_qualifier
- **Element Position:** 1.1
- **Pattern/Regex:** AVM
- **Required:** yes
- **Description:** Reference code qualifier — AVM = Goods item information (first sub-component of C506)

### reference_identifier
- **Element Position:** 1.2
- **Pattern/Regex:** .{1,70}
- **Required:** no
- **Description:** Reference identifier value

## Edge Cases & Notes
Example: RFF+AVM:GoodsItemId'

## Claude Confidence
HIGH — spec clearly defines all elements

## Review Status
- [ ] Reviewed by human