# Field: consignor_address

## Display Name
Consignor Address (Shipper / Ship-From Address)

## Field Description
The address block of the shipper/consignor who is sending the shipment. Contains the origin address information.

## Format & Validation Rules
- **Data Type:** string (multi-line text block)
- **Length:** Variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes (for ESS Label; not present on Network Label or Routing Label)

## Examples from Spec
No complete address examples in the extracted text.

## Position on Label
Dedicated segment on the DHL Transport Label. Subject to GDPR conditions. The spec references segment 5.2.1.1 for consignor address specifications, including a "Highly Compact Label" variant.

## Edge Cases & Notes
- GDPR regulations apply — same restrictions as consignee address regarding contact details and account numbers.
- Account numbers and related GDPR-protected information are explicitly prohibited on Transport Labels.

## Claude Confidence
MEDIUM — The spec clearly indicates this is a required segment with GDPR constraints, but detailed field breakdown is not fully provided in the extracted text.

## Review Status
- [ ] Reviewed by human