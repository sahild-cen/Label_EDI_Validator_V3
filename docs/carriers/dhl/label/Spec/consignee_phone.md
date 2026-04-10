# Field: consignee_phone

## Display Name
Consignee Phone Number

## Field Description
The telephone number of the receiver/consignee for delivery contact and customs clearance purposes.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — required for international shipments and certain service types

## Examples from Spec
No examples in spec.

## Position on Label
Within or near the consignee address block.

## Edge Cases & Notes
Critical for international shipments as customs brokers and delivery couriers may need to contact the receiver. Should include country dialing code.

## Claude Confidence
HIGH — Required for international DHL Express shipments.

## Review Status
- [ ] Reviewed by human