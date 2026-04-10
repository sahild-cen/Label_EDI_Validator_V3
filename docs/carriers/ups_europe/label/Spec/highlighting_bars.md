# Field: highlighting_bars

## Display Name
Highlighting Bars

## Field Description
One-tenth inch solid black lines located immediately above and below the UPS Barcode block. These visual markers help identify and frame the barcode area on the label.

## Format & Validation Rules
- **Data Type:** graphic
- **Length:** Not applicable — graphical element
- **Pattern/Regex:** Not applicable
- **Allowed Values:** Solid black lines, 0.1 inch thickness
- **Required:** yes

## Examples from Spec
No visual examples in extracted text.

## Position on Label
Immediately above and below the UPS Barcode block.

## ZPL Rendering
- **Typical Position:** Directly above and below the primary tracking number barcode
- **Font / Size:** Not applicable
- **Field Prefix:** None — graphic
- **ZPL Command:** ^GB (graphic box) — solid black lines drawn at 0.1 inch height spanning barcode width

## Edge Cases & Notes
- These are distinct from separating lines, which are narrow lines used to segregate barcode and information blocks.

## Claude Confidence
HIGH — Clearly defined in glossary with specific dimensions (0.1 inch solid black lines, positioned above and below barcode block).

## Review Status
- [ ] Reviewed by human