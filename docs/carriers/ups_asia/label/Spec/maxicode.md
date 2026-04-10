# Field: maxicode

## Display Name
MaxiCode (2D Barcode)

## Field Description
A two-dimensional MaxiCode barcode containing encoded shipment data including destination postal code, country code, class of service, tracking number, and address information. Used by UPS for automated package sortation.

## Format & Validation Rules
- **Data Type:** barcode (MaxiCode 2D)
- **Length:** approximately 100 characters of information
- **Pattern/Regex:** Structured data string with message header `[)><RS>01<GS>96`, followed by postal code, country code, class of service, tracking number, SCAC, account number, Julian day, shipment ID, package count, weight, address validation, address, city, state, terminated by `<RS><EOT>`
- **Allowed Values:** UPPERCASE characters only; no punctuation allowed in the data string except "/" in package count field
- **Required:** yes

## Examples from Spec
- Validated address: `[)><RS>01<GS>96303281483<GS>840<GS>001<GS>1Z12345673<GS>UPSN<GS>1X2X3X<GS>187<GS><GS>1/1<GS>37<GS>Y<GS>123<FS>567<GS>ATLANTA<GS>GA<RS><EOT>`
- Non-validated: `[)><RS>01<GS>96841706672<GS>840<GS>001<GS>1Z12345673<GS>UPSN<GS>1X2X3X<GS>187<GS><GS>1/1<GS>10<GS>N<GS>19 SOUTH ST<GS>SALT LAKE CITY<GS>UT<RS><EOT>`
- International: `[)><RS>01<GS>9651147<GS>276<GS>066<GS>1Z12345677<GS>UPSN<GS>1X2X3X<GS>187<GS><GS>1/1<GS>10<GS>N<GS>5 WALDSTRASSE<GS>COLOGNE<GS><RS><EOT>`
- Letter/Envelope: `[)><RS>01<GS>96841706672<GS>840<GS>001<GS>1Z12345673<GS>UPSN<GS>1X2X3X<GS>187<GS><GS>1/1<GS>1<GS>N<GS>1 MAIN ST<GS>SALT LAKE CITY<GS>UT<RS><EOT>`

## Position on Label
Shown on label example in the middle-right area, labeled as "MaxiCode" with the bull's-eye finder pattern.

## Edge Cases & Notes
- Use Mode 2 for all-numeric postal codes (up to 9 characters); use Mode 3 for alphanumeric postal codes (up to 6 characters). If longer, truncate from the right.
- Encode postal codes without spaces or special characters like dashes.
- Blank fields must still be separated with a `<GS>` character.
- For Letters/Envelopes, the Package Weight field is left blank.
- For UPS Worldwide Express Freight, weight field is left blank if it exceeds the maximum characters allowed.
- Some non-U.S. destinations will not have a state/province — the field separator is still required.
- Customer data (purchase orders, invoice numbers) can be appended using Application Identifiers (AI format header 05) or Data Identifiers (DI format header 06).
- Primary message = Postal Code + Country Code + Class of Service. Secondary message = everything else.
- Printer manufacturers may rearrange the primary and secondary message order.

## Claude Confidence
HIGH — spec provides extensive detail on MaxiCode data format, multiple examples, and encoding rules.

## Review Status
- [ ] Reviewed by human