# Field: urc_version_number

## Display Name
URC Version Number

## Field Description
The version number of the UPS Routing Code data file used to generate the routing information on the label.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- `18.5A 01/2020`

## Position on Label
Located at the bottom of the Carrier Segment, typically in the lower-right area beneath the description of goods.

## ZPL Rendering
- **Typical Position:** Bottom-right of carrier segment
- **Font / Size:** 6pt
- **Field Prefix:** None — displayed as version string
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
- The URC data file must be updated monthly to ensure the most accurate routing information.
- The label sample annotations explicitly label this as "URC Version Number."
- Format appears to be version number followed by date (MM/YYYY).

## Claude Confidence
MEDIUM — spec labels it in the diagram and shows examples but provides limited format details

## Review Status
- [ ] Reviewed by human