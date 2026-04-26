# Field: data_matrix_2d

## Display Name
2D Data Matrix – Customer Data

## Field Description
A two-dimensional Data Matrix barcode (ECC 200) encoding operational data for use in pickup/delivery and in-facility domains. Contains concatenated data from public, open (DHL EDIFACT), and customer segments per ISO/IEC 15434 structure. The exhaustive list of encoded data elements is defined in DHL's "Data Matrix 2D Specifications" document.

## Format & Validation Rules
- **Data Type:** barcode (Data Matrix ECC 200)
- **Length:** variable — typically requires at least 200 character capacity
- **Pattern/Regex:** Not specified in spec — content per ISO/IEC 15434 segments
- **Allowed Values:** Concatenation of public segment (mandatory), open segment (systematically used), and customer segment (optional)
- **Required:** conditional — present on 2D-enabled transport labels

## Examples from Spec
No verbatim data examples in spec. Sample labels show the 2D symbol placement.

## ZPL Rendering
- **Typical Position:** placed to maximize quiet zone and protect finder patterns from damage; must meet ISO 15394:2017 requirements
- **Font / Size:** Human-readable interpretation is not shown verbatim; excerpts like public information may be displayed similar to 1D codes
- **Field Prefix:** None — barcode
- **ZPL Command:** ^BX (Data Matrix)

## Edge Cases & Notes
- Symbology: Data Matrix ECC 200, module size 0.38mm (nominal range 0.38–0.40mm, may extend to 0.24mm in future).
- Only square symbol matrices should be used; smallest possible matrix for best readability.
- Macro 06 should be used.
- Quiet zone: recommended minimum 4mm on all sides.
- Quality grade: B.
- Currently uses 7-bit data only (no ECI specification required).
- For sorting purposes, module size must not fall below 0.76mm.
- Three segments in fixed sequence: Public (mandatory), Open (systematically used), Customer (optional, not used by DHL).

## Claude Confidence
HIGH — detailed technical parameters provided in the spec

## Review Status
- [x] Reviewed by human