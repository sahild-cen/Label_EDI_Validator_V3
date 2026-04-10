# Field: maxicode_ship_to_state

## Display Name
Ship To State/Province (MaxiCode)

## Field Description
The 2-character state or province code for the destination, encoded in the MaxiCode data string.

## Format & Validation Rules
- **Data Type:** alphabetic
- **Length:** 2 (exact)
- **Pattern/Regex:** `[A-Z]{2}`
- **Allowed Values:** Valid state/province codes
- **Required:** yes (but may be blank for some non-U.S. destinations)

## Examples from Spec
- `GA` (Georgia)
- `UT` (Utah)
- Blank (international example for Cologne, Germany — `<RS>` used as placeholder)

## Position on Label
Encoded within the MaxiCode barcode (secondary message, last field before end-of-format).

## Edge Cases & Notes
- Some non-U.S. destinations will not have a state or province. In such cases, the field is left blank but the `<RS>` record separator is still provided.

## Claude Confidence
HIGH — spec clearly defines as 2-character alphabetic with note about international exceptions.

## Review Status
- [ ] Reviewed by human