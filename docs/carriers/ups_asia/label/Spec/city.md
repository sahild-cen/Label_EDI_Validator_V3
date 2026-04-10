# Field: city

## Display Name
City

## Field Description
The city name within the consignee address, positioned according to the destination country's address format (before or after postal code).

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
No examples in spec.

## Position on Label
Within the consignee address block, on the postal code line per the Address Format Type (Format 1: after postal code; Format 2: before postal code).

## Edge Cases & Notes
- Positioning relative to postal code is country-dependent.

## Claude Confidence
MEDIUM — Implicitly defined through address format matrix but no standalone specification in this extract.

## Review Status
- [ ] Reviewed by human