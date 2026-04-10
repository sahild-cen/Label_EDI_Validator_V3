# Field: description_of_goods

## Display Name
Description of Goods (DESC)

## Field Description
A general description of the contents/commodities being shipped, required for customs and identification purposes.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted — should describe shipment contents
- **Required:** yes (for international shipments)

## Examples from Spec
- `DESC: DOCUMENTS`
- `DESC: AUTO PARTS`
- `DESC: SHOES`
- `DESC: DOCUMENT BOX`
- `DESC: COMPUTER EQUIPMENT`

## Position on Label
In the lower portion of the label, below the billing information, prefixed with "DESC:".

## Edge Cases & Notes
Labeled as "General Description of Goods" in the spec's label callout annotations. For document box labels in World Ease, the description is "DOCUMENT BOX".

## Claude Confidence
HIGH — Consistently shown across all label examples with clear callout.

## Review Status
- [ ] Reviewed by human