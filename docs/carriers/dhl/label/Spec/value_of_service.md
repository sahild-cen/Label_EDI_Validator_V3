# Field: value_of_service

## Display Name
Value of Service (Declared Value)

## Field Description
The declared monetary value associated with a value-added service (e.g., insured value for delivery signature).

## Format & Validation Rules
- **Data Type:** numeric (decimal)
- **Length:** Variable
- **Pattern/Regex:** Not specified in spec; example shows format with space as thousands separator and period for decimals
- **Allowed Values:** Monetary value
- **Required:** conditional — when a value-added service requiring a declared value is selected

## Examples from Spec
- "1 000.00" EUR for Delivery Signature service

## Position on Label
Appears alongside the product service code on the transport label or waybill.

## Edge Cases & Notes
- Currency code accompanies the value (see currency_code field).

## Claude Confidence
LOW — Only one example provided; full specification not in extracted text.

## Review Status
- [ ] Reviewed by human