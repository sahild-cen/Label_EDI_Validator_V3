# Field: country_specific_codes

## Display Name
Country-Specific / Region-Specific Codes

## Field Description
An optional field in the routing barcode for domestic use only, providing additional region-specific routing information after the product/feature block.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** Variable — up to 6 numeric characters or up to 2 alphabetic characters
- **Pattern/Regex:** `(\d{1,6}|[A-Za-z]{1,2})?`
- **Allowed Values:** Country/region-specific; example: street and house number code for Germany
- **Required:** no (optional; may remain empty)

## Examples from Spec
- `123456` — Region-specific codes for Belgium EUROPACK example
- `556677` — Street and house number for Germany DOM EUROPACK example

## Position on Label
Within the routing barcode, after an optional "+" field separator following the product/feature block.

## Edge Cases & Notes
- The field separator before this section is optional (FNC1 in ASC MH10, "+" in GS1). If no country-specific codes exist, both the separator and this field may be omitted entirely.
- For domestic shipments only.

## Claude Confidence
HIGH — Spec provides clear format constraints and examples.

## Review Status
- [ ] Reviewed by human