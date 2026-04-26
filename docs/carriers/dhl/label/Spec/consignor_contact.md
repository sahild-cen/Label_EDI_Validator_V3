# Field: consignor_contact

## Display Name
Consignor's Contact

## Field Description
Shipper contact details such as phone number or email. While still critical operational information, this is no longer required to be printed on the Transport Label as part of DHL's ongoing process improvements. The information is made available electronically to relevant employees.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — generally no longer printed on label; mandatory only in exceptional circumstances (e.g., compliance with ICAO or IATA regulations for goods with UN Code UN3373) upon formal approval

## Examples from Spec
"In exceptional circumstances (e.g. for compliance with international regulations like the ICAO or IATA for goods with UN Code UN3373) and only upon formal approval, specific contact details may have to be printed on the Transport Label."

## ZPL Rendering
- **Typical Position:** near the Ship From address area
- **Font / Size:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
This field has effectively been deprecated from standard label printing due to GDPR considerations. Contact details are captured and stored as part of the shipment preparation process but are made available electronically rather than printed. Only printed in exceptional circumstances with formal approval.

## Claude Confidence
HIGH — clearly described as conditional with detailed explanation

## Review Status
- [x] Reviewed by human