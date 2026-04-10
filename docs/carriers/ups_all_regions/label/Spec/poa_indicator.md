# Field: poa_indicator

## Display Name
Power of Attorney (POA) Routing Instruction

## Field Description
A routing instruction indicator that must be present on the label when the shipper has authorized UPS to complete AES filing on their behalf.

## Format & Validation Rules
- **Data Type:** string
- **Length:** 3 characters
- **Pattern/Regex:** `POA`
- **Allowed Values:** "POA"
- **Required:** conditional — required when shipper authorizes UPS to complete AES filing

## Examples from Spec
- `SDL/POA`
- `SDL/EEI/POA`
- `POA / CO`
- `POA`

## Position on Label
Immediately below the larger documentation indicator, in the additional routing instructions area.

## Edge Cases & Notes
Font size is 10 pt. Located immediately below the larger documentation indicator. When combined with EEI and/or CO indicators, separated by forward slash (/). On World Ease labels, shown as "POA / CO".

## Claude Confidence
HIGH — Clearly defined with specific placement rules and multiple examples.

## Review Status
- [ ] Reviewed by human