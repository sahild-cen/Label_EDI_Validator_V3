# Field: reference_number

## Display Name
Reference Number (Shipper Reference)

## Field Description
A customer-defined reference number for the shipment, used by the shipper to cross-reference with their own systems (e.g., order number, invoice number).

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable, typically up to 35 characters
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted (customer-defined)
- **Required:** no

## Examples from Spec
No examples in spec.

## Position on Label
Typically in the reference/details section of the label.

## Edge Cases & Notes
Multiple reference numbers may be supported. DHL labels commonly allow at least one shipper reference field. This is visible on the label and may appear in tracking information.

## Claude Confidence
HIGH — Standard optional field on DHL labels.

## Review Status
- [ ] Reviewed by human