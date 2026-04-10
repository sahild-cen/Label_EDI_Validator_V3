# Field: routing_barcode

## Display Name
Routing Barcode (ISO Routing Code)

## Field Description
A barcode containing the DHL ISO Routing Code, which encodes destination country, destination postcode, transport product code, and associated product features. Supports both ASC MH10 (prefix "2L", Code 128) and GS1 (prefix "403", GS1-128) standards.

## Format & Validation Rules
- **Data Type:** barcode (Code 128 or GS1-128)
- **Length:** Variable; structured fields with fixed and variable-length components
- **Pattern/Regex:** ASC MH10: `\(2L\)[A-Z]{2}.+\+\d{2}\d{2}\d{1}\d{3}.*`; GS1: `\(403\)\d{3}.+\+\d{2}\d{2}\d{1}\d{3}.*`
- **Allowed Values:** See sub-field specifications
- **Required:** yes (the whole barcode is either printed or not printed)

## Examples from Spec
- `(2L)BE3500+11311002123456` — EUROPACK piece to Belgium with region-specific routing
- `(2L)DE81541+05000000556677` — DOM EUROPACK to Germany, no fixed date/time/features, domestic routing code = street and house number
- `(2L)CH3000+57520001` — ECONOMY SELECT to Switzerland, hold at depot, customs clearance
- `(2L)NL1023FG+48101081` — EXPRESS WORLDWIDE to Netherlands, delivery at 10th of month, time code 1, feature sum 081
- GS1: `(403)7563000+57520001` — Same Switzerland example in GS1 format

## Position on Label
Part of the DHL handling information section on the transport label.

## Edge Cases & Notes
- Parentheses around the Data Identifier appear only in human-readable text, NOT in the barcode itself.
- DHL Express-internal applications will only produce ASC MH10 routing barcodes starting with "2L".
- Both ASC MH10 and GS1 standards are complementary and can co-exist.
- A product/feature block always consists of 8 digits regardless of products/features chosen.
- The routing barcode may have an exceptional minimum height of 11 mm (vs. standard 25 mm for other barcodes).
- Postcode may never contain spaces or symbols. If no postcode system exists for the country, the field remains empty.
- Known DHL Service Area Code (3 chars) or Delivery Facility Identifier (6 chars) can replace postcode, separated by ":".

## Claude Confidence
HIGH — Spec provides detailed structure breakdown, multiple examples, and clear field definitions.

## Review Status
- [ ] Reviewed by human