# Field: shipper_account_number

## Display Name
Shipper Account Number (DHL Account Number)

## Field Description
The DHL account number of the shipper used for billing and identification purposes.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 9 digits
- **Pattern/Regex:** `^\d{9}$`
- **Allowed Values:** Valid DHL account numbers
- **Required:** yes

## Examples from Spec
No examples in spec.

## Position on Label
Typically displayed in the shipper information area or billing section of the label.

## Edge Cases & Notes
The account number determines billing and may affect available services. DHL Express account numbers are typically 9 digits. Different account numbers may be used for shipper, receiver, or third-party billing.

## Claude Confidence
HIGH — Required for all DHL Express shipments.

## Review Status
- [ ] Reviewed by human