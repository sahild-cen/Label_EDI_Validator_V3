# Field: billing_indicator

## Display Name
Billing Indicator

## Field Description
Indicates the billing method for the shipment (e.g., prepaid, collect, third-party).

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** `P/P` (Prepaid) shown in all examples; other values likely exist but not shown in extracted text
- **Required:** yes

## Examples from Spec
- `BILLING: P/P`

## Position on Label
Below the tracking number area, prefixed with "BILLING:".

## Edge Cases & Notes
All examples show "P/P" (prepaid). Other billing types (collect, third-party) may use different codes but are not shown in the extracted text.

## Claude Confidence
HIGH — Consistently shown on all label examples, though only one value is demonstrated.

## Review Status
- [x] Reviewed by human