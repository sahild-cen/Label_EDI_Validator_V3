# Field: maxicode_barcode

## Display Name
MaxiCode Barcode

## Field Description
A 2D barcode symbology (MaxiCode™) that encodes address and shipment data in a structured data string format, used for automated package sorting and routing. It contains both a primary message (postal code, country code, class of service) and a secondary message (tracking details, address information).

## Format & Validation Rules
- **Data Type:** barcode (2D MaxiCode symbology)
- **Length:** Approximately 100 characters maximum capacity
- **Pattern/Regex:** `[)><RS>01<GS>96{postal_code}<GS>{country_code}<GS>{class_of_service}<GS>{tracking_number}<GS>UPSN<GS>{account}<GS>{julian_day}<GS>{shipment_id}<GS>{n/x}<GS>{weight}<GS>{address_validation}<GS>{address}<GS>{city}<GS>{state}<RS><EOT>`
- **Allowed Values:** Structured ANSI data string with specific field separators
- **Required:** yes

## Examples from Spec
`[)><RS>01<GS>96303281483<GS>840<GS>001<GS>1Z12345673<GS>UPSN<GS>1X2X3X<GS>187<GS><GS>1/1<GS>37<GS>Y<GS>123<FS>567<GS>ATLANTA<GS>GA<RS><EOT>`

`[)><RS>01<GS>96841706672<GS>840<GS>001<GS>1Z12345673<GS>UPSN<GS>1X2X3X<GS>187<GS><GS>1/1<GS>10<GS>N<GS>19 SOUTH ST<GS>SALT LAKE CITY<GS>UT<RS><EOT>`

`[)><RS>01<GS>9651147<GS>276<GS>066<GS>1Z12345677<GS>UPSN<GS>1X2X3X<GS>187<GS><GS>1/1<GS>10<GS>N<GS>5 WALDSTRASSE<GS>COLOGNE<GS><RS><EOT>`

## Position on Label
Not specified in spec (position on label not stated in extracted text, though typically upper portion of UPS labels).

## Edge Cases & Notes
- Mode 2 is used for US destinations (numeric postal codes up to 9 characters); Mode 3 is used for non-US destinations (alphanumeric postal codes up to 6 characters).
- Some label creation software providers interpret Mode 2 exclusively for US and Mode 3 exclusively for non-US.
- Non-printable characters are used: <GS> (decimal 29) separates fields, <RS> (decimal 30) separates format types, <FS> (decimal 28) separates primary/secondary address numbers, <EOT> (decimal 4) ends transmission.
- If MaxiCode exceeds maximum length, first clear Shipment ID Number field, then shorten Ship-To Address field.
- Printer manufacturers may rearrange the primary/secondary message order.

## Claude Confidence
HIGH — spec provides detailed data string format, multiple examples, and explicit encoding rules

## Review Status
- [x] Reviewed by human