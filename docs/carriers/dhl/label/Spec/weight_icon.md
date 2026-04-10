# Field: weight_icon

## Display Name
Weight Icon

## Field Description
A visual icon/indicator printed on the label when the piece weight meets or exceeds specified thresholds, alerting handlers to heavier packages.

## Format & Validation Rules
- **Data Type:** graphic/icon
- **Length:** N/A
- **Pattern/Regex:** N/A
- **Allowed Values:** 
  - No icon: piece weight < 10 kg (22 lb)
  - Icon printed: piece weight ≥ 10 kg (22 lb) and < 20 kg (44 lb)
  - Icon printed: piece weight ≥ 20 kg (44 lb)
- **Required:** conditional — printed only when piece weight is ≥ 10 kg (22 lb)

## Examples from Spec
No specific icon images in extracted text, but weight ranges are provided:
- 0.100 to 9.999 kg: No Icon printed
- 10.000 to 19.999 kg: Icon printed
- 20.000 kg and above: Icon printed

## Position on Label
Not specified in extracted text, but appears on the transport label as a visual handling indicator.

## Edge Cases & Notes
- Two tiers of weight icons may exist (the spec lists three weight ranges with two apparently having icons), suggesting potentially different icons for the two heavier ranges.
- The threshold differs depending on the unit system: 10 kg / 22 lb for the first tier, 20 kg / 44 lb for the second.

## Claude Confidence
MEDIUM — Spec defines clear thresholds but the exact icon designs and visual differentiation between tiers are not detailed in the extracted text.

## Review Status
- [ ] Reviewed by human