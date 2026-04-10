# Field: weight

## Display Name
Weight

## Field Description
The actual weight of the shipment/piece, displayed on the label for handling and billing reference.

## Format & Validation Rules
- **Data Type:** numeric (decimal)
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Positive numeric values
- **Required:** yes

## Examples from Spec
No examples in spec.

## Position on Label
Typically in the shipment details section of the label.

## Edge Cases & Notes
Weight may be displayed in kilograms (kg) or pounds (lbs) depending on the origin country. DHL Express primarily uses kilograms for international shipments. Dimensional weight may also be considered for billing.

## Claude Confidence
HIGH — Standard element on all DHL labels.

## Review Status
- [ ] Reviewed by human