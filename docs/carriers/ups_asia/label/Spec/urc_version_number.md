# Field: urc_version_number

## Display Name
URC Version Number

## Field Description
Version number associated with the UPS Routing Code table used to derive the routing information.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** `^\d+\.\d+[A-Z]\s\d{2}/\d{4}$`
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- `18.5A 01/2020`

## Position on Label
Bottom of the Carrier Segment, typically in the lower-right area of the label.

## Edge Cases & Notes
- Font Size = 6 pt. (very small, informational)
- Appears consistently across all label samples in the spec
- Format appears to be: version number, letter, space, month/year

## Claude Confidence
HIGH — consistently shown across all label samples with same format

## Review Status
- [ ] Reviewed by human