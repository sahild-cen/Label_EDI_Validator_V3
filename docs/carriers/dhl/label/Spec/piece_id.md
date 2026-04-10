# Field: piece_id

## Display Name
Piece ID (License Plate / Piece Tracking Number)

## Field Description
A unique identifier for each individual piece in a shipment, distinct from the master waybill/tracking number. Used for piece-level tracking.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable (typically up to 35 characters)
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** DHL system-generated
- **Required:** conditional — required for multi-piece shipments

## Examples from Spec
No examples in spec.

## Position on Label
Typically encoded in a barcode and may be displayed as human-readable text.

## Edge Cases & Notes
In multi-piece shipments, each piece has its own piece ID while sharing the same master waybill number. This enables individual piece tracking through the DHL network.

## Claude Confidence
MEDIUM — Standard for multi-piece DHL Express shipments but format details not in extracted text.

## Review Status
- [ ] Reviewed by human