# Field: ups_scac

## Display Name
UPS SCAC (Standard Carrier Alpha Code)

## Field Description
The Standard Carrier Alpha Code for UPS, which is always "UPSN". This is a required field in the MaxiCode secondary message identifying UPS as the carrier.

## Format & Validation Rules
- **Data Type:** alphabetic
- **Length:** 4 characters
- **Pattern/Regex:** `^UPSN$`
- **Allowed Values:** "UPSN" (fixed value)
- **Required:** yes

## Examples from Spec
- `UPSN` (all MaxiCode examples)

## Position on Label
Encoded within MaxiCode secondary message only.

## ZPL Rendering
- **Typical Position:** Encoded within MaxiCode
- **Font / Size:** Not applicable
- **Field Prefix:** None
- **ZPL Command:** Encoded within ^BD (MaxiCode)

## Edge Cases & Notes
- This is always the fixed value "UPSN" for UPS shipments.

## Claude Confidence
HIGH — spec clearly states the fixed value "UPSN" with consistent usage across all examples

## Review Status
- [ ] Reviewed by human