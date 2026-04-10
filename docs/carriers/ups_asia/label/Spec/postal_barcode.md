# Field: postal_barcode

## Display Name
Postal Barcode

## Field Description
A Code 128 barcode encoding destination postal code information with GS1 Application Identifiers. Used for postal sorting purposes.

## Format & Validation Rules
- **Data Type:** barcode (Code 128)
- **Length:** up to 15 alphanumeric characters
- **Pattern/Regex:** Domestic: `^420\d{5,9}$`; International: `^421\d{3}[A-Z0-9]{0,9}$`
- **Allowed Values:** Domestic movements: AI 420 + Destination Postal Code (positions 1-3 = 420, positions 4-12 = postal code). International movements: AI 421 + ISO 3-digit Country Code + Destination Postal Code (positions 1-3 = 421, positions 4-6 = ISO country code, positions 7-15 = postal code)
- **Required:** yes

## Examples from Spec
Domestic: `420300768845`
International: `421124L4V1X5`

## Position on Label
To the right of the MaxiCode symbology, beneath the URC and above the Tracking Number Barcode Block.

## Edge Cases & Notes
- No spaces, parentheses or dashes should be encoded into the barcode.
- The MaxiCode data string and the Postal Barcode must have identical postal codes.
- Minimum height = 0.5 inch; width is variable.
- See Appendix B for Code 128 specifications and width information.

## Claude Confidence
HIGH — spec clearly defines format with positional data content and examples

## Review Status
- [ ] Reviewed by human