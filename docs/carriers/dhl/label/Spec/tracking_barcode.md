# Field: tracking_barcode

## Display Name
Tracking Number Barcode

## Field Description
The primary machine-readable barcode encoding the DHL tracking/waybill number. This is the main barcode scanned throughout the DHL network for package identification and tracking.

## Format & Validation Rules
- **Data Type:** barcode
- **Length:** corresponds to tracking number length (10-11 digits typically)
- **Pattern/Regex:** Encodes the tracking number value
- **Allowed Values:** Not restricted beyond valid tracking number
- **Required:** yes

## Examples from Spec
No examples in extracted spec text.

## ZPL Rendering
- **Typical Position:** center or lower portion of label, large barcode area
- **Font / Size:** Not applicable — barcode element
- **Field Prefix:** None — barcode
- **ZPL Command:** ^BC (Code 128) or ^BI (Interleaved 2 of 5) depending on DHL service

## Edge Cases & Notes
DHL Express typically uses Code 128 for the primary tracking barcode. The barcode must meet minimum height and width specifications for scanning reliability. Human-readable interpretation line should appear below the barcode.

## Claude Confidence
MEDIUM — standard DHL barcode element

## Review Status
- [ ] Reviewed by human