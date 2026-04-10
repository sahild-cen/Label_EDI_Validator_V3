# Field: weight_unit

## Display Name
Weight Unit of Measure

## Field Description
The unit of measurement for the shipment weight (kilograms or pounds).

## Format & Validation Rules
- **Data Type:** string
- **Length:** 1-3 characters
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** "K" or "KG" for kilograms, "L" or "LB" for pounds
- **Required:** yes

## Examples from Spec
No examples in spec.

## Position on Label
Adjacent to the weight value.

## Edge Cases & Notes
DHL Express uses kilograms as the standard unit for international shipments.

## Claude Confidence
HIGH — Always accompanies weight on DHL labels.

## Review Status
- [ ] Reviewed by human