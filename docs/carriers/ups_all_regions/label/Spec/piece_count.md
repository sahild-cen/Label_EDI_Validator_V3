# Field: piece_count

## Display Name
Piece Count (Package N of X)

## Field Description
Indicates the package number within the total number of packages in the shipment, displayed in "N OF X" format.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** `\d+\sOF\s\d+`
- **Allowed Values:** N must be between 1 and X; X is total package count
- **Required:** yes

## Examples from Spec
- `1 OF 1`
- `1 OF 2`
- `1 OF 5`
- `2 OF 2` (implied from multi-package examples)

## Position on Label
Top right area of the label, near the package weight.

## Edge Cases & Notes
For single-package shipments, this is always "1 OF 1". For multi-piece shipments, each package gets a sequential number. This field is sometimes referred to as "Package Count Number" in the spec annotations.

## Claude Confidence
HIGH — Consistently present in all label examples.

## Review Status
- [ ] Reviewed by human