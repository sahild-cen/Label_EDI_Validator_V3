# Field: shipper_name_and_address

## Display Name
Shipper / Consignor Name and Address

## Field Description
A segment at header level (SG4 - NAD) to identify the consignor with account numbers, names and addresses.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes (Required — up to 3 occurrences at SG4)

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
NAD at header level specifically identifies the consignor. The spec notes it contains account numbers, names and addresses. SG5 (CTA/COM) provides contact person and communication details for this party. SG6 (RFF) provides registration numbers such as VAT number of the consignor.

## Claude Confidence
HIGH — Clearly described in the Declaration of Data Elements - Header section.

## Review Status
- [ ] Reviewed by human