# Field: address_format_type

## Display Name
Address Format Type

## Field Description
Indicates the ordering of postal code, city, and state/province on the address line, determined by the destination country. Format 1 places postal code before city; Format 2 places city before postal code.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 1
- **Pattern/Regex:** `[12]`
- **Allowed Values:** 1 = "Postal Code, City, State/Province/County"; 2 = "City, State/Province/County, Postal Code"
- **Required:** yes — determined by destination country

## Examples from Spec
- Croatia: Format 1
- Indonesia: Format 2
- Nigeria: Format 2
- Turkey: Format 1
- Norfolk Island: Format 2
- Kosovo: Format 1

## Position on Label
Determines layout of the postal code line within the consignee address block.

## Edge Cases & Notes
- Some countries have no defined format (indicated by "-").
- Most countries use Format 1; Format 2 is less common.

## Claude Confidence
HIGH — Appendix F provides a clear matrix of address formats per country.

## Review Status
- [x] Reviewed by human