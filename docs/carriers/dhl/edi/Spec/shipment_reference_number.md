# Field: shipment_reference_number

## Display Name
Shipment Reference Number

## Field Description
A segment (SG32 - RFF) containing references and constants which apply to the entire consignment or shipment. Used to identify references used by a party.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes (Required at SG32 shipment level, up to 999 occurrences)

## Examples from Spec
No examples in spec. Change report v0.2 mentions clarification on the BBX reference value needed – C502.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
Up to 999 occurrences allowed, supporting multiple reference types. The BBX reference value was specifically clarified in v0.2. Per change report v1.2, RFF/C506/1156 was added.

## Claude Confidence
MEDIUM — Clearly required with high occurrence count; specific reference qualifiers not fully detailed in extracted text.

## Review Status
- [ ] Reviewed by human