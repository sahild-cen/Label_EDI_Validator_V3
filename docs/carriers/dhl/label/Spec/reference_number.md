# Field: reference_number

## Display Name
Reference Number

## Field Description
A customer-defined reference number associated with the shipment. This can be an order number, internal reference, or any identifier the shipper uses to cross-reference the shipment in their own systems.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable, up to 35 characters
- **Pattern/Regex:** .{1,35}
- **Allowed Values:** Not restricted — customer-defined
- **Required:** no

## Examples from Spec
No examples in extracted spec text.

## ZPL Rendering
- **Typical Position:** lower section of label or reference area
- **Font / Size:** Not specified
- **Field Prefix:** "Ref:" or "Reference:" or similar
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
DHL may support multiple reference fields (Reference 1, Reference 2, etc.). These references are searchable in DHL's tracking systems and appear on invoices and reports. Some customers use this for PO numbers, department codes, or cost center identifiers.

## Claude Confidence
MEDIUM — standard optional field on DHL labels

## Review Status
- [ ] Reviewed by human