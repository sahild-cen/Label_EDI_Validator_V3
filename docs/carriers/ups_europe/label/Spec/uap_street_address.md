# Field: uap_street_address

## Display Name
UPS Access Point™ Street Address

## Field Description
The street address of the UPS Access Point location.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — required when shipping to a UPS Access Point location

## Examples from Spec
Label examples show "UAP STREET ADDRESS" as placeholder.

## Position on Label
Ship To section, below UAP extended address.

## ZPL Rendering
- **Typical Position:** Ship-to section
- **Font / Size:** 10 pt.
- **Field Prefix:** None (part of address block)
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Required for Access Point shipments.

## Claude Confidence
HIGH — Listed in Access Point label requirements

## Review Status
- [ ] Reviewed by human