# Field: uap_city_postal_code

## Display Name
UPS Access Point™ City and Postal Code

## Field Description
The city and postal code of the UPS Access Point location.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — required when shipping to a UPS Access Point location

## Examples from Spec
- `9000 GHENT`

## Position on Label
Ship To section, below UAP street address. Font size 12 pt. bold for the postal line.

## ZPL Rendering
- **Typical Position:** Ship-to section
- **Font / Size:** 12 pt. bold for Postal line and Country
- **Field Prefix:** None (part of address block)
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
The postal line and country use a larger bold font (12 pt. bold) compared to other address lines (10 pt.).

## Claude Confidence
HIGH — Explicitly specified in Access Point label requirements with font size

## Review Status
- [ ] Reviewed by human