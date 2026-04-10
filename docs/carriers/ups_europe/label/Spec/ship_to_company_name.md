# Field: ship_to_company_name

## Display Name
Ship To Company Name

## Field Description
The company name at the destination/consignee address. For Access Point shipments, this is the UPS Access Point facility name.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — required when applicable

## Examples from Spec
"COMPANY NAME", "UPS ACCESS POINT (UAP) NAME", "UPS ACCESS POINT NAME"

## Position on Label
Middle-left area of label, in the ship-to address block.

## ZPL Rendering
- **Typical Position:** Middle-left, ship-to address block
- **Font / Size:** 12 pt Bold per spec
- **Field Prefix:** None — data value
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
For Access Point Direct to Retail labels, the Access Point name is shown instead of the consignee company name.

## Claude Confidence
HIGH — consistently shown in label examples

## Review Status
- [ ] Reviewed by human