# Field: service_title

## Display Name
Service Title

## Field Description
Identifies the UPS service level for the shipment. For World Ease shipments, this displays "UPS World Ease". For Trade Direct, different service levels apply.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** "UPS World Ease", "UPS EXPEDITED", "UPS GROUND", "UPS World Ease" (with service level codes like EXP, STD for Trade Direct)
- **Required:** yes

## Examples from Spec
- "UPS World Ease"
- "UPS EXPEDITED"
- "UPS GROUND"

## Position on Label
Printed prominently on the label. For World Ease Summary Label, Font Size 16 pt. Bold.

## Edge Cases & Notes
For World Ease single labels, the service prints to the right of the Tracking # separated by a vertical line.

## Claude Confidence
HIGH — spec clearly names this field with examples across multiple label types

## Review Status
- [ ] Reviewed by human