# Field: package_count

## Display Name
Package Count

## Field Description
Indicates the number of this package (N) related to the total number of packages in the entire shipment (X), displayed as "N OF X".

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 10 positions max
- **Pattern/Regex:** Positions 1-3 = up to three numeric; Position 4 = space; Positions 5-6 = "OF"; Position 7 = space; Positions 8-10 = up to three numeric
- **Allowed Values:** Format: N OF X where N and X are numeric (1-999)
- **Required:** yes

## Examples from Spec
- `999 OF 999`
- `1 OF 1`
- `1 OF 2`

## Position on Label
Top right corner of the label, in the Package Information Block.

## ZPL Rendering
- **Typical Position:** Top-right corner, adjacent to package weight
- **Font / Size:** 10pt bold
- **Field Prefix:** None — displayed as "N OF X"
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
- For multi-package shipments where total package count is not known at label print time, display as "1 OF __" or "2 OF __", etc.

## Claude Confidence
HIGH — spec provides detailed positional data content and examples

## Review Status
- [ ] Reviewed by human