# Field: shipper_contact_name

## Display Name
Shipper Contact Person

## Field Description
A segment (SG5 - CTA) to specify a person within the consignor party at header level.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — up to 9 occurrences allowed at SG5

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
Part of SG5 which is nested under SG4 (consignor). Works in conjunction with COM segment for communication details.

## Claude Confidence
MEDIUM — Described in branching diagram and header declaration.

## Review Status
- [ ] Reviewed by human