# Field: origin_country

## Display Name
Origin Country

## Field Description
Indicates whether the origin of the shipment is from the destination country itself (domestic) or from another country (international). The Postal Code Line Format Matrix marks this with a bullet (•) for applicable origin countries.

## Format & Validation Rules
- **Data Type:** string (alpha)
- **Length:** 2 characters (ISO 3166 alpha code)
- **Pattern/Regex:** `^[A-Z]{2}$`
- **Allowed Values:** ISO 3166 alpha-2 country codes; this guide is specifically for customers located in Asia
- **Required:** yes

## Examples from Spec
No standalone examples; referenced in Postal Code Line Format Matrix as "Origin Country" column.

## Position on Label
Used in the ship-from/return address block.

## Edge Cases & Notes
- This guide is specifically for "Customers Located in Asia," so origin countries are expected to be Asian countries.
- Domestic movements are within a single postal authority; international movements cross postal authorities.

## Claude Confidence
MEDIUM — Referenced in matrix and definitions but not detailed as a standalone label field in this extract.

## Review Status
- [ ] Reviewed by human