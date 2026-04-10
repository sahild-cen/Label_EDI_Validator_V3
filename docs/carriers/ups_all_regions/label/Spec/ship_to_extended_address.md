# Field: ship_to_extended_address

## Display Name
Ship To Extended Address

## Field Description
Additional address information for the delivery destination, such as suite number, floor, building name, or secondary address line.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** no — conditional, only when additional address detail exists

## Examples from Spec
- `EXTENDED ADDRESS` (placeholder used throughout spec)
- `KENNEDYSTABE` (street name in Germany example)

## Position on Label
Middle section of the label in the ship-to address block, below the company name.

## Edge Cases & Notes
Not all labels include this field. Some labels show two extended address lines (e.g., "EXTENDED ADDRESS" appearing twice).

## Claude Confidence
HIGH — Clearly shown as optional in label examples.

## Review Status
- [ ] Reviewed by human