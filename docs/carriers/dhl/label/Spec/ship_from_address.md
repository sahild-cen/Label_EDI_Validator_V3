# Field: ship_from_address

## Display Name
Ship From Address (Consignor's Address)

## Field Description
The sender/consignor's address that serves the purpose of supporting identification by the carrier (e.g., for Pickup) as well as the Consignee. It does not necessarily reflect the return address in case of failed delivery.

## Format & Validation Rules
- **Data Type:** string (multi-line)
- **Length:** Maximum 47 characters per line; maximum 7 lines total (5 lines for Highly-Compact labels)
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted — address elements based on DHL Corporate Data Model
- **Required:** conditional — the section is present on standard labels; a deviating address may be printed if approved by DHL

## Examples from Spec
Highly-Compact structure example:
1. Address line 1: Receiver Company / Name
2. Address line 2: Building Name or equivalent
3. Address line 3: Street Name, Street Number
4. Address line 4: City Name, Postcode or equivalent
5. Country Code / Country Name

## Position on Label
Left side of the label, with the word "From" printed in the upper left corner of this section.

## Edge Cases & Notes
- The word "From" must appear; may be written in local language, but for international shipments English "From" must appear (optionally both languages separated by "/")
- For international shipments, Country Name shall be on its own line
- For domestic pieces, Country Name may be in local language; for cross-border, Country Name must be in English (may be followed by local translation)
- Country Name is optional for domestic shipments but mandatory for cross-border if ISO 3166 code is missing
- Country Code follows ISO 3166 two-character standard
- If approved by DHL, a deviating address may be printed here
- Highly-Compact labels reduce to 5 lines upon formal DHL Express approval

## Claude Confidence
HIGH — spec provides detailed structure, line limits, and language requirements

## Review Status
- [ ] Reviewed by human