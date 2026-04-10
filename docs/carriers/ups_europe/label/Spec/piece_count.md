# Field: piece_count

## Display Name
Piece Count (Package X of Y)

## Field Description
Indicates the package number within a multi-piece shipment, showing the current piece and total piece count (e.g., "1 OF 3").

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** `\d+ OF \d+`
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
"1 OF 1", "1 OF 2", "2 OF 2", "1 OF 3", "2 OF 3", "3 OF 3"

## Position on Label
Top-right area of the label, on the same line as the package weight.

## ZPL Rendering
- **Typical Position:** Top-right, adjacent to or on same line as weight
- **Font / Size:** 12 pt Bold per spec
- **Field Prefix:** None — format is "X OF Y"
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
For single-piece shipments, always shows "1 OF 1". Multi-piece shipments increment the first number while maintaining the total count. Each piece in a multi-piece shipment gets its own tracking number.

## Claude Confidence
HIGH — consistently shown on all label examples with clear format

## Review Status
- [ ] Reviewed by human