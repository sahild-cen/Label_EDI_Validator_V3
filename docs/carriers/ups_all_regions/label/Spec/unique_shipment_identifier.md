# Field: unique_shipment_identifier

## Display Name
Unique Shipment Identifier (USI)

## Field Description
A mandatory identifier that uniquely identifies the shipment. The USI is used for UPS Worldwide Express Freight and UPS SurePost labels.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 15 characters total (including "USI: " prefix)
- **Pattern/Regex:** `USI: [0-9]{9}[0-9T]` — Positions 1-4 = "USI:", Position 5 = space, Positions 6-14 = 9 numeric digits, Position 15 = check digit (numeric or letter "T")
- **Allowed Values:** 9 numeric digits followed by a check digit (numeric or "T")
- **Required:** yes — mandatory for Express Freight and SurePost labels

## Examples from Spec
- `USI: 840000028T`

## Position on Label
Must print left justified. For SurePost labels, it must print right justified on the same line as the USPS Ship To five digit postal code in the UPS Address Block.

## Edge Cases & Notes
Check digit can be numeric or the letter "T". The spec references Appendix A for the check digit calculation example. For SurePost, the USI positioning requirement differs (right justified on postal code line) compared to Express Freight (left justified).

## Claude Confidence
HIGH — Detailed format specification with positions, data content, and examples clearly provided.

## Review Status
- [ ] Reviewed by human