# Field: shipment_weight

## Display Name
Shipment Weight (SHP WT)

## Field Description
The total weight of the entire shipment (all packages combined), prefixed with "SHP WT:" on the label.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** `\d+(\.\d+)?\s*(KG|LBS)`
- **Allowed Values:** Numeric value followed by unit (KG or LBS)
- **Required:** conditional — appears on multi-piece shipments and most single-piece shipments

## Examples from Spec
"SHP WT: 50.5 KG", "SHP WT: 25 KG", "SHP WT: 8 KG", "SHP WT: 203 KG", "SHP WT: 1542 LBS", "SHP WT: 243 LBS", "SHP WT: 91 KG", "SHP WT: 52 KG", "SHP WT: 20 KG"

## Position on Label
Upper right portion of the label, in the shipment details block below shipment number.

## Edge Cases & Notes
For single-piece shipments, SHP WT equals the package weight. For multi-piece shipments, this is the sum of all package weights. Not all labels show this field (some letter/envelope labels omit it).

## Claude Confidence
HIGH — field appears consistently across most label examples

## Review Status
- [ ] Reviewed by human