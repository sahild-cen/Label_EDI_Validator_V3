# Field: declared_customs_value

## Display Name
Declared Customs Value

## Field Description
A monetary amount segment (SG25 - MOA) at shipment level to indicate a monetary value for an entire shipment, e.g. declared customs value, cash on delivery or insurance.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — up to 4 occurrences at shipment level

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
MOA appears at header level (for entire consignment), shipment level, and invoice level. At header level it covers cash on delivery or insurance for the entire consignment. At invoice level, per change report v1.3.6, notes were added for enabling the "Perfect Invoice" to carry further Duty/Tax amounts on Commercial Invoice.

## Claude Confidence
MEDIUM — MOA segment clearly described at multiple levels with different purposes.

## Review Status
- [ ] Reviewed by human