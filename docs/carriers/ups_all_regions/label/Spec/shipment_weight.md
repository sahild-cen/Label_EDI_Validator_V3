# Field: shipment_weight

## Display Name
Shipment Weight (SHP WT)

## Field Description
The total actual weight of the shipment, rounded to the next whole pound or kilogram. Displayed on both World Ease labels and Trade Direct LTL/TL pallet labels.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** `SHP WT: [0-9]{1,5} (LBS|KG)`
- **Allowed Values:** Not restricted (unit must be LBS or KG)
- **Required:** yes

## Examples from Spec
- "SHP WT: 49 LBS"
- "SHP WT: 1250 LBS"
- "SHP WT: 100 LBS"
- "SHP WT: 120 KG"
- "SHP WT: 1000 KG"
- "SHP WT: 2500 LBS"

## Position on Label
For World Ease: in the shipment information area. For Trade Direct LTL/TL: directly beneath the pallet count. Data content: positions 1-7 = "SHP WT:", position 8 = space, positions 9-13 = up to five numeric, position 14 = space, positions 15-17 = "LBS" or "KG". Font Size = 8 pt (Trade Direct).

## Edge Cases & Notes
Weight is rounded up to the next whole pound or kilogram. For World Ease Package Pallet labels, the format also appears as right-justified with up to four numeric characters. The minimum weight for MaxiCode must be 1 LB or 1 KG.

## Claude Confidence
HIGH — spec provides explicit format with multiple examples

## Review Status
- [ ] Reviewed by human