# Field: piece_count

## Display Name
Piece Count (Package X of Y)

## Group Description
Indicates which package this label represents out of the total number of packages in the shipment.

## Sub-Fields

### piece_indicator
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** `^\d+\s+OF\s+\d+$`
- **Allowed Values:** Not restricted (format: "N OF M" where N ≤ M)
- **Required:** yes
- **Description:** Package sequence number out of total package count (e.g., "1 OF 1", "2 OF 3")
- **Detect By:** text_match:OF, spatial:top_right
- **Position on Label:** top-right, next to or near weight
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Examples from Spec
- "1 OF 1"
- "1 OF 2"
- "2 OF 2"
- "1 OF 3"
- "2 OF 3"
- "3 OF 3"

## Edge Cases & Notes
- Multi-piece shipments show sequential numbering (e.g., 1 OF 3, 2 OF 3, 3 OF 3).
- Each piece in a multi-piece shipment gets its own label with unique tracking number.

## Claude Confidence
HIGH — Consistently appears across all label examples.

## Review Status
- [x] Reviewed by human