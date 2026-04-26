# Field: destination_country_code

## Display Name
Destination ISO Country Code

## Field Description
The ISO 3166-1 country code for the destination country. In the ASC MH10 routing barcode, this is a 2-character uppercase alpha code. In the GS1 routing barcode, it is a 3-digit numeric code. This field is also displayed on the label in the routing information area.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 2 alpha characters (ASC MH10) or 3 numeric digits (GS1)
- **Pattern/Regex:** ASC MH10: `[A-Z]{2}` ; GS1: `\d{3}`
- **Allowed Values:** Valid ISO 3166-1 country codes
- **Required:** yes — mandatory in both routing barcode and label

## Examples from Spec
- `BE` (Belgium), `DE` (Germany), `CH` (Switzerland), `NL` (Netherlands)
- GS1: `756` (Switzerland)

## ZPL Rendering
- **Typical Position:** Part of routing barcode and routing code human-readable area
- **Font / Size:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field) — also encoded within routing barcode

## Edge Cases & Notes
- For domestic shipments, the destination country code is still required in the routing barcode.
- ISO 3166-1 is the referenced standard.

## Claude Confidence
HIGH — explicitly defined as mandatory in the routing barcode structure

## Review Status
- [x] Reviewed by human