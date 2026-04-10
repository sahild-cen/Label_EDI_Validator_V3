# Field: ship_to_postal_code_line

## Display Name
Ship To Postal Code Line

## Field Description
The postal/ZIP code and city line for the consignee/destination address. Format varies by country.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
"POSTAL CODE LINE", "SINGAPORE 486064", "60386 FRANKFURT", "MESA AZ 85206-4802", "TOKYO 1000004", "MUMBAI 400060", "710082 XIAN", "ROSWELL GA 30076", "CHICAGO IL 60607", "12099 BERLIN", "DULUTH GA 30097", "2080032 TOKYO"

## Position on Label
Middle left portion of the label, in the ship-to address block below street address.

## Edge Cases & Notes
Format varies significantly by destination country. US addresses use "CITY STATE ZIP" format. German addresses use "ZIP CITY". Japanese addresses use "ZIP CITY". Singapore uses "SINGAPORE ZIP".

## Claude Confidence
HIGH — field appears consistently with many country-specific examples

## Review Status
- [ ] Reviewed by human