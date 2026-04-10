# Field: dhl_logo

## Display Name
DHL Logo

## Field Description
The official DHL carrier logo printed on the transport label, following DP-DHL Standard Brand and Design Guidelines.

## Format & Validation Rules
- **Data Type:** image
- **Length:** N/A
- **Pattern/Regex:** Not applicable
- **Allowed Values:** Official DHL logo per DP-DHL Brand and Design Guidelines; black & white version sufficient for transport labels
- **Required:** yes — mandatory

## Examples from Spec
No examples in spec.

## Position on Label
Upper right corner of the label. Associated information (e.g., a particular DHL Country Organization) can be printed directly below the logo.

## Edge Cases & Notes
- For transport labels, black & white version is sufficient
- When using labels with a pre-printed logo, official DP-DHL brand color specifications must be followed
- Any DHL-owned customer automation system must be able to print the logo as an image
- Only if it is not possible to insert images may the equivalent text be printed in plain text instead

## Claude Confidence
HIGH — spec clearly states placement, format, and mandatory status

## Review Status
- [ ] Reviewed by human