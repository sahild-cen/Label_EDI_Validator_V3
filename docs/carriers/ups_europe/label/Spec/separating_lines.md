# Field: separating_lines

## Display Name
Separating Lines

## Field Description
Narrow lines used to segregate barcode and information blocks on the label. These provide visual structure and separation between different label zones.

## Format & Validation Rules
- **Data Type:** graphic
- **Length:** Not applicable — graphical element
- **Pattern/Regex:** Not applicable
- **Allowed Values:** Narrow black lines
- **Required:** yes

## Examples from Spec
No visual examples in extracted text.

## Position on Label
Between barcode blocks and information blocks throughout the label.

## ZPL Rendering
- **Typical Position:** Between label sections/zones
- **Font / Size:** Not applicable
- **Field Prefix:** None — graphic
- **ZPL Command:** ^GB (graphic box) — narrow horizontal lines

## Edge Cases & Notes
- Distinct from highlighting bars which are thicker (0.1 inch) and specifically frame the barcode block.

## Claude Confidence
MEDIUM — Defined in glossary but no specific dimensions or exact positions in extracted text.

## Review Status
- [ ] Reviewed by human