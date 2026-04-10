# Field: label_spec_version

## Display Name
Label Specification Version

## Field Description
The version identifier of the UPS label specification used to generate the label.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable (approximately 13 characters)
- **Pattern/Regex:** `\d+\.\d+[A-Z]\s\d{2}/\d{4}`
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- `18.5A 01/2020`

## Position on Label
In the lower portion of the label.

## Edge Cases & Notes
Appears on every label example with the same value "18.5A 01/2020". Format appears to be version number followed by month/year.

## Claude Confidence
HIGH — Shown on every single label example with consistent format.

## Review Status
- [ ] Reviewed by human