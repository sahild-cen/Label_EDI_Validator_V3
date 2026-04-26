# Field: package_count

## Display Name
Package Count

## Group Description
Indicates the number of this package relative to the total number of packages in the entire shipment, displayed in the top-right corner of the label.

## Sub-Fields

### package_count
- **Data Type:** alphanumeric
- **Length:** 10 (format: "N OF X")
- **Pattern/Regex:** `^\d{1,3}\sOF\s\d{0,3}$`
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Package count in format "N OF X" where N is the current package number and X is the total number of packages in the shipment
- **Detect By:** spatial:top_right, text matching pattern "N OF X"
- **Position on Label:** top-right corner of the label
- **ZPL Font:** 10pt bold
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Examples from Spec
- `999 OF 999`
- `1 OF 1`
- `1 OF 2`
- `1 OF __` (when total not known at print time)

## Edge Cases & Notes
- Positions 1-3 = up to three numeric, Position 4 = space, Positions 5-6 = "OF", Position 7 = space, Positions 8-10 = up to three numeric
- For multi-piece shipments where total is unknown at print time, display as `1 OF __` or `2 OF __`

## Claude Confidence
HIGH — spec clearly defines format with positional data and examples

## Review Status
- [x] Reviewed by human