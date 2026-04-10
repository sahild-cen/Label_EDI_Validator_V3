# Field: maxicode

## Display Name
MaxiCode

## Field Description
A 2D MaxiCode symbology that encodes address, tracking, and shipment data elements for automated package sorting. It contains a structured data string with primary message (postal code, country code, class of service) and secondary message (tracking number, SCAC, account number, and other shipment details).

## Format & Validation Rules
- **Data Type:** barcode (MaxiCode 2D)
- **Length:** Approximately 100 characters of data capacity
- **Pattern/Regex:** Structured message format: `[)><RS>01<GS>96` + data fields separated by `<GS>` + `<RS><EOT>`
- **Allowed Values:** Structured data per UPS MaxiCode specification
- **Required:** yes

## Examples from Spec
- Validated address: `[)><RS>01<GS>96303281483<GS>840<GS>001<GS>1Z12345673<GS>UPSN<GS>1X2X3X<GS>187<GS><GS>1/1<GS>37<GS>Y<GS>123<FS>567<GS>ATLANTA<GS>GA<RS><EOT>`
- Non-validated US: `[)><RS>01<GS>96841706672<GS>840<GS>001<GS>1Z12345673<GS>UPSN<GS>1X2X3X<GS>187<GS><GS>1/1<GS>10<GS>N<GS>19 SOUTH ST<GS>SALT LAKE CITY<GS>UT<RS><EOT>`
- International (Germany): `[)><RS>01<GS>9651147<GS>276<GS>066<GS>1Z12345677<GS>UPSN<GS>1X2X3X<GS>187<GS><GS>1/1<GS>10<GS>N<GS>5 WALDSTRASSE<GS>COLOGNE<GS><RS><EOT>`
- Letter/Envelope: `[)><RS>01<GS>96841706672<GS>840<GS>001<GS>1Z12345673<GS>UPSN<GS>1X2X3X<GS>187<GS><GS>1/1<GS>1<GS>N<GS>1 MAIN ST<GS>SALT LAKE CITY<GS>UT<RS><EOT>`

## Position on Label
Not specified precisely in this extract, but typically upper-left or upper area of UPS labels.

## ZPL Rendering
- **Typical Position:** Upper portion of label (standard UPS label layout)
- **Font / Size:** Not applicable (2D barcode)
- **Field Prefix:** None — barcode
- **ZPL Command:** ^BD (MaxiCode)

## Edge Cases & Notes
- Mode 2 is used for US destinations (postal codes 5 or 9 numeric characters); Mode 3 for non-US destinations (postal codes up to 6 alphanumeric characters).
- Some label software providers interpret Mode 2 for US and Mode 3 for non-US exclusively.
- Non-printable characters: `<GS>` = decimal 29 (group separator), `<RS>` = decimal 30 (record separator), `<FS>` = decimal 28 (field separator), `<EOT>` = decimal 4 (end of transmission).
- Each printer manufacturer may rearrange the data string order (primary vs. secondary message) — see examples for ABC and XYZ printers.
- If MaxiCode exceeds maximum length: first clear the Shipment ID Number field (saves ~11 chars), then shorten the Ship-To Address field.
- Customer data (invoice/PO numbers) can be appended using Data Identifiers (format header 06) or Application Identifiers (format header 05).

## Claude Confidence
HIGH — spec provides extensive detail on MaxiCode data structure, multiple examples, and encoding rules

## Review Status
- [ ] Reviewed by human