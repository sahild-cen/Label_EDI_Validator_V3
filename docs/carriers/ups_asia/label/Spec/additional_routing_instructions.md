# Field: additional_routing_instructions

## Display Name
Additional Routing Instructions

## Field Description
Documentation indicators required for proper international shipment processing, indicating the type of customs documentation accompanying the shipment.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable (3-7 characters)
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:**
  - `EDI-DOC` — Documents only shipment
  - `INV` — Shipping system generates invoice for dutiable shipment
  - `KEY` — Shipping system does not generate invoice for dutiable shipment and invoice is required
- **Required:** yes — for international shipments

## Examples from Spec
- `INV` (most label examples)
- `EDI-DOC` (UPS Saver envelope example)
- `KEY` (UPS Expedited example)
- `INV-RS1` (Express Freight Import Control example)

## Position on Label
Right-justified in the Additional Routing Instructions Block immediately below the highlight bar of the Tracking Number Barcode Block.

## Edge Cases & Notes
The `INV-RS1` variant appears on Import Control/Return Service labels. The spec explicitly states these are required for international shipments. Font size is 16 pt. bold.

## Claude Confidence
HIGH — Explicitly defined with three allowed values and shown on label examples.

## Review Status
- [ ] Reviewed by human