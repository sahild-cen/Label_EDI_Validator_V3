# Field: consignment_number

## Display Name
Consignment Number / Transport Document Number

## Field Description
A segment to indicate consignments included in the consolidation using the transport document/message number. This is the primary consignment identifier at the shipment level (CNI segment).

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes (Mandatory at SG25 Shipment Level)

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
CNI segment appears at both Shipment Level and Invoice Level within SG25. At the shipment level it carries the transport document number; at the invoice level it carries invoice information.

## Claude Confidence
MEDIUM — CNI segment is clearly defined as mandatory at shipment level, but detailed format/length not provided in extracted text.

## Review Status
- [ ] Reviewed by human