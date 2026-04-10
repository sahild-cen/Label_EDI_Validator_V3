# Field: consignee_name_and_address

## Display Name
Consignee / Receiver Name and Address

## Field Description
A segment (SG43 - NAD) at shipment level to indicate names and addresses of the consignee, importer, or exporter party roles.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes (Required — up to 9 occurrences at SG43)

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
SG43 NAD supports multiple party roles: Consignee, Importer, Exporter. Per change report v0.8, NAD+JD qualifier was added for Port of Entry address. For Loose BBX (LBBX) shipments, the Baby Importer must be the same as the Mother Receiver.

## Claude Confidence
HIGH — Clearly defined in both the declaration and document change report.

## Review Status
- [ ] Reviewed by human