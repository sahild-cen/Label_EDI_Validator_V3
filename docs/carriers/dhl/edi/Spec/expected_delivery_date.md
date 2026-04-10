# Field: expected_delivery_date

## Display Name
Expected Delivery Date

## Field Description
A segment at shipment level (SG25 - DTM) to indicate date and time such as expected delivery.

## Format & Validation Rules
- **Data Type:** date
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — at shipment level, up to 3 occurrences allowed

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
Distinct from the header-level DTM which captures message creation date. This is specifically noted for expected delivery at shipment level.

## Claude Confidence
MEDIUM — Described in the declaration of data elements but detailed format not in extracted text.

## Review Status
- [ ] Reviewed by human