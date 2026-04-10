# Field: iso_country_code

## Display Name
ISO Country Code (Destination)

## Field Description
The ISO 3166-1 country code for the destination/consignee country, encoded within the routing barcode. Uses 2 upper-case alpha characters for ASC MH10 format or 3 numeric digits for GS1 format.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 2 characters (ASC MH10) or 3 digits (GS1)
- **Pattern/Regex:** ASC MH10: `[A-Z]{2}`; GS1: `\d{3}`
- **Allowed Values:** Per ISO 3166-1 country codes
- **Required:** yes (mandatory in routing barcode)

## Examples from Spec
- `BE` (Belgium), `DE` (Germany), `CH` (Switzerland), `NL` (Netherlands) — ASC MH10 format
- `756` (Switzerland) — GS1 format

## Position on Label
Within the routing barcode structure, immediately after the Data Identifier.

## Edge Cases & Notes
- The same shipment destination is represented differently depending on the barcode standard used (alpha vs. numeric).
- Also appears in the human-readable routing code text.

## Claude Confidence
HIGH — Spec clearly defines both formats with examples and references ISO 3166-1.

## Review Status
- [ ] Reviewed by human