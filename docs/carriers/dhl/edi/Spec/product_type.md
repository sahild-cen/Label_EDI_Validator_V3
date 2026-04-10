# Field: product_type

## Display Name
Product Type / Transport Service

## Field Description
A segment (SG25 - TSR) indicating the DHL product type for transport service requirements at shipment level. Appendix A contains the full list of product types.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** See Appendix A – Product Type (not fully extracted)
- **Required:** yes (Required at shipment level, 1 occurrence)

## Examples from Spec
No examples in spec (Appendix A referenced but not fully extracted).

## Position on Label
Not specified in spec.

## Edge Cases & Notes
TSR also appears at SG49 level for party-specific transport service requirements. Appendix A contains the full enumeration of DHL product types.

## Claude Confidence
MEDIUM — TSR segment clearly defined as required; actual product type codes are in Appendix A which is referenced but content not fully extracted.

## Review Status
- [ ] Reviewed by human