# Field: piece_count

## Display Name
Piece Count (X OF Y)

## Field Description
Indicates the current package number and total number of packages in the shipment, displayed as "X OF Y" format.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** `\d+\s+OF\s+\d+`
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
"1 OF 1", "1 OF 2", "2 OF 2", "1 OF 3", "2 OF 3", "3 OF 3"

## Position on Label
Upper right area of the label, typically to the right of or on the same line as the package weight.

## Edge Cases & Notes
For single-piece shipments, displays "1 OF 1". For multi-piece shipments, each package label shows its sequential number. Examples show up to 3-piece shipments.

## Claude Confidence
HIGH — field appears consistently across all label examples with clear format

## Review Status
- [ ] Reviewed by human