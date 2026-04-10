# Field: ship_to_postal_code_city_country

## Display Name
Ship To Postal Code / City / Country

## Field Description
The destination postal code, city, and country information for the consignee, which may also appear in a routing code format.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- `DEU 091 0-00` (routing code format for Germany)

## Position on Label
In the Ship To address block and/or in the routing code area of the label.

## Edge Cases & Notes
The postal/routing code may appear in a specialized format (e.g., "DEU 091 0-00") which includes country code and postal/routing information.

## Claude Confidence
MEDIUM — The routing format is shown but detailed format rules are not fully specified in extracted text.

## Review Status
- [ ] Reviewed by human