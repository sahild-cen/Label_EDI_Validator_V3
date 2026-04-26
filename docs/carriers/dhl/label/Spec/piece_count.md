# Field: piece_count

## Display Name
Piece Count (Piece Number / Total Pieces)

## Field Description
Indicates the piece number and total number of pieces in a multi-piece shipment. Displayed as "X of Y" format (e.g., "1 of 3") to identify individual pieces within a shipment.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable, typically "X of Y" format
- **Pattern/Regex:** ^\d+ of \d+$ or ^\d+/\d+$
- **Allowed Values:** Positive integers where piece number ≤ total pieces
- **Required:** yes

## Examples from Spec
No examples in extracted spec text.

## ZPL Rendering
- **Typical Position:** mid to lower section of label, near weight information
- **Font / Size:** Not specified
- **Field Prefix:** "Piece:" or "Pcs:" or similar
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
For single-piece shipments, this typically shows "1 of 1" or "1/1". In multi-piece shipments, each piece label has a unique piece number but shares the same master AWB number. DHL may also use the term "number of pieces" or "NOP".

## Claude Confidence
MEDIUM — standard DHL label field

## Review Status
- [ ] Reviewed by human