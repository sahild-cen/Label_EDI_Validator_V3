# Field: package_count

## Display Name
Package Count

## Field Description
Indicates the number of the package N related to the number of packages in the entire shipment X (e.g., N of X). For over-labels, only N prints. For the document box, the complete N of X prints.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** For document box: `[0-9]{1,3} OF [0-9]{1,3}`; For child packages: `PKG# [0-9]{1,3}`
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- "1 OF 10" (document box)
- "1 OF 5" (label example)
- "PKG# 3" (child package over-label)
- "PKG# 1" / "PKG# 6" (over-label examples)

## Position on Label
Upper right corner area of the label. Font Size = 12-14 pt.

## Edge Cases & Notes
Document box label: positions 1 = numeric, position 2 = space, positions 3-4 = "OF", position 5 = space, positions 6-8 = up to three numeric. Child packages: positions 1-4 = "PKG#", position 5 = space, positions 6-8 = up to three numeric. The summary label uses "TOTAL PKG #:" format instead.

## Claude Confidence
HIGH — spec provides detailed positional format and multiple examples

## Review Status
- [ ] Reviewed by human