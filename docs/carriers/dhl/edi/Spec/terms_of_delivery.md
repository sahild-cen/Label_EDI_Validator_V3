# Field: terms_of_delivery

## Display Name
Terms of Delivery / Incoterms

## Field Description
A segment (SG31 - TOD) to indicate terms of delivery/incoterms at both shipment and invoice level.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted (standard Incoterms expected)
- **Required:** yes (Required at SG31, 1 occurrence at shipment level)

## Examples from Spec
No examples in spec. Document change report mentions usage samples for LBBX Baby or Mother service code were added.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
TOD appears at both shipment level and invoice level. Per v1.1 update, element 4052:2 was added for Account Number. LOC segment follows TOD to identify a location related to the incoterms.

## Claude Confidence
MEDIUM — Required segment clearly identified but detailed code values not in extracted text.

## Review Status
- [ ] Reviewed by human