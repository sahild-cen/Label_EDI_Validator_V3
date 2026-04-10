# Field: ship_to_consignee_phone_number

## Display Name
Ship To Consignee Phone Number

## Field Description
The telephone number of the consignee/recipient.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes (for Access Point labels)

## Examples from Spec
Label examples show "CONSIGNEE PHONE NUMBER" as placeholder.

## Position on Label
In the Ship To section of the label, below the consignee name.

## ZPL Rendering
- **Typical Position:** Ship-to section, second line after consignee name
- **Font / Size:** 10 pt.
- **Field Prefix:** None (part of address block)
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Specifically called out as required in the Ship To section for Access Point labels.

## Claude Confidence
HIGH — Explicitly listed in Access Point spec requirements

## Review Status
- [ ] Reviewed by human