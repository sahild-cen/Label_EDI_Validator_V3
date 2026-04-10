# Field: ups_scac

## Display Name
UPS SCAC (Standard Carrier Alpha Code)

## Field Description
The Standard Carrier Alpha Code identifying UPS as the carrier, encoded in the MaxiCode data string.

## Format & Validation Rules
- **Data Type:** string
- **Length:** 4 (exact)
- **Pattern/Regex:** `UPSN`
- **Allowed Values:** `UPSN`
- **Required:** yes

## Examples from Spec
- `UPSN` (all MaxiCode examples)

## Position on Label
Encoded within the MaxiCode barcode (secondary message).

## Edge Cases & Notes
- Always the fixed value "UPSN".

## Claude Confidence
HIGH — spec explicitly states the value is "UPSN" and marks it as required.

## Review Status
- [ ] Reviewed by human