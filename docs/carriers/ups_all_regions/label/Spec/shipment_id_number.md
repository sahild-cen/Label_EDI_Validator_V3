# Field: shipment_id_number

## Display Name
Shipment ID Number (SHP#)

## Field Description
A unique identifier for the overall shipment, which may contain multiple packages. This links all packages in a multi-piece shipment together.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — appears on international and multi-piece shipments

## Examples from Spec
- `1X2X 3X33 3TT`
- `1X2X 3X7R CDG`
- `1X2X3X33 3TS`
- `1X2X3X 9TT`
- `1X2X3X 9X4`
- `1X2X3X 19K`
- `1X2X3X 9VM`
- `1X2X 3X33 3VP`
- `1X2X3X 7HP3K`
- `1X2X 3X33 9TT`
- `1X2X 3XTT M4H`

## Position on Label
Top right section of the label, preceded by "SHP#:" or "SHP #:".

## Edge Cases & Notes
The field label varies slightly between "SHP#:" and "SHP #:" (with space). Not present on all domestic US labels (e.g., some domestic Ground labels omit it). Present on most international labels.

## Claude Confidence
HIGH — Consistently present on international labels with clear "SHP#:" prefix.

## Review Status
- [ ] Reviewed by human