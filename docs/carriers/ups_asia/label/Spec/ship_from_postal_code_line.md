# Field: ship_from_postal_code_line

## Display Name
Ship From Postal Code Line

## Field Description
The postal/ZIP code and city line for the shipper address. For some countries this includes city, state, and postal code combined on one line.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
"POSTAL CODE LINE", "SINGAPORE 486064", "CHICAGO IL 60607", "KALAMAZOO MI 49009", "12099 BERLIN"

## Position on Label
Upper left portion of the label, in the ship-from address block below street address.

## Edge Cases & Notes
Format varies by country — US format includes city, state abbreviation, and ZIP; Singapore includes country name and postal code; German format uses postal code before city name.

## Claude Confidence
HIGH — field appears consistently across all label examples with varying country formats

## Review Status
- [ ] Reviewed by human