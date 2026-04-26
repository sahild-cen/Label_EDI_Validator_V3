# Field: HAN

## Display Name
Handling Instructions

## Segment ID
HAN

## Required
no

## Description
Indicates handling instructions for goods items, such as stackability.

## Subfields

### handling_instruction_description_code
- **Element Position:** 1.1
- **Pattern/Regex:** (3|ZNS)
- **Required:** no
- **Description:** Handling instruction description code (composite C524, sub-element 4079). 3=Stacked, ZNS=No Stackability

## Edge Cases & Notes
Not used for Air, Sea, or Courier shipments. Used for Road to indicate goods can be stacked. Example: HAN+3'

## Claude Confidence
HIGH — spec is clear about valid codes and usage

## Review Status
- [ ] Reviewed by human