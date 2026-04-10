# Field: documentation_indicator

## Display Name
Documentation Indicator

## Field Description
An indicator that identifies the type of international documentation accompanying the shipment, printed in the Additional Routing Instructions block.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** INV, INV-CC, EDI-CCP, EDI, and others
- **Required:** conditional — required for international shipments

## Examples from Spec
- `INV` (paper invoice shipments)
- `INV-CC` (World Ease with paper documents, CC = Customs Clearance)
- `EDI-CCP` (World Ease Paperless Invoice with Document Box)

## Position on Label
Top right corner of the Additional Routing Instructions Block. For World Ease labels, it also appears on the bottom right corner of the over-label.

## Edge Cases & Notes
For World Ease paper documentation shipments, the indicator is "INV-CC" (16 pt. bold). For Paperless Invoice with Document Box, it is "EDI-CCP" (16 pt. bold). All UPS Worldwide Economy labels must display "EDI". The indicator follows the format: base indicator + dash + modifier (e.g., INV-CC). All labels including the document box must display the same indicator.

## Claude Confidence
HIGH — Extensively documented with specific values and rules for different scenarios.

## Review Status
- [ ] Reviewed by human