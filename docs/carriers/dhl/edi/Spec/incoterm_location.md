# Field: incoterm_location

## Display Name
Incoterm Location / Place of Delivery Terms

## Field Description
A segment (SG31 - LOC) to identify a location related to the incoterms at both shipment and invoice levels.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — up to 1 occurrence following TOD

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
Per change report v1.3.8, corrections were made to show how DHL Express Facility Codes should be given in SG31 - LOC and SG43 - LOC segments.

## Claude Confidence
MEDIUM — Described in structure; DHL facility code usage clarified in change report.

## Review Status
- [ ] Reviewed by human