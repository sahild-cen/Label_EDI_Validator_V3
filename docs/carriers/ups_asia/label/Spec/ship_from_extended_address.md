# Field: ship_from_extended_address

## Display Name
Ship From Extended Address

## Field Description
An additional address line for the shipper (e.g., suite, floor, building name), displayed in the ship-from address block.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** no — optional additional address line

## Examples from Spec
"EXTENDED ADDRESS"

## Position on Label
Upper left portion of the label, in the ship-from address block below company name.

## Edge Cases & Notes
Not all label examples include this field; it is optional. Some labels skip directly from company name to street address.

## Claude Confidence
HIGH — field appears in many but not all label examples, clearly optional

## Review Status
- [ ] Reviewed by human