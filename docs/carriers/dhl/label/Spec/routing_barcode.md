# Field: routing_barcode

## Display Name
Routing Barcode (ISO Routing Code)

## Field Description
A composite barcode containing the DHL ISO Routing Code, which encodes destination country, destination postcode, transport product, and associated product features. It is encoded in Code 128 (ASC MH10 with "2L" Data Identifier) or GS1-128 (with "403" Application Identifier). This barcode drives the automated sorting and routing of shipments through the DHL network.

## Format & Validation Rules
- **Data Type:** barcode (Code 128 or GS1-128)
- **Length:** Variable — minimum ~12 characters, structured fields with fixed-length components
- **Pattern/Regex:** ASC MH10: `2L[A-Z]{2}.{0,12}\+\d{2}\d{2}\d{1}\d{3}(\+.{0,6})?` ; GS1: `403\d{3}.{0,12}\+\d{2}\d{2}\d{1}\d{3}(\+.{0,6})?`
- **Allowed Values:** Structured per routing barcode specification (see structure below)
- **Required:** yes — the whole barcode is either printed or not printed (mandatory at printout level)

## Examples from Spec
- `(2L)BE3500+11311002123456` — EUROPACK piece to Belgium, postcode 3500, product 11, delivery date 31st, time code 1, feature 002, region code 123456
- `(2L)DE81541+05000000556677` — DOM EUROPACK to Germany, postcode 81541, no fixed date/time, no features, domestic routing code 556677
- `(2L)CH3000+57520001` — ECONOMY SELECT to Switzerland, postcode 3000, hold at depot, no fixed time, customs clearance feature 001
- `(2L)NL1023FG+48101081` — EXPRESS WORLDWIDE to Netherlands, postcode 1023FG, delivery on 10th, time code 1, features 081 (=1+16+64)
- GS1 example: `FNC1 403 756 3000+57520001` — Switzerland ECONOMY SELECT

## ZPL Rendering
- **Typical Position:** Routing barcode area of label
- **Font / Size:** Human-readable interpretation printed below barcode; parentheses around Data Identifier appear in human-readable only, not in barcode
- **Field Prefix:** "(2L)" or "(403)" in human-readable format only
- **ZPL Command:** ^BC (Code 128) for ASC MH10; ^BC with FNC1 for GS1-128

## Edge Cases & Notes
- Parentheses around Data Identifier ("2L" or "403") appear only in human-readable text, NOT in the barcode data itself.
- DHL Express internal applications will only produce ASC MH10 routing barcodes starting with "2L".
- Product/feature block is always 8 digits regardless of which products/features are chosen.
- Delivery date field is mandatory in the barcode even if no date is specified — must be populated with "00".
- Delivery time field is mandatory — must be populated with "0" if no time is specified.
- Handling feature code is mandatory — must be populated with "000" if no features selected.
- Postcode may never contain spaces or symbols; must be omitted entirely if country has no postcode system.
- Known DHL Service Area Code (3 chars) or Delivery Facility Identifier (6 chars) can be coded in place of postcode, separated by ":".
- Country-specific extension after second "+" separator is optional and may remain empty.
- Minimum barcode height is 25 mm standard or 11 mm for compact labels (approved in 2014).
- X-dimension: 0.33 mm to 0.51 mm for Code 128.

## Claude Confidence
HIGH — extensively detailed in the spec with full structure, examples, and field-by-field breakdown

## Review Status
- [ ] Reviewed by human