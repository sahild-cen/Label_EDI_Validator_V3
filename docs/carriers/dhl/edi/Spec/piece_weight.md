# Field: piece_weight

## Display Name
Piece Weight / Measurements

## Field Description
A segment (SG52 - MEA) to specify measurements applicable to a goods item, such as weight at piece level.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Weight units: KGM (Kilograms, default), LBR (Pounds)
- **Required:** yes (Required at SG52, up to 9 occurrences at piece level)

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
Default weight unit is KGM (Kilograms), also acceptable is LBR (Pounds). MEA also appears at SG67 for dangerous goods measurements and at SG70 for shipment loading meters.

## Claude Confidence
HIGH — Units of measure clearly defined in spec.

## Review Status
- [ ] Reviewed by human