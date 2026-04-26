# Field: handling_feature_code

## Display Name
Handling Feature Code(s)

## Field Description
A 3-digit numeric code in the routing barcode representing the sum of values of all product features selected for the shipment. Multiple features are combined by summing their individual numeric values. When no features are chosen, the code is "000".

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 3 digits (fixed length, with leading zeroes)
- **Pattern/Regex:** `\d{3}`
- **Allowed Values:** Sum of individual feature values; "000" when no features selected. Example individual values include 001 (Customs Clearance), and others that sum to combined codes.
- **Required:** yes — mandatory in routing barcode; must be "000" if no features selected

## Examples from Spec
- `000` — No features (Germany DOM EUROPACK example)
- `001` — Customs Clearance (Switzerland ECONOMY SELECT example)
- `002` — Feature value 002 (Belgium EUROPACK example)
- `081` — Sum of features 1+16+64 = 81 (Netherlands EXPRESS WORLDWIDE example)

## ZPL Rendering
- **Typical Position:** Encoded within routing barcode; part of human-readable routing code
- **Font / Size:** Not specified
- **Field Prefix:** None — positional within routing string
- **ZPL Command:** Encoded within routing barcode (^BC)

## Edge Cases & Notes
- Multiple features are summed into a single 3-digit value (e.g., 1+16+64 = 081).
- Always padded with leading zeroes to 3 digits.
- Part of the fixed 8-digit product/feature block in the routing barcode.

## Claude Confidence
HIGH — explicitly defined with examples showing the additive feature coding system

## Review Status
- [ ] Reviewed by human