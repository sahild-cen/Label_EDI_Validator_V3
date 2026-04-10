# Field: destination_postcode

## Display Name
Destination Postcode

## Field Description
The postcode of the consignee/destination address, encoded within the routing barcode. Variable length, maximum 12 characters.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** Variable, max 12 characters
- **Pattern/Regex:** No spaces or symbols allowed in the barcode encoding
- **Allowed Values:** Valid postcodes for the destination country; alternatively, a DHL Service Area Code (3 chars) or DHL Delivery Facility Identifier (6 chars) separated from the country code by ":"
- **Required:** conditional — Mandatory where a postcode system exists for the destination country; omitted if the country has no postcode system

## Examples from Spec
- `3500` (Belgium)
- `81541` (Germany)
- `3000` (Switzerland)
- `1023FG` (Netherlands — alphanumeric postcode)

## Position on Label
Within the routing barcode, between the ISO Country Code and the field separator "+".

## Edge Cases & Notes
- Postcodes may never contain spaces or symbols when encoded in the routing barcode.
- If no postcode system exists, the field must be omitted entirely (not filled with zeroes).
- A DHL Service Area Code (3 chars) or Delivery Facility Identifier (6 chars) can substitute for the postcode, separated by a colon ":".

## Claude Confidence
HIGH — Spec clearly defines format, length constraints, and provides multiple examples.

## Review Status
- [ ] Reviewed by human