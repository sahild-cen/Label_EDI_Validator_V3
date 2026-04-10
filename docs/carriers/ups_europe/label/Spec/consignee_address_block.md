# Field: consignee_address_block

## Display Name
Consignee Address Block (Bottom of Label)

## Field Description
On Access Point labels, the consignee's personal address is printed at the very bottom of the label, separate from the Ship To Access Point address. This block includes the consignee name, extended address, street address, city/postal code, and country.

## Format & Validation Rules
- **Data Type:** string (multi-line block)
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — required for Access Point labels

## Examples from Spec
From label diagrams:
- CONSIGNEE NAME
- EXTENDED ADDRESS
- STREET ADDRESS
- CITY POSTAL CODE
- COUNTRY NAME

From specific example:
- `WINDSOR ON N8N2M1` (city/state/postal)
- `CANADA` (country)

## Position on Label
At the very bottom of the label, separated by horizontal lines (minimum 0.03 inches) above the Consignee Name text and below the Consignee Country.

## ZPL Rendering
- **Typical Position:** Bottom of label
- **Font / Size:** 10 pt. bold for Consignee Name; 10 pt. for remaining lines
- **Field Prefix:** None (address block; horizontal rule separators above and below)
- **ZPL Command:** ^FD (text field) for each line; ^GB for horizontal lines

## Edge Cases & Notes
This is a distinct address block specific to Access Point labels. Horizontal lines must be minimum 0.03 inches, placed above the Consignee Name and below the Consignee Country. This is the delivery address of the actual recipient, not the Access Point address.

## Claude Confidence
HIGH — Spec explicitly describes format, positioning, and font requirements

## Review Status
- [ ] Reviewed by human