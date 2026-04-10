# Field: destination_country_code

## Display Name
Destination Country Code

## Field Description
The ISO 3166 country code for the destination/consignee country. Used in addressing, MaxiCode encoding, and routing. Both alpha (2-letter) and numeric (3-digit) codes are defined.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 2 characters (alpha code) or 3 digits (numeric code)
- **Pattern/Regex:** Alpha: `[A-Z]{2}`; Numeric: `[0-9]{3}`
- **Allowed Values:** ISO 3166 country codes as enumerated in Appendix E (e.g., GB=826, DE=276, FR=250, US=840, etc.). Special cases: Kosovo uses numeric 901 and alpha KV.
- **Required:** yes

## Examples from Spec
- United Kingdom: GB (826)
- United States: US (840)
- Germany: DE (implied from standard)
- France: FR (implied from standard)
- Kosovo: KV (901) — special non-standard code
- Switzerland: CH (756)
- Poland: PL (616)

## Position on Label
Used in address blocks and encoded in MaxiCode. The numeric country code is typically used in MaxiCode data string; the alpha code appears in human-readable address.

## ZPL Rendering
- **Typical Position:** Within consignee address block and encoded in MaxiCode
- **Font / Size:** Not specified
- **Field Prefix:** None — part of address formatting
- **ZPL Command:** ^FD (text field) in address block; ^BD (MaxiCode) for barcode encoding

## Edge Cases & Notes
- Kosovo uses non-standard codes: numeric 901, alpha KV (not in ISO 3166 standard).
- Parent country codes may be used when shipping to satellite countries (e.g., United Kingdom country code used when shipping to the Isle of Man).
- The country code is a key element in determining MaxiCode mode (Mode 2 for US, Mode 3 for non-US).

## Claude Confidence
HIGH — Appendix E provides comprehensive country code listings with clear format definitions and special case notes.

## Review Status
- [ ] Reviewed by human