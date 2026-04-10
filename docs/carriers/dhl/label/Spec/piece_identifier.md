# Field: piece_identifier

## Display Name
Piece Identifier (License Plate / PID)

## Field Description
A Unique Identifier (code) assigned to a single transport unit by its issuer, in accordance with ISO/IEC 15459-1. It acts as the primary Piece Identifier (PID) standard for DHL Express and is used to uniquely identify each piece/package in a shipment.

## Format & Validation Rules
- **Data Type:** alphanumeric / barcode
- **Length:** Variable; the Data Identifier prefix is "JD01" followed by character string (exact length after DI clarified elsewhere in spec)
- **Pattern/Regex:** Not fully specified in extracted text; uses Data Identifier prefix (e.g., "JD01") per ISO/IEC 15459-1
- **Allowed Values:** Unique identifiers assigned by the label issuer per ISO/IEC 15459-1
- **Required:** yes

## Examples from Spec
No complete examples provided in the extracted text, though the spec references PID type "JD01" and notes that the number of characters following the Data Identifier was clarified in an update.

## Position on Label
Encoded in barcode on the DHL Transport Label; appears in both human-readable and barcoded format.

## Edge Cases & Notes
- The license plate shall be valid for the lifetime of the unit it is applied to.
- The spec distinguishes between Piece Identifier (piece level) and Shipment Identifier (shipment level).
- Historical term was "License Plate" — now referred to as "Piece Identifier" per spec updates.
- Encoded using Code 128 barcode symbology per ISO/IEC 15417.

## Claude Confidence
MEDIUM — The spec clearly defines the concept and references ISO standard, but exact format details (full length, complete regex) are not fully present in the extracted text.

## Review Status
- [ ] Reviewed by human