# Field: barcode_block

## Display Name
Barcode Block

## Field Description
A standardized unit of area on the label in which bar-coded information is presented. Barcode blocks are typically stacked vertically and separated from each other by horizontal lines.

## Format & Validation Rules
- **Data Type:** graphic/structured area
- **Length:** N/A
- **Pattern/Regex:** N/A
- **Allowed Values:** Contains barcode symbol(s) and associated human-readable interpretation
- **Required:** yes

## Examples from Spec
No examples in spec.

## Position on Label
Stacked vertically on the label, separated by horizontal separating lines.

## Edge Cases & Notes
- Each barcode block contains a specific barcode and its human-readable interpretation.
- Highlighting bars bound the UPS Barcode block specifically.

## Claude Confidence
HIGH — Definitions section explicitly describes barcode block structure and layout.

## Review Status
- [x] Reviewed by human