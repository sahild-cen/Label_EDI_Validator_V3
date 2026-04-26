# Field: highlighting_bars

## Display Name
Highlighting Bars

## Group Description
One-tenth inch solid black lines located immediately above and below the UPS Barcode block to visually delineate the barcode area.

## Sub-Fields

### highlighting_bars
- **Data Type:** barcode (graphic element)
- **Length:** Not applicable (visual element, one-tenth inch height)
- **Pattern/Regex:** Not applicable
- **Allowed Values:** Solid black lines
- **Required:** yes (implied by definition as structural label element)
- **Description:** Solid black horizontal lines (0.1 inch thick) placed immediately above and below the UPS barcode block. They visually separate the barcode block from other label content.
- **Detect By:** spatial:barcode_block_border
- **Position on Label:** Immediately above and below the UPS Barcode block
- **ZPL Font:** Not applicable
- **Field Prefix:** None
- **ZPL Command:** ^GB (graphic box) or ^FO with line drawing

## Examples from Spec
No examples in spec (this extract).

## Edge Cases & Notes
- These are structural/visual elements, not data-carrying fields.
- The spec defines them as exactly one-tenth inch (0.1") solid black lines.

## Claude Confidence
MEDIUM — Definition is clear; exact ZPL implementation not specified in this extract.

## Review Status
- [x] Reviewed by human