# Field: consignment_remarks

## Display Name
Consignment Remarks / Free Text

## Field Description
A segment (SG25 - FTX) at shipment level to specify free form or process available supplementary information, such as consignment remarks.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Multiple qualifiers including CCI for Custom Remarks/Instructions, AAU for Duty Free Import Remarks
- **Required:** conditional — up to 9 occurrences at shipment level

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
Per change report v1.3.9, notes were added for SG25/FTX with CCI qualifier on how to populate Custom Remarks/Instructions for if DHL renders Invoice Image (which may then be returned to shipper). Per v1.3.2, corrected mapping of Duty Free Import Remarks uses FTX with AAU qualifier.

## Claude Confidence
MEDIUM — FTX segment described with multiple qualifier types documented in change reports.

## Review Status
- [ ] Reviewed by human