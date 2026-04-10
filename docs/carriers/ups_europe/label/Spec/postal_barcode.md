# Field: postal_barcode

## Display Name
Postal Barcode

## Field Description
A Code 128 barcode that contains the receiver's postal code. It is one of the five key data elements on the UPS Smart Label, used for routing packages to the correct destination.

## Format & Validation Rules
- **Data Type:** barcode (Code 128)
- **Length:** Up to 15 alphanumeric characters
- **Pattern/Regex:** Domestic: `420` + up to 9-digit destination postal code; International: `421` + 3-digit ISO country code + up to 9-character destination postal code
- **Allowed Values:** EAN-UCC Application Identifier 420 (domestic) or 421 (international) followed by postal code data
- **Required:** yes

## Examples from Spec
- Domestic: `420300768845`
- International: `421124L4V1X5`

## Position on Label
Must print to the right of the MaxiCode™ symbology, beneath the URC and above the Tracking Number Barcode Block.

## ZPL Rendering
- **Typical Position:** Middle of carrier segment, right of MaxiCode, below UPS Routing Code, above tracking barcode
- **Font / Size:** Not specified for human-readable; barcode height minimum 0.5 inches
- **Field Prefix:** None — barcode
- **ZPL Command:** ^BC (Code 128)

## Edge Cases & Notes
- No spaces, parentheses, or dashes should be encoded in the barcode.
- Ensure that both the MaxiCode™ data string and the Postal Barcode have identical postal codes.
- Minimum quiet zone top and bottom = 0.0625 inches.
- Minimum quiet zone left and right = 10 times the X-dimension.
- Height (minimum) = 0.5 inches; Width = Variable.
- See Appendix B for Code 128 specifications and Appendix F for postal code line format matrix.

## Claude Confidence
HIGH — spec provides detailed data content, examples, and dimensional requirements

## Review Status
- [ ] Reviewed by human