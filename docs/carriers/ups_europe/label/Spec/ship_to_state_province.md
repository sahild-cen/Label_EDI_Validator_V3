# Field: ship_to_state_province

## Display Name
Ship To State/Province

## Field Description
The state or province code of the destination/consignee address. Encoded as the last data field before the record separator in the MaxiCode secondary message.

## Format & Validation Rules
- **Data Type:** alphabetic
- **Length:** 2 characters
- **Pattern/Regex:** `^[A-Z]{2}$`
- **Allowed Values:** Valid 2-character state/province codes
- **Required:** conditional — required for US and countries with state/province codes; some non-US destinations will not have a state or province (leave as placeholder)

## Examples from Spec
- `GA` (Georgia, validated address example)
- `UT` (Utah, non-validated and letter/envelope examples)
- Empty/placeholder (international Germany example — no state)

## Position on Label
Encoded within MaxiCode secondary message. Also printed as human-readable text in the ship-to address block.

## ZPL Rendering
- **Typical Position:** Ship-to address block, center/middle of label
- **Font / Size:** Not specified
- **Field Prefix:** None (part of address block)
- **ZPL Command:** ^FD (text field) for human-readable; encoded within ^BD (MaxiCode)

## Edge Cases & Notes
- Some non-US destinations will not have a state or province. In that case, the field is left empty but the record separator `<RS>` must still follow.
- In the international Germany example, the state field is empty with just the `<RS>` following.

## Claude Confidence
HIGH — spec clearly defines the field with conditional requirement for non-US destinations

## Review Status
- [ ] Reviewed by human