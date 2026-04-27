# Field: maxicode_country_code

## Display Name
MaxiCode Country Code Field

## Field Description
The country code encoded within the MaxiCode data string, used to determine whether Mode 2 (U.S.) or Mode 3 (non-U.S.) encoding applies.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 3 (ISO 3166 numeric)
- **Pattern/Regex:** `[0-9]{3}`
- **Allowed Values:** ISO 3166 numeric country codes per Appendix E
- **Required:** yes

## Examples from Spec
No direct MaxiCode country code examples, but implied from Mode 2 (U.S. = 840) and Mode 3 (all others).

## Position on Label
Encoded within the MaxiCode 2D barcode data string.

## Edge Cases & Notes
- Mode 2 is used exclusively for U.S. destinations (country code 840).
- Mode 3 is used for all non-U.S. destinations.
- Kosovo uses numeric code 901.

## Claude Confidence
MEDIUM — Implied from MaxiCode mode definitions and country code appendix but not explicitly shown as a separate field in this extract.

## Review Status
- [x] Reviewed by human