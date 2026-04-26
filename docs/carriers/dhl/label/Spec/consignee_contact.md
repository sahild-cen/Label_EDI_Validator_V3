# Field: consignee_contact

## Display Name
Consignee's Contact

## Field Description
Consignee's contact details for delivery coordination. Similar to the consignor's contact, this information is no longer required to be printed on the Transport Label as part of DHL's ongoing improvements, but is made available electronically.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — generally no longer printed; mandatory only in exceptional circumstances (e.g., ICAO/IATA compliance for UN3373 goods) upon formal approval

## Examples from Spec
"Consignee's Shipper contact details are still critical operational information... this information is, however, no longer required to be printed on the Transport Label."

## ZPL Rendering
- **Typical Position:** near the Ship To address area
- **Font / Size:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Effectively deprecated from standard label printing due to GDPR. The area within the hooks of the Ship To address shall include the contact information when required. Only printed in exceptional circumstances with formal approval.

## Claude Confidence
HIGH — clearly described in spec section 5.8 annotation 9

## Review Status
- [x] Reviewed by human