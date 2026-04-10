# Field: tracking_number_barcode

## Display Name
Tracking Number Barcode (1D Barcode)

## Field Description
A 1D barcode encoding the DHL tracking/waybill number for automated scanning and sortation throughout the DHL network.

## Format & Validation Rules
- **Data Type:** barcode
- **Length:** Encodes 10-11 digit tracking number
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Code 128 or Interleaved 2 of 5 symbology
- **Required:** yes

## Examples from Spec
No examples in spec.

## Position on Label
Typically in the upper-middle area of the label, prominently placed for scanning.

## Edge Cases & Notes
DHL Express labels typically use Code 128 symbology. The barcode must be scannable and meet minimum height requirements for automated sortation equipment.

## Claude Confidence
HIGH — Standard element on all DHL shipping labels.

## Review Status
- [ ] Reviewed by human