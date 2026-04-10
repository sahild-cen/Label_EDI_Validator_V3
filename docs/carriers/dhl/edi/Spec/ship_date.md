# Field: ship_date

## Display Name
Ship Date / Creation Date/Time

## Field Description
A segment indicating creation date and time of the message (DTM at header level), and date/time such as expected delivery at shipment level.

## Format & Validation Rules
- **Data Type:** date
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes (Required — appears at header level with max 2 occurrences)

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
DTM appears at multiple levels: Header level (message creation date/time), Shipment level (expected delivery date), and Invoice level (date related to invoice). Up to 2 occurrences at header level.

## Claude Confidence
MEDIUM — DTM is defined as Required at header level but exact date format codes not visible in extracted text.

## Review Status
- [ ] Reviewed by human