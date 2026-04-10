# Field: destination_country_numeric_code

## Display Name
Destination Country Numeric Code

## Field Description
The ISO 3166 numeric country code for the destination country, used in MaxiCode encoding and data transmission.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 3 characters (zero-padded)
- **Pattern/Regex:** `^\d{3}$`
- **Allowed Values:** ISO 3166 numeric codes as listed in Appendix E (e.g., 840 for US, 826 for GB, 156 for CN, 392 for JP). Kosovo uses 901.
- **Required:** yes — for MaxiCode encoding

## Examples from Spec
004 (Afghanistan), 840 (United States), 826 (United Kingdom), 156 (China Mainland), 392 (Japan), 702 (Singapore), 344 (Hong Kong), 901 (Kosovo)

## Position on Label
Encoded within MaxiCode data string; not typically displayed as human-readable text.

## Edge Cases & Notes
- Kosovo uses non-standard numeric code 901.
- Codes are zero-padded to 3 digits (e.g., Afghanistan is 004, not 4).

## Claude Confidence
HIGH — Full list provided in Appendix E with clear format.

## Review Status
- [ ] Reviewed by human