# Field: shipper_vat_number

## Display Name
Shipper VAT Registration Number

## Field Description
A segment (SG6 - RFF) indicating the Registration Numbers (e.g. VAT number) of the consignor at header level.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — up to 9 occurrences at SG6

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
Per change report v1.2, RFF/C506/1156 was added to SG6. This is for VAT and other registration numbers of the consignor.

## Claude Confidence
MEDIUM — Clearly described as VAT number reference at header level.

## Review Status
- [ ] Reviewed by human