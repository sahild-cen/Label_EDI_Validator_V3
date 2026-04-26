# Field: GDS

## Display Name
Nature of Cargo

## Segment ID
GDS

## Required
no

## Description
Specifies the nature of cargo and commodity code for the goods item.

## Subfields

### cargo_type_classification_code
- **Element Position:** 1.1
- **Pattern/Regex:** .{0,3}
- **Required:** no
- **Description:** Cargo type classification code (composite C703, sub-element 7085)

### product_group_name_code
- **Element Position:** 2.1
- **Pattern/Regex:** .{0,25}
- **Required:** no
- **Description:** Commodity Code — product group name code (composite C288, sub-element 5389)

## Edge Cases & Notes
Example: GDS++CommCode'

## Claude Confidence
HIGH — spec clearly defines the two used composites

## Review Status
- [ ] Reviewed by human