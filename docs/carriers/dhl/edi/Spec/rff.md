# Field: RFF

## Display Name
Reference

## Segment ID
RFF

## Required
no

## Description
Provides reference numbers and identifiers for various purposes throughout the message.

## Subfields

### reference_qualifier
- **Element Position:** 1.1
- **Pattern/Regex:** ABT|ABW|ACL|AFE|ANK|AVY|BRD|CN|CU|DA|EI|ERN|FT|HS|MF|MRN|VA|ZZZ
- **Required:** yes
- **Description:** Reference function qualifier — VA = VAT registration number, CU = Customer/Shipper reference, ACL = Mother shipment AWB / Piece reference, EI = EIN (US tax ID), HS = Harmonized System code, MF = Manufacturer part number, ZZZ = Mutually defined (e.g. tax ID or original export date), DA = Account number, ERN = Original export tracking ID, CN = Original carrier name, MRN = Movement Reference Number, FT = Free trade zone ID, ABW = SKU number, BRD = Brand name, AFE = Additional reference, ABT = Additional reference, ANK = Additional reference, AVY = Additional reference

### reference_identifier
- **Element Position:** 1.2
- **Pattern/Regex:** .{1,70}
- **Required:** yes
- **Description:** Reference number or identifier value

### reference_country_code
- **Element Position:** 1.3
- **Pattern/Regex:** [A-Z]{2}
- **Required:** no
- **Description:** Country code associated with the reference (used with VA for VAT country, FT for free trade zone country)

## Edge Cases & Notes
RFF appears at many levels: message header (shipper tax IDs), consignment level (customer references, AWB cross-references), and invoice line item level (HS codes, part numbers, export references). RFF+VA may include a country code as third sub-component. RFF+ACL at consignment level links baby to mother AWB. RFF+ACL at piece level links baby piece to mother piece. RFF+HS carries the harmonized tariff code at line item level. For return shipments, RFF+ZZZ carries original export date, RFF+ERN carries original export tracking ID, RFF+CN carries original carrier name.

## Claude Confidence
HIGH — extensively documented with many qualifier values

## Review Status
- [ ] Reviewed by human