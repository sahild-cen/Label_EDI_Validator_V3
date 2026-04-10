# Field: consignee_address

## Display Name
Consignee (Ship-To) Address

## Field Description
The destination address block for the package recipient. Includes street address, city, state/province/county, postal code, and country. The address is also encoded (compressed) within the MaxiCode data string.

## Format & Validation Rules
- **Data Type:** alphanumeric (multi-line text block)
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Must conform to destination country address format (Format 1 or Format 2 per Appendix F)
- **Required:** yes

## Examples from Spec
No complete address examples in this extract. MaxiCode examples reference consignee address compression.

## Position on Label
Not specified in this extract, but standard UPS label placement is in the center/lower portion of the label.

## Edge Cases & Notes
- The "Compressed MaxiCode™ Data String" involves reducing the number of bits for characters in the consignee address.
- Address validation for U.S. addresses uses the USPS CASS database.
- Postal code line formatting varies by country (see address_format_type field).

## Claude Confidence
MEDIUM — Referenced multiple times in definitions and MaxiCode sections, but full field spec not in this extract.

## Review Status
- [ ] Reviewed by human