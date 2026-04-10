# Field: goods_item_details

## Display Name
Goods Item Details

## Field Description
A segment (SG50 - GID) to identify a goods item for which transport is undertaken. Contains goods item identification details at piece level.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes (Mandatory at SG50, 1 occurrence)

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
GID appears at both shipment piece level and invoice line item level. At piece level it is part of a group that includes measurements, dimensions, references, package identification, and dangerous goods information.

## Claude Confidence
MEDIUM — Clearly mandatory at SG50 level.

## Review Status
- [ ] Reviewed by human