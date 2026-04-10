# Field: piece_dimensions

## Display Name
Piece Dimensions (Length, Width, Height)

## Field Description
A segment (SG53 - DIM) to specify dimensions (length, width, height) applicable to a goods item at piece level.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Dimension units: CMT (Centimeters, default), MTR (Meters), INH (Inches)
- **Required:** yes (Required at SG53, 1 occurrence)

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
Default dimension unit is CMT (Centimeters). Also acceptable: MTR (Meters) and INH (Inches). Volume can be expressed in MTQ (Cubic Meters, default), CMQ (Cubic Centimeters), or INQ (Cubic Inches).

## Claude Confidence
HIGH — Units of measure clearly defined in spec.

## Review Status
- [ ] Reviewed by human