# Field: RFF (SG32 Invoice Level)

## Display Name
References (Invoice Level)

## Segment ID
RFF

## Required
no

## Description
A segment indicating Registration Numbers and various Invoice Reference numbers. Part of Segment Group 32 at Invoice Level. Up to 999 occurrences.

## Subfields

### reference_code_qualifier
- **Element Position:** 1.1
- **Pattern/Regex:** (CU|ABT|[A-Z]{2,3})
- **Required:** yes
- **Description:** Reference code qualifier (element 1153 within C506 composite). Use 'CU' = Consignor/Shipper's reference, 'ABT' = MRN (Master Reference No., goods declaration document identifier for export from Germany). Full list available from DHL Express.

### reference_identifier
- **Element Position:** 1.2
- **Pattern/Regex:** .{1,35}
- **Required:** yes
- **Description:** Reference identifier (element 1154). The reference number value.

## Edge Cases & Notes
Example: RFF+CU:1154345678'. Values are validated against Shipper OR Consignee Country Codes under SG4-NAD-3207 and SG43-NAD-3207.

## Claude Confidence
HIGH — spec clearly defines qualifiers and provides example

## Review Status
- [ ] Reviewed by human