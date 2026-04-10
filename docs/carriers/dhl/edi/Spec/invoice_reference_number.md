# Field: invoice_reference_number

## Display Name
Commercial Invoice Reference Number

## Field Description
A segment (SG32 Invoice Level - RFF) indicating registration numbers such as Commercial Invoice Reference Number and MRN (Movement Reference Number) related to the invoice.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Qualifier ABT is used for MRN (not "MRN" as qualifier)
- **Required:** yes (Required at invoice-level SG32, up to 999 occurrences)

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
Per change report v1.3.3, the qualifier for MRN in SG32 (Invoice level) C506, 1153 was corrected to show ABT, not MRN. This is an important implementation detail.

## Claude Confidence
HIGH — MRN qualifier correction explicitly documented in change report.

## Review Status
- [ ] Reviewed by human