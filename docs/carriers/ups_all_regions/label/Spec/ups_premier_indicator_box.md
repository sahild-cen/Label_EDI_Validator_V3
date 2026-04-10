# Field: ups_premier_indicator_box

## Display Name
UPS Premier Indicator Box (V Icon)

## Field Description
A visual indicator consisting of a white "V" character printed inside a black square on the label, identifying the package as a UPS Premier shipment.

## Format & Validation Rules
- **Data Type:** string (visual indicator)
- **Length:** 1 character ("V")
- **Pattern/Regex:** `^V$`
- **Allowed Values:** "V"
- **Required:** conditional — required for UPS Premier shipments

## Examples from Spec
"V" shown on the UPS Premier Silver International Label example.

## Position on Label
Left justified on the label. The black square is 0.35 inches x 0.35 inches with a white "V" inside.

## Edge Cases & Notes
- Text Color = White on black square background.
- Font Size = 28 pt. bold.
- The box dimensions are 0.35 inches x 0.35 inches.
- Left justified positioning.

## Claude Confidence
HIGH — spec provides exact character, dimensions, color, and positioning requirements.

## Review Status
- [ ] Reviewed by human