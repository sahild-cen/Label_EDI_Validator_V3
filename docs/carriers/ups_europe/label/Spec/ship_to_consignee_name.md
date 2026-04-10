# Field: ship_to_consignee_name

## Display Name
Ship To Consignee Name

## Field Description
The name of the person to whom the package is being shipped. For Access Point labels, this is the name of the person who will pick up the package at the UPS Access Point location.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
Label examples show "CONSIGNEE NAME" as placeholder.

## Position on Label
In the Ship To section of the label. For Access Point labels, appears both in the Ship To block and in the Consignee Address Block at the bottom of the label.

## ZPL Rendering
- **Typical Position:** Ship-to section, below "SHIP TO:" indicator; also at bottom of label for Access Point
- **Font / Size:** 10 pt. for Ship To section; 10 pt. bold for Consignee Address Block name
- **Field Prefix:** "SHIP TO:" label appears to the left of the section
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
For Access Point labels, the consignee name appears in two locations: in the Ship To section alongside the Access Point address, and separately in the Consignee Address Block at the bottom. The consignee may be required to produce sufficient verification of name/address based on shipment type.

## Claude Confidence
HIGH — Spec explicitly describes this field with formatting requirements

## Review Status
- [ ] Reviewed by human