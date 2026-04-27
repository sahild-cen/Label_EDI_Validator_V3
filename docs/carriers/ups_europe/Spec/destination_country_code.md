# Field: destination_country_code

## Display Name
Destination Country Code (ISO 3166)

## Field Description
The ISO 3166 country code for the destination/consignee country. Available in both numeric (3-digit) and alpha (2-letter) formats.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 2 (alpha) or 3 (numeric)
- **Pattern/Regex:** ISO 3166 alpha-2: `[A-Z]{2}` ; ISO 3166 numeric: `[0-9]{3}`
- **Allowed Values:** Full ISO 3166 list as provided in Appendix E (e.g., GB=826, US=840, DE=276, FR=250, etc.)
- **Required:** yes

## Examples from Spec
- Nicaragua: NI / 558
- Nigeria: NG / 566
- Norway: NO / 578
- United Kingdom: GB / 826
- United States: US / 840
- Germany (implied by Europe context)
- Kosovo: KV / 901 (special case)

## Position on Label
Part of the consignee address block and encoded in MaxiCode data string.

## Edge Cases & Notes
- Kosovo uses non-standard codes: numeric 901, alpha KV (not part of official ISO 3166 but used by UPS).
- Parent country codes may be used when shipping to satellite countries (e.g., United Kingdom country code used when shipping to the Isle of Man).
- Sint Maarten and Saint Martin share code SX / 534.

## Claude Confidence
HIGH — Appendix E provides the complete ISO 3166 country code table with explicit examples and special notes.

## Review Status
- [x] Reviewed by human