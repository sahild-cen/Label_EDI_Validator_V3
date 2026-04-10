# Field: billing_option

## Display Name
Billing Option

## Field Description
Indicates the billing method for the shipment (e.g., Prepaid). Must follow the specifications outlined in the UPS Guide to Labeling.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** "P/P" (Prepaid) shown in examples; full list in main UPS Guide to Labeling
- **Required:** yes

## Examples from Spec
- "BILLING: P/P"

## Position on Label
In the Additional Routing Instructions Block or billing area of the label.

## Edge Cases & Notes
Full specifications for billing options are referenced in the main UPS Guide to Labeling, not in this supplement.

## Claude Confidence
MEDIUM — example shown but full allowed values referenced in separate document

## Review Status
- [ ] Reviewed by human