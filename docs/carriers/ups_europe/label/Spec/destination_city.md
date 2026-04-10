# Field: destination_city

## Display Name
Destination City

## Field Description
The city name in the consignee/destination address. Its position relative to the postal code depends on the address format for the destination country (Format 1 or Format 2).

## Format & Validation Rules
- **Data Type:** string
- **Length:** Variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted — valid city name for the destination country
- **Required:** yes

## Examples from Spec
No explicit city examples in the extracted text, but the address format matrix implies city is part of the postal code line.

## Position on Label
Within the consignee address block. Position relative to postal code:
- Address Format 1: Postal Code, City, State/Province/County
- Address Format 2: City, State/Province/County, Postal Code

## ZPL Rendering
- **Typical Position:** Consignee address block
- **Font / Size:** Not specified
- **Field Prefix:** None — part of address line
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
- Address format (1 vs 2) determines whether the city appears before or after the postal code on the postal code line.

## Claude Confidence
MEDIUM — Implicitly defined through address format matrix but not independently specified with format details.

## Review Status
- [ ] Reviewed by human