# Field: ship_to_indicator

## Display Name
Ship To Indicator ("TO:" or "SHIP TO:")

## Field Description
A text indicator that marks the beginning of the Ship To (consignee/recipient) address block on the label.

## Format & Validation Rules
- **Data Type:** string
- **Length:** 3-8 characters
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** "TO:" or "SHIP TO:"
- **Required:** yes

## Examples from Spec
`TO:`, `SHIP TO:`

## Position on Label
Left side of the Ship To address block, oriented vertically or horizontally depending on label layout.

## Edge Cases & Notes
Label diagrams show both "TO:" and "SHIP" appearing as indicators.

## Claude Confidence
HIGH — clearly visible on all label diagrams

## Review Status
- [ ] Reviewed by human