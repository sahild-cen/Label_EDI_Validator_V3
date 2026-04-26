# Field: pickup_summary_barcode

## Display Name
Pickup Summary Barcode Report

## Group Description
A barcode report generated as part of the pickup summary process, submitted alongside shipping labels during certification.

## Sub-Fields

### pickup_summary_barcode
- **Data Type:** barcode
- **Length:** Variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not specified
- **Required:** conditional — required if the application supports it
- **Description:** A Pickup Summary Barcode report that accompanies the shipping label submission. At least one must be submitted during the label certification process if the application supports generating it.
- **Detect By:** Not specified (separate report, not on shipping label)
- **Position on Label:** Not on shipping label (separate document)
- **ZPL Font:** Not applicable
- **Field Prefix:** None
- **ZPL Command:** Not specified

## Examples from Spec
No examples in spec (this extract).

## Edge Cases & Notes
- This is a supplementary document, not a field on the shipping label itself.
- Required only during the certification process and only if the shipping application supports it.

## Claude Confidence
LOW — Mentioned only in the certification process; minimal technical detail provided.

## Review Status
- [x] Reviewed by human