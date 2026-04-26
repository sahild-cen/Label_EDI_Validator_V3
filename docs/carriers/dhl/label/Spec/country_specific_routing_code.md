# Field: country_specific_routing_code

## Display Name
Country-Specific / Region-Specific Routing Code

## Field Description
An optional extension to the routing barcode for domestic routing purposes. Contains variable-length codes specific to the destination country's internal routing requirements, such as street and house number information.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** Variable — up to 6 numeric characters or up to 2 alphabetic characters
- **Pattern/Regex:** `(\d{1,6}|[A-Za-z]{1,2})?`
- **Allowed Values:** Country-specific; for domestic use only
- **Required:** no — optional, may remain empty

## Examples from Spec
- `123456` — Region-specific code in Belgium EUROPACK example
- `556677` — Street and house number routing code in Germany DOM EUROPACK example

## ZPL Rendering
- **Typical Position:** Encoded within routing barcode after second "+" separator; part of human-readable routing code
- **Font / Size:** Not specified
- **Field Prefix:** Preceded by "+" separator (which is FNC1 in Code 128 or "+" in GS1-128)
- **ZPL Command:** Encoded within routing barcode (^BC)

## Edge Cases & Notes
- The "+" separator before this field is optional and may remain empty if no country-specific codes exist.
- For domestic use only.
- In Code 128, the separator before this field is the FNC1 special character; in GS1-128, it is a literal "+".

## Claude Confidence
HIGH — explicitly defined in routing barcode structure with examples

## Review Status
- [x] Reviewed by human