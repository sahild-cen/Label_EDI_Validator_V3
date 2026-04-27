# Field: maxicode_ship_to_state

## Display Name
Ship To State/Province (MaxiCode)

## Field Description
The destination state or province code encoded in the MaxiCode data string. Required but may be empty for non-US destinations that do not have a state or province.

## Format & Validation Rules
- **Data Type:** alphabetic
- **Length:** 2 (exactly)
- **Pattern/Regex:** `[A-Z]{2}`
- **Allowed Values:** Valid state/province abbreviations
- **Required:** yes — however, some non-US destinations will not have a state or province (leave as placeholder)

## Examples from Spec
- `GA` (Georgia)
- `UT` (Utah)
- Empty/blank (international example for Germany — Cologne)

## Position on Label
Encoded within MaxiCode barcode (secondary message).

## Edge Cases & Notes
- Some non-US destinations will not have a state or province; in such cases the field may be empty but the record separator (<RS>) must still follow.
- This is the last data field before the end of format record separator.

## Claude Confidence
HIGH — spec defines format and notes exception for non-US destinations

## Review Status
- [x] Reviewed by human