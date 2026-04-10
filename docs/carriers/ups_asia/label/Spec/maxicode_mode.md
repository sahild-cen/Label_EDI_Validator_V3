# Field: maxicode_mode

## Display Name
MaxiCode Mode

## Field Description
The MaxiCode encoding mode used for the shipment, determined by the destination country. Mode 2 is used for U.S. destinations; Mode 3 is used for all non-U.S. destinations.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 1 character
- **Pattern/Regex:** `^[23]$`
- **Allowed Values:** 2 (U.S. destinations), 3 (non-U.S. destinations)
- **Required:** yes

## Examples from Spec
- Mode 2: U.S. destinations with numeric postal codes
- Mode 3: Non-U.S. destinations with alphanumeric postal codes

## Position on Label
Encoded within the MaxiCode symbol parameters; not displayed as human-readable text.

## Edge Cases & Notes
- Some label software providers and printer manufacturers interpret Mode 2 exclusively for U.S. destinations and Mode 3 exclusively for non-U.S. destinations.
- The compressed MaxiCode data string formats for both modes are not covered in this guide.

## Claude Confidence
HIGH — Clearly defined with explicit mode assignments by destination.

## Review Status
- [ ] Reviewed by human