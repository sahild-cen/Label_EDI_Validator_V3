# Field: shipment_dimensional_weight

## Display Name
Shipment Dimensional Weight (SHP DWT)

## Field Description
The dimensional (volumetric) weight of the shipment, used for billing purposes when it exceeds actual weight.

## Format & Validation Rules
- **Data Type:** numeric with unit
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Numeric value followed by LBS or KG
- **Required:** conditional — shown when dimensional weight is applicable

## Examples from Spec
- `SHP DWT: 25 LBS`
- `SHP DWT: 38 LBS`
- `SHP DWT: 49 LBS`

## Position on Label
In the upper right area of the label, near the shipment weight field.

## Edge Cases & Notes
May not appear on all label types. Shown with "SHP DWT:" prefix.

## Claude Confidence
HIGH — Shown on multiple label examples.

## Review Status
- [ ] Reviewed by human