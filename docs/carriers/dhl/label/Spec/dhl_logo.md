# Field: dhl_logo

## Display Name
DHL Logo

## Field Description
The DHL carrier logo placed in the upper right corner of the transport label. It is a mandatory visual element for brand identification. Associated information (e.g., a particular DHL Country Organization) can be printed directly below the logo.

## Format & Validation Rules
- **Data Type:** graphic/image
- **Length:** N/A
- **Pattern/Regex:** N/A
- **Allowed Values:** Official DP-DHL brand logo per Standard Brand and Design Guidelines
- **Required:** yes

## Examples from Spec
"For transport labels, the black & white version of the logo is sufficient. When using labels with a pre-printed logo, the official DP DHL brand color specifications for the logo have to be followed."

## ZPL Rendering
- **Typical Position:** upper right corner of the label
- **Font / Size:** N/A — graphic element
- **Field Prefix:** None
- **ZPL Command:** ^GFA (graphic field) or equivalent image command; if not possible to insert images, equivalent text may be printed in plain text instead

## Edge Cases & Notes
Any DHL-owned customer automation system must be able to print the logo as an image. Only if it is not possible to insert images into the label may the equivalent text be printed in plain text instead. Must follow official DP-DHL Standard Brand and Design Guidelines.

## Claude Confidence
HIGH — clearly specified as mandatory with positioning

## Review Status
- [ ] Reviewed by human