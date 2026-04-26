# Field: billing_type

## Display Name
Billing Type / Payment Method

## Field Description
Indicates who is responsible for paying the shipping charges — the shipper, the receiver, or a third party. Determines the billing account used for the shipment.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** "SHIPPER" (S), "RECEIVER" (R), "THIRD PARTY" (T)
- **Required:** yes

## Examples from Spec
No examples in extracted spec text.

## ZPL Rendering
- **Typical Position:** billing/payment area of label
- **Font / Size:** Not specified
- **Field Prefix:** "Bill To:" or "Payment:" or similar
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
When billing type is "RECEIVER" or "THIRD PARTY", the corresponding DHL account number must be provided. This field may also be encoded in the shipment data rather than explicitly printed as a separate text field on some label formats.

## Claude Confidence
LOW — standard field but minimal spec detail

## Review Status
- [x] Reviewed by human