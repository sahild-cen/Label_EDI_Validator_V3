# Field: uap_name

## Display Name
UPS Access Point™ Name

## Field Description
The name of the UPS Access Point location where the package will be held for pickup.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — required when shipping to a UPS Access Point location

## Examples from Spec
Label examples show "UPS ACCESS POINT (UAP) NAME" as placeholder.

## Position on Label
Ship To section, below consignee phone number and above UAP address lines.

## ZPL Rendering
- **Typical Position:** Ship-to section
- **Font / Size:** 10 pt.
- **Field Prefix:** None (part of address block)
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Only appears on Access Point labels. The UAP name identifies the specific retail or Access Point location.

## Claude Confidence
HIGH — Explicitly described in Access Point specifications

## Review Status
- [ ] Reviewed by human