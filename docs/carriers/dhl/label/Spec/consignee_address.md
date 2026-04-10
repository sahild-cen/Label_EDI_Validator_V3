# Field: consignee_address

## Display Name
Consignee Address (Ship-To Address)

## Field Description
The address block of the recipient/consignee to whom the shipment is being delivered. Contains all relevant delivery address information.

## Format & Validation Rules
- **Data Type:** string (multi-line text block)
- **Length:** Variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes (for ESS Label; not present on Network Label or Routing Label)

## Examples from Spec
No complete address examples in the extracted text.

## Position on Label
Dedicated segment on the DHL Transport Label. Subject to GDPR conditions. The spec references segments 5.6 and 5.8 for address specifications and GDPR considerations. A "Highly Compact Label" variant has specific segment specifications for the consignee address.

## Edge Cases & Notes
- GDPR regulations apply — contact details may only be printed in exceptional scenarios per GDPR guidelines.
- Account numbers and related GDPR-protected information are explicitly prohibited on Transport Labels.
- The Network Label does not include addresses. The Routing Label also omits addresses.
- The ESS Label includes full address information.

## Claude Confidence
MEDIUM — The spec clearly indicates this is a required field on ESS Labels with GDPR constraints, but detailed format/field breakdown is not fully provided in the extracted text.

## Review Status
- [ ] Reviewed by human