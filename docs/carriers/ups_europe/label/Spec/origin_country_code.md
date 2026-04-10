# Field: origin_country_code

## Display Name
Origin Country Code

## Field Description
The ISO 3166 country code for the origin/shipper country. The spec is specifically for "Customers Located in Europe," indicating European origin countries. Used in routing and potentially in address blocks.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 2 characters (alpha) or 3 digits (numeric)
- **Pattern/Regex:** Alpha: `[A-Z]{2}`; Numeric: `[0-9]{3}`
- **Allowed Values:** ISO 3166 country codes; countries marked with bullet (•) in the "Origin Country" column of Appendix F
- **Required:** yes

## Examples from Spec
Countries marked as origin countries in Appendix F include (among others): Croatia, Indonesia, Ivory Coast, Mozambique, Namibia, Nigeria, Norfolk Island, Solomon Islands, Togo, Turkey, Wallis and Futuna, Zimbabwe.

## Position on Label
Within the shipper/return address block.

## ZPL Rendering
- **Typical Position:** Shipper address area of label
- **Font / Size:** Not specified
- **Field Prefix:** None — part of address
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
- The spec is tailored to European origin customers, so typical origin countries would be European nations.
- Appendix F distinguishes between origin and destination countries with bullet markers.

## Claude Confidence
MEDIUM — Inferred from Appendix F matrix and spec title; specific rendering details not in extracted text.

## Review Status
- [ ] Reviewed by human