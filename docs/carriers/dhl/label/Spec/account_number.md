# Field: account_number

## Display Name
DHL Account Number

## Field Description
The DHL customer account number associated with the shipment for billing purposes. This identifies the shipper's commercial agreement with DHL.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 9 digits
- **Pattern/Regex:** ^\d{9}$
- **Allowed Values:** Valid DHL account numbers
- **Required:** yes

## Examples from Spec
No examples in extracted spec text.

## ZPL Rendering
- **Typical Position:** upper area of label, near shipper information
- **Font / Size:** Not specified
- **Field Prefix:** "ACCT:" or "Account:" or similar
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Third-party billing scenarios may show a different account number than the shipper's account. Some DHL services allow receiver-pays billing, in which case the receiver's account number may also appear.

## Claude Confidence
MEDIUM — standard DHL billing field

## Review Status
- [x] Reviewed by human