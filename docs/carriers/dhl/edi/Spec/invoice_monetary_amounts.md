# Field: invoice_monetary_amounts

## Display Name
Invoice Monetary Amounts

## Field Description
A segment (SG25 Invoice Level - MOA) to indicate monetary values for an invoice, e.g. declared customs value, cash on delivery, insurance, and duty/tax amounts.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes (Required at invoice level, up to 99 occurrences)

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
Per change report v1.2, new notes were added to SG25/MOA at Invoice Level. Per v1.3.6, notes were added for enabling the "Perfect Invoice" to carry further Duty/Tax amounts on Commercial Invoice. Low value dutiable shipments to Singapore have specific notes per v1.3.4.

## Claude Confidence
MEDIUM — Required at invoice level with multiple qualifier types for different monetary amounts.

## Review Status
- [ ] Reviewed by human