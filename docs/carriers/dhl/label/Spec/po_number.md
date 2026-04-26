# Field: po_number

## Display Name
Purchase Order Number

## Field Description
The purchase order number associated with the shipment, typically provided by the consignee/buyer. This is a specific type of reference number used for commercial shipments.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable, up to 35 characters
- **Pattern/Regex:** .{1,35}
- **Allowed Values:** Not restricted — customer-defined
- **Required:** no

## Examples from Spec
No examples in extracted spec text.

## ZPL Rendering
- **Typical Position:** reference area, lower section of label
- **Font / Size:** Not specified
- **Field Prefix:** "PO:" or "PO#:" or similar
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
May be used interchangeably with or in addition to the general reference number field. Important for B2B shipments where the receiver needs to match incoming packages to purchase orders.

## Claude Confidence
LOW — common shipping field but no specific DHL spec detail in extracted text

## Review Status
- [ ] Reviewed by human