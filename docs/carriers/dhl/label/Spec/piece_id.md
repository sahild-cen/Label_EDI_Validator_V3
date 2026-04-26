# Field: piece_id

## Display Name
Piece ID (License Plate)

## Field Description
A unique identifier assigned to each individual piece in a shipment. Also known as the license plate number (LPN). This is distinct from the master tracking/waybill number and allows individual piece-level tracking within a multi-piece shipment.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable, typically up to 35 characters
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** DHL system-generated unique piece identifiers
- **Required:** conditional — required for multi-piece shipments

## Examples from Spec
No examples in extracted spec text.

## ZPL Rendering
- **Typical Position:** near the piece-level barcode, often below or alongside the tracking barcode
- **Font / Size:** Not specified
- **Field Prefix:** None or "Piece ID:"
- **ZPL Command:** ^BC (Code 128) for barcode; ^FD for human-readable

## Edge Cases & Notes
The piece ID may be encoded in its own barcode separate from the master AWB barcode. In DHL's system, the piece ID enables individual package tracking even when multiple pieces share the same waybill number.

## Claude Confidence
MEDIUM — known DHL operational field

## Review Status
- [ ] Reviewed by human