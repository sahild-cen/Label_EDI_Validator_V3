# Field: destination_country_name

## Display Name
Destination Country Name

## Field Description
The full name of the destination country, typically printed on the label as part of the consignee address block for international shipments.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Country names per ISO 3166 / UPS Appendix E listing
- **Required:** yes — for international shipments

## Examples from Spec
Afghanistan, United States, United Kingdom, China Mainland, Japan, Singapore, Hong Kong SAR China, Australia, etc.

## Position on Label
Last line of the consignee address block (standard practice for international labels).

## Edge Cases & Notes
- Some countries have specific short names vs. official names (e.g., "China Mainland" vs. "People's Republic of China").
- Parent country names may be used for satellite territories.

## Claude Confidence
MEDIUM — Country names are listed in Appendix E; specific label positioning not detailed in this extract.

## Review Status
- [ ] Reviewed by human