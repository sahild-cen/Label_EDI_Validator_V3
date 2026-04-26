# Field: destination_postcode

## Display Name
Destination Postcode

## Field Description
The postcode of the consignee's destination address, encoded within the routing barcode. Variable length up to 12 characters. The postcode must not contain spaces or symbols. If the country has no postcode system, this field is omitted entirely.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** Variable, max 12 characters
- **Pattern/Regex:** `[A-Za-z0-9]{1,12}` — no spaces or symbols allowed
- **Allowed Values:** Valid postcodes for the destination country; alternatively a DHL Service Area Code (3 chars) or DHL Delivery Facility Identifier (6 chars) separated by ":"
- **Required:** conditional — mandatory where a postcode system exists; omitted for countries without postcodes

## Examples from Spec
- `3500` (Belgium), `81541` (Germany), `3000` (Switzerland), `1023FG` (Netherlands)

## ZPL Rendering
- **Typical Position:** Part of routing barcode and routing code human-readable area
- **Font / Size:** Not specified
- **Field Prefix:** None — directly follows country code in routing string
- **ZPL Command:** Encoded within routing barcode (^BC); also displayed as ^FD text

## Edge Cases & Notes
- Must never contain spaces or symbols.
- If no postcode system exists for the country, this field is omitted entirely (not populated with zeroes).
- DHL Service Area Code (3 chars) or Delivery Facility Identifier (6 chars) can substitute, separated from country code by ":".
- This is one of the few routing barcode fields that is truly optional/omittable.

## Claude Confidence
HIGH — explicitly detailed in routing barcode structure with examples

## Review Status
- [ ] Reviewed by human