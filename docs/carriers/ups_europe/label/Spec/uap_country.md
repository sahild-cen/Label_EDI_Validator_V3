# Field: uap_country

## Display Name
UPS Access Point™ Country

## Field Description
The country of the UPS Access Point location.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Country names
- **Required:** conditional — required when shipping to a UPS Access Point location

## Examples from Spec
No explicit UAP country example, but "COUNTRY NAME" placeholder shown in label diagrams.

## Position on Label
Ship To section, below city/postal code line.

## ZPL Rendering
- **Typical Position:** Ship-to section, last line of UAP address
- **Font / Size:** 12 pt. bold
- **Field Prefix:** None (part of address block)
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Uses same 12 pt. bold font as the postal code line.

## Claude Confidence
HIGH — Explicitly listed in Access Point label requirements

## Review Status
- [ ] Reviewed by human