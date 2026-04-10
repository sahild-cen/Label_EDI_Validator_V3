# Field: ship_to_country

## Display Name
Ship To Country

## Field Description
The full country name of the destination/consignee address.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted — full country name
- **Required:** yes — for international shipments

## Examples from Spec
"COUNTRY", "SINGAPORE", "GERMANY", "UNITED STATES", "JAPAN", "INDIA", "CHINA PEOPLES REPUBLIC OF"

## Position on Label
Middle left portion of the label, last line of the ship-to address block.

## Edge Cases & Notes
Uses full country name, not ISO codes. "CHINA PEOPLES REPUBLIC OF" is used for China, which is a non-standard ordering.

## Claude Confidence
HIGH — field appears consistently across all international label examples

## Review Status
- [ ] Reviewed by human