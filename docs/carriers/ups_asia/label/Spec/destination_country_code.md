# Field: destination_country_code

## Display Name
Destination Country Code

## Field Description
The ISO 3166 alpha country code for the destination/consignee country. Used on the label and within the MaxiCode data string for international shipments.

## Format & Validation Rules
- **Data Type:** string (alpha)
- **Length:** 2 characters
- **Pattern/Regex:** `^[A-Z]{2}$`
- **Allowed Values:** ISO 3166 alpha-2 codes as listed in Appendix E (e.g., AF, AL, DZ, US, GB, CN, JP, KR, SG, HK, AU, etc.). Special case: Kosovo uses "KV" (non-standard).
- **Required:** yes — for all shipments

## Examples from Spec
AF (Afghanistan), US (United States), GB (United Kingdom), CN (China Mainland), JP (Japan), KR (Korea, Republic of), SG (Singapore), HK (Hong Kong SAR, China), AU (Australia), IN (India), TW (Taiwan, China), KV (Kosovo — special code)

## Position on Label
Used within address blocks and MaxiCode data; also part of the Postal Code Line Format determination.

## Edge Cases & Notes
- Kosovo uses non-standard code "KV" (numeric 901) instead of an ISO-assigned code.
- Parent country codes may be used when shipping to satellite countries (e.g., United Kingdom "GB" used when shipping to the Isle of Man).
- The country code is critical for MaxiCode mode selection: non-US destinations use Mode 3.

## Claude Confidence
HIGH — Comprehensive list provided in Appendix E with clear format and special cases noted.

## Review Status
- [ ] Reviewed by human