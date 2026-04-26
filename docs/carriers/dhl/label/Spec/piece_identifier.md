# Field: piece_identifier

## Display Name
Piece Identifier (License Plate / PID)

## Field Description
A unique identifier assigned to each individual piece (package) within a shipment. This is the primary barcode on the transport label and must be encoded in Code 128 barcode symbology. Each piece of each shipment shipped with DHL requires a Piece Identifier. Any ISO 15459-compliant Piece Identifier may be used.

## Format & Validation Rules
- **Data Type:** alphanumeric (barcode + human-readable text)
- **Length:** max 35 characters (excluding the Data Identifier "J"); JD01-type identifiers are exactly 20 characters after the Data Identifier
- **Pattern/Regex:** `^[A-Z0-9]{1,35}$` — only numeric and uppercase alphabetic characters from ISO/IEC 646; no lowercase or punctuation
- **Allowed Values:** Must start with a string representing an issuing agency assigned by ISO. DHL-issued PIDs usually begin with "JD00" or "JD01"
- **Required:** yes

## Examples from Spec
- JD01 format with Data Identifier: barcode encodes "JJD01…" and human readable prints "(J)JD01 ….."
- Human-readable must be grouped in blocks of four digits following the (Sub-)Issuing Agency Code, built left to right so last four digits form a group

## ZPL Rendering
- **Typical Position:** lower portion of the label, piece identifier segment
- **Font / Size:** Human-readable text printed below the barcode
- **Field Prefix:** Data Identifier "(J)" in human-readable form; "J" in barcode (no parentheses in barcode)
- **ZPL Command:** ^BC (Code 128); Code 39 must NOT be used on DHL-produced labels

## Edge Cases & Notes
- The Data Identifier "J" is NOT part of the Piece Identifier itself for length determination, but must always be printed in both human-readable and barcoded format.
- Parentheses around the Data Identifier appear only in human-readable form, never in the barcode.
- Two Piece Identifiers are considered identical if their only difference is the Data Identifier prefix (e.g., "J" vs "2J").
- Grouping in blocks of four digits is mandatory for all DHL-owned customer automation software.
- If the label is split into two smaller labels, the label without the PID barcode must still show the PID in human-readable form with minimum 8-point font.
- Minimum barcode height: 25mm.

## Claude Confidence
HIGH — extensively specified in the document with clear rules

## Review Status
- [ ] Reviewed by human