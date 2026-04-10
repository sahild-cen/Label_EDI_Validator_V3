# Field: ship_from_extended_address

## Display Name
Ship From Extended Address

## Field Description
Additional address information for the shipper, such as suite number, floor, building name, or secondary address line.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** no — conditional, only when additional address detail exists

## Examples from Spec
- `EXTENDED ADDRESS` (placeholder used throughout spec)

## Position on Label
Top section of the label in the ship-from address block, below the company name and before the street address.

## Edge Cases & Notes
Not all labels include this field. It is omitted on several label examples where only street address is needed.

## Claude Confidence
HIGH — Clearly shown as optional in label examples.

## Review Status
- [ ] Reviewed by human