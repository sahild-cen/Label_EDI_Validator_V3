# Field: data_matrix_barcode

## Display Name
2D Data Matrix Barcode

## Field Description
A bi-dimensional Data Matrix barcode used on the 2D-enabled Transport Label layout. Encodes operational or customer data per ISO/IEC 16022 specifications.

## Format & Validation Rules
- **Data Type:** barcode (2D Data Matrix)
- **Length:** Variable
- **Pattern/Regex:** Per ISO/IEC 16022 symbology specification
- **Allowed Values:** Operational data and/or customer data as defined by DHL
- **Required:** conditional — used on 2D-enabled Transport Label layouts

## Examples from Spec
No specific encoded data examples in the extracted text.

## Position on Label
Part of the 2D-enabled Transport Label layout (section 8.1.7 and 5.12).

## Edge Cases & Notes
- The spec introduces the "2D Data Matrix – Customer Data" section, formally defining the 2D-enabled Transport Label layout.
- Referenced under "Global SOP Data Matrix 2D Specifications" as a separate document.
- Bi-dimensional barcode symbol attributes are specified in section 9.3.

## Claude Confidence
MEDIUM — The spec references this element and its ISO standard, but detailed encoding content is not in the extracted text.

## Review Status
- [ ] Reviewed by human