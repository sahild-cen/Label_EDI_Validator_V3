# Field: shipper_communication_contact

## Display Name
Shipper Communication Contact

## Field Description
A segment (SG5 - COM) to identify a communication number of a person or department to whom communication is directed, at the consignor header level.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — up to 9 occurrences allowed

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
Supports multiple communication types. Per the Document Change Report, qualifiers TEL, EML, FAX, and AL (for mobile/MOB) are supported.

## Claude Confidence
MEDIUM — Described in header declaration; communication qualifiers noted in change report.

## Review Status
- [ ] Reviewed by human