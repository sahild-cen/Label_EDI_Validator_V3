# Field: itn_number

## Display Name
Internal Transaction Number (ITN)

## Field Description
The AES (Automated Export System) Internal Transaction Number assigned when the shipper has completed AES filing, which must print on the label. The ITN takes precedence over reference numbers.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** Up to 20 characters total; "AES " prefix (4 chars) + up to 16 alphanumeric
- **Pattern/Regex:** `AES [A-Z0-9]{1,16}` (positions 1-3 = "AES", position 4 = space, positions 5-20 = up to 16 alphanumeric)
- **Allowed Values:** Valid AES Internal Transaction Numbers
- **Required:** conditional — required when shipper has completed AES filing and has the ITN

## Examples from Spec
- `AES X23456789012345`
- `AES X20034567890`

## Position on Label
In the routing section of the label. Must always take precedence over reference numbers on the address label.

## Edge Cases & Notes
Font size is 10 pt. The ITN number must always take precedence over the printing of reference numbers on the address label.

## Claude Confidence
HIGH — Clearly defined with data content positions, format rules, and examples.

## Review Status
- [ ] Reviewed by human