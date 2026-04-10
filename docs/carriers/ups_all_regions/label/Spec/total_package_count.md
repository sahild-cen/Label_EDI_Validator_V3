# Field: total_package_count

## Display Name
Total Package Count

## Field Description
The total number of packages in the consolidated shipment, printed on the summary label. Uses "TOTAL PKG #:" format for Paperless Invoice labels and "PKG/PLT #:" for Single Label summary.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** `TOTAL PKG #: [0-9]{1,3}` or `TOTAL PKG/PLT #: [0-9]{1,3}`
- **Allowed Values:** Not restricted
- **Required:** yes — on summary labels

## Examples from Spec
- "TOTAL PKG #: 6"
- "PKG/PLT #: 123"

## Position on Label
On the summary label. Font Size = 12 pt.

## Edge Cases & Notes
Paperless Invoice Summary format: positions 1-5 = "TOTAL", position 6 = space, positions 7-9 = "PKG", positions 9-10 = "#:", position 11 = space, positions 12-14 = three numeric. Single Label Summary format uses "PKG/PLT" instead of just "PKG" to account for pallets.

## Claude Confidence
HIGH — spec provides explicit positional content and examples for both variants

## Review Status
- [ ] Reviewed by human