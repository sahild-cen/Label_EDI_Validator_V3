# Field: PCI

## Display Name
Package Identification

## Segment ID
PCI

## Required
no

## Description
Package identification segment at line item level (SG24). Supports marking instructions codes 17 (Seller's instructions for serial numbers), 18 (Carrier's instructions for SSCC codes), and 24 (Shipper assigned package marks).

## Subfields

### marking_instructions_code
- **Element Position:** 1
- **Pattern/Regex:** (17|18|24)
- **Required:** no
- **Description:** Marking instructions code — 17 = Seller's instructions (serial numbers), 18 = Carrier's instructions (SSCC code), 24 = Shipper assigned

### shipping_marks_1
- **Element Position:** 2.1
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Shipping marks description (first occurrence). Used with qualifier 24 for package mark/IDs. Not used with 17 or 18.

### shipping_marks_2
- **Element Position:** 2.2
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Shipping marks description (second occurrence)

### shipping_marks_3
- **Element Position:** 2.3
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Shipping marks description (third occurrence)

### shipping_marks_4
- **Element Position:** 2.4
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Shipping marks description (fourth occurrence)

### shipping_marks_5
- **Element Position:** 2.5
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Shipping marks description (fifth occurrence)

### shipping_marks_6
- **Element Position:** 2.6
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Shipping marks description (sixth occurrence)

### shipping_marks_7
- **Element Position:** 2.7
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Shipping marks description (seventh occurrence)

### shipping_marks_8
- **Element Position:** 2.8
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Shipping marks description (eighth occurrence)

### shipping_marks_9
- **Element Position:** 2.9
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Shipping marks description (ninth occurrence)

### shipping_marks_10
- **Element Position:** 2.10
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Shipping marks description (tenth occurrence)

## Edge Cases & Notes
When qualifier is 17 or 18, the C210 Marks & labels composite is not used (marks come via following GIN segment). When qualifier is 24, the C210 composite carries package mark/IDs. Examples: PCI+17', PCI+18', PCI+24+518351:518352:518353:518354:518355:518356:518357:518358:518359:518360'

## Claude Confidence
HIGH — spec clearly defines all variants

## Review Status
- [ ] Reviewed by human