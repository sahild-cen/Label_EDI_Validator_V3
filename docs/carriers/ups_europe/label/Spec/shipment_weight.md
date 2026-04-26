# Field: shipment_weight

## Display Name
Shipment Weight (SHP WT)

## Group Description
The total weight of the entire shipment (all packages combined), displayed with "SHP WT:" prefix. For multi-piece shipments, this is the aggregate weight.

## Sub-Fields

### shipment_weight
- **Data Type:** numeric
- **Length:** variable
- **Pattern/Regex:** `^\d+(\.\d+)?\s*KG$`
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Total actual weight of the entire shipment in kilograms
- **Detect By:** text_prefix:SHP WT:
- **Position on Label:** upper-right area, shipment information section
- **ZPL Font:** Not specified
- **Field Prefix:** "SHP WT:"
- **ZPL Command:** ^FD (text field)

## Examples from Spec
- `SHP WT: 91 KG`
- `SHP WT: 45 KG`
- `SHP WT: 50.5 KG`
- `SHP WT: 20 KG`
- `SHP WT: 38 KG`

## Edge Cases & Notes
- SHP DWT (dimensional weight) does not always appear — it is absent from some label examples (e.g., UPS Express Freight, UPS Saver envelope)
- Both SHP WT and SHP DWT may have the same value
- May include decimal places

## Claude Confidence
HIGH — Clearly shown with prefixes across multiple label examples.

## Review Status
- [x] Reviewed by human