# Field: GIN

## Display Name
Goods Identity Number

## Segment ID
GIN

## Required
no

## Description
Goods identity number segment at line item level (SG24), used in conjunction with PCI. Supports serial numbers (BN with PCI+17) and SSCC codes (AW with PCI+18). Up to 5 pairs of identity number ranges per segment, max 10 occurrences.

## Subfields

### object_identification_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** (BN|AW)
- **Required:** yes
- **Description:** Object identification code qualifier — BN = Serial number (used with PCI+17), AW = Serial shipping container code (used with PCI+18)

### identity_number_1a
- **Element Position:** 2.1
- **Pattern/Regex:** .{1,35}
- **Required:** yes
- **Description:** First object identifier in first identity number range (C208). For AW, SSCC expected without leading 00 qualifier.

### identity_number_1b
- **Element Position:** 2.2
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Second object identifier in first identity number range

### identity_number_2a
- **Element Position:** 3.1
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** First object identifier in second identity number range (C208)

### identity_number_2b
- **Element Position:** 3.2
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Second object identifier in second identity number range

### identity_number_3a
- **Element Position:** 4.1
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** First object identifier in third identity number range (C208)

### identity_number_3b
- **Element Position:** 4.2
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Second object identifier in third identity number range

### identity_number_4a
- **Element Position:** 5.1
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** First object identifier in fourth identity number range (C208)

### identity_number_4b
- **Element Position:** 5.2
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Second object identifier in fourth identity number range

### identity_number_5a
- **Element Position:** 6.1
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** First object identifier in fifth identity number range (C208)

### identity_number_5b
- **Element Position:** 6.2
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Second object identifier in fifth identity number range

## Edge Cases & Notes
For SSCC (AW qualifier), codes are expected to NOT include the qualifier 00. V1.5 added mapping to handle SSCC with qualifier 00. Examples: GIN+BN+123456789', GIN+AW+373999991234567899'

## Claude Confidence
HIGH — spec clearly defines all elements

## Review Status
- [ ] Reviewed by human