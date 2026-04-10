# Field: tracking_number_abbreviated

## Display Name
Tracking Number (Last 3 Digits)

## Field Description
The last three digits of the shipment's virtual document box 1Z tracking number, printed on over-labels, child packages, and summary labels for World Ease consolidated shipments.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 3 digits
- **Pattern/Regex:** `[0-9]{3}`
- **Allowed Values:** Not restricted
- **Required:** yes — for World Ease over-labels and summary labels

## Examples from Spec
- "TRKG# 775" (over-label format)
- "TRKG #: 123" (summary label format)
- "TRKG# 763"

## Position on Label
On over-labels: positions 1-5 = "TRKG#", position 6 = space, positions 7-9 = three numeric. On summary labels: positions 1-4 = "TRKG", position 5 = space, positions 6-7 = "#:", position 8 = space, positions 9-11 = three numeric. Font Size = 12 pt.

## Edge Cases & Notes
The format differs between over-labels ("TRKG# 775") and summary labels ("TRKG #: 123"). Over-labels use "TRKG#" while summary labels use "TRKG #:" with different spacing.

## Claude Confidence
HIGH — spec provides explicit positional data content and examples for both formats

## Review Status
- [ ] Reviewed by human