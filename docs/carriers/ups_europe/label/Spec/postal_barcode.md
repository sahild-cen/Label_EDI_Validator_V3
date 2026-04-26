# Field: postal_barcode

## Display Name
Postal Barcode

## Group Description
A Code 128 barcode containing the receiver's postal code. It prints to the right of the MaxiCode symbology, beneath the URC and above the Tracking Number Barcode Block. This is one of the five key data elements of the UPS Smart Label.

## Sub-Fields

### postal_barcode
- **Data Type:** barcode
- **Length:** variable (up to 15 alphanumeric)
- **Pattern/Regex:** Domestic: `^420\d{5,9}$`; International: `^421\d{3}[A-Z0-9]{1,9}$`
- **Allowed Values:** Not restricted — EAN-UCC Application Identifier + country code (international) + destination postal code
- **Required:** yes
- **Description:** Code 128 barcode encoding the destination postal code with EAN-UCC application identifier prefix
- **Detect By:** barcode_data:^420 or ^421, zpl_command:^BC
- **Position on Label:** right of MaxiCode, beneath URC, above tracking number barcode block
- **ZPL Font:** Not applicable (barcode)
- **Field Prefix:** None
- **ZPL Command:** ^BC (Code 128 barcode)

## Examples from Spec
- Domestic: `420300768845` (AI 420 + postal code 300768845)
- International: `421124L4V1X5` (AI 421 + ISO 3-digit country code 124 + postal code L4V1X5)

## Edge Cases & Notes
- Domestic movements: Positions 1-3 = "420" (EAN-UCC AI), Positions 4-12 = destination postal code
- International movements: Positions 1-3 = "421" (EAN-UCC AI), Positions 4-6 = ISO 3-digit country code, Positions 7-15 = destination postal code (up to 9 alphanumeric)
- No spaces, parentheses, or dashes should be encoded in the barcode
- Ensure that both the MaxiCode data string and the Postal Barcode have identical postal codes
- Minimum height = 0.5 inches; width = variable
- See Appendix B for Code 128 specifications

## Claude Confidence
HIGH — spec provides detailed data content format, examples, and encoding rules

## Review Status
- [x] Reviewed by human