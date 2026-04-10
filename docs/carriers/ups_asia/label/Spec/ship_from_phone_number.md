# Field: ship_from_phone_number

## Display Name
Ship From Phone Number

## Field Description
The phone number at the origin/shipper location.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — Required except when origin and destination country are the same; optional when shipping to/from the European Union (EU)

## Examples from Spec
- `PHONE NUMBER`

## Position on Label
Second line of the Ship From address block, top-left of label.

## Edge Cases & Notes
- Font Size = 8 pt.
- Phone number is optional when shipping to/from the EU

## Claude Confidence
HIGH — clearly shown in label samples with conditional requirements noted

## Review Status
- [ ] Reviewed by human