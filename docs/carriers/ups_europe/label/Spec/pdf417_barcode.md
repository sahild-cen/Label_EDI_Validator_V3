# Field: pdf417_barcode

## Display Name
PDF417 Barcode

## Group Description
A PDF417 barcode that must print on the shipping label when required. The spec references a separate "PDF417 Barcode Symbology" document for full details.

## Sub-Fields

### pdf417_symbol
- **Data Type:** barcode
- **Length:** variable (per PDF417 Barcode Symbology document)
- **Pattern/Regex:** Not specified in spec (refers to separate document)
- **Allowed Values:** Not specified in spec
- **Required:** conditional — must print when required
- **Description:** PDF417 2D barcode printed on the shipping label. Full specifications are in a separate PDF417 Barcode Symbology document.
- **Detect By:** zpl_command:^B7, visual:stacked linear barcode pattern
- **Position on Label:** on the shipping label (exact position not specified in this extract)
- **ZPL Font:** Not applicable (barcode)
- **Field Prefix:** None
- **ZPL Command:** ^B7 (PDF417 barcode)

## Examples from Spec
No specific data content examples provided in this extracted spec. Spec states: "For details on the PDF417 Barcode, please refer to the PDF417 Barcode Symbology document."

## Edge Cases & Notes
- The PDF417 is described as conditional — "must print on the shipping label when required."
- Full specifications are deferred to a separate document not included in this extract.
- Mentioned for both 4x6 and 4x4.25 label formats.

## Claude Confidence
LOW — Spec only mentions PDF417 must print when required and defers to a separate document for details.

## Review Status
- [x] Reviewed by human