# Field: trading_transaction_type

## Display Name
Trading Transaction Type

## Field Description
A free text segment (SG33 Invoice Level - FTX) to specify Trading Transaction Type as supplementary information related to governmental procedures.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — up to 9 occurrences at invoice-level SG33

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
Only appears at invoice level within SG33, following the GOR segment.

## Claude Confidence
MEDIUM — Explicitly described in invoice-level SG33 FTX.

## Review Status
- [ ] Reviewed by human