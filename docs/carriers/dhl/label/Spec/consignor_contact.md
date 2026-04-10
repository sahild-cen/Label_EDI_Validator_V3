# Field: consignor_contact

## Display Name
Consignor's Contact

## Field Description
Shipper contact details that are critical operational information, captured and stored as part of the shipment preparation process in accordance with GDPR.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — no longer required to be printed on the Transport Label in most cases; required only in exceptional circumstances (e.g., compliance with ICAO or IATA for goods with UN Code UN3373) upon formal approval

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in spec for standard labels (no longer required to be printed).

## Edge Cases & Notes
- Information is made available electronically to DHL employees and operators rather than printed on label
- Exceptional circumstances requiring printing include compliance with international regulations like ICAO or IATA for goods with UN Code UN3373
- Only upon formal approval may specific contact details be printed on the Transport Label
- GDPR compliance governs how this data is captured and stored

## Claude Confidence
HIGH — spec explicitly states this is no longer required on labels except in specific regulated cases

## Review Status
- [ ] Reviewed by human