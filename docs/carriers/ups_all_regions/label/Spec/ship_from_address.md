# Field: ship_from_address

## Display Name
Ship From Address

## Field Description
The shipper/origin address block containing the shipper's contact name, phone number, company name, extended address, street address, city, state/province, postal code, and country.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable per line
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- "CONTACT NAME / PHONE NUMBER / WORLDEASE US SHIPPER / 1 UPS WAY / LOS ANGELES CA 90001 / UNITED STATES"

## Position on Label
Upper portion of the label, above the SHIP TO block. Format must follow specifications in the UPS Guide to Labeling.

## Edge Cases & Notes
For Trade Direct labels, the Ship From and Ship To address formats must follow the specifications outlined in the current UPS Guide to Labeling.

## Claude Confidence
HIGH — spec shows clear examples in label diagrams

## Review Status
- [ ] Reviewed by human