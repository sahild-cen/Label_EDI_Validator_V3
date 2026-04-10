# Field: shipper_instructions

## Display Name
Shipper's Instructions

## Field Description
Instructions on the summary label directing which package the label should be applied to.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** `Please Apply This Label to Package # [0-9]+`
- **Allowed Values:** Not restricted (package number is variable)
- **Required:** yes — on summary labels

## Examples from Spec
- "PLEASE APPLY THIS LABEL TO PACKAGE # 6"

## Position on Label
Top of the summary label. Font Size = 12 pt. Bold.

## Edge Cases & Notes
The blank/number indicates the value of the last package or total number of packages in the consolidated shipment.

## Claude Confidence
HIGH — spec explicitly describes this field with format and purpose

## Review Status
- [ ] Reviewed by human