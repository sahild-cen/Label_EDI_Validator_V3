# Field: CPI

## Display Name
Charge Payment Instructions

## Segment ID
CPI

## Required
no

## Description
Specifies charge payment instructions including who pays for the transport charges.

## Subfields

### charge_category_code
- **Element Position:** 1.1
- **Pattern/Regex:** .{1,3}
- **Required:** no
- **Description:** Charge category code

### code_list_identification_code
- **Element Position:** 1.2
- **Pattern/Regex:** .{1,17}
- **Required:** no
- **Description:** Code list identification code

### code_list_responsible_agency_code
- **Element Position:** 1.3
- **Pattern/Regex:** .{1,3}
- **Required:** no
- **Description:** Code list responsible agency code

### transport_charges_payment_method_code
- **Element Position:** 2
- **Pattern/Regex:** .{1,3}
- **Required:** no
- **Description:** Transport charges payment method code (e.g., prepaid, collect)

### payment_arrangement_code
- **Element Position:** 3
- **Pattern/Regex:** .{1,3}
- **Required:** no
- **Description:** Payment arrangement code

## Edge Cases & Notes
Used within SG6 (up to 9 occurrences). Mandatory within SG6 when the group is present.

## Claude Confidence
MEDIUM — standard EDIFACT CPI structure; carrier-specific codes not detailed in extracted text

## Review Status
- [ ] Reviewed by human