# Field: two_d_data_matrix

## Display Name
2D Data Matrix – Customer Data

## Field Description
A two-dimensional Data Matrix barcode encoding operational data using ISO/IEC 15434 standard. Contains multiple segments: a mandatory public segment (standardized package data), an open segment (DHL EDIFACT data), and optional customer segments.

## Format & Validation Rules
- **Data Type:** barcode (2D Data Matrix ECC 200)
- **Length:** variable — typically requires at least 200 characters capacity
- **Pattern/Regex:** ISO/IEC 15434 encoding format with multiple segments
- **Allowed Values:** Concatenated data from public, open, and customer segments per Global SOP "Data Matrix 2D Specifications"
- **Required:** conditional — public segment is mandatory; open and customer segments are systematically used

## Examples from Spec
No specific data content examples provided in this extract.

## Position on Label
Placed to maximize quiet zone and protect finder patterns from damage. Must meet ISO 15394:2017 requirements. Located in the 2D symbol area of the label.

## Edge Cases & Notes
- Segments always appear in fixed sequence: public, open, customer
- Only public segment is mandatory but both public and open are in systematic use
- Symbology: Data Matrix ECC 200
- Module size: 0.38 mm (nominal range 0.40 > x > 0.38)
- Quality Grade: B
- Encoding: Currently 7-bit data only
- Human readable: Data contents not shown verbatim; excerpts like public information displayed similar to 1D codes
- Smallest possible symbol matrix should be used for best readability

## Claude Confidence
HIGH — spec provides clear symbology details, segment structure, and technical parameters

## Review Status
- [ ] Reviewed by human