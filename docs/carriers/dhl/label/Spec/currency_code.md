# Field: currency_code

## Display Name
Currency Code

## Field Description
The ISO currency code indicating the currency used for the declared value of service.

## Format & Validation Rules
- **Data Type:** string
- **Length:** 3 characters
- **Pattern/Regex:** `[A-Z]{3}` (ISO 4217)
- **Allowed Values:** Standard ISO currency codes (e.g., "EUR")
- **Required:** conditional — when a value of service is declared

## Examples from Spec
- "EUR"

## Position on Label
Appears alongside the value of service on the transport label or waybill.

## Edge Cases & Notes
- Standard ISO 4217 currency code format.

## Claude Confidence
MEDIUM — Format is standard ISO, though only one example is shown in the extracted text.

## Review Status
- [ ] Reviewed by human