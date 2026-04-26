# Field: qr_code

## Display Name
QR Code (LabelFree)

## Field Description
A two-dimensional QR Code barcode used to encode operational data for pickup/delivery and in-facility domains, specifically in the context of DHL's LabelFree scenarios. Compliant with ISO/IEC 18004:2006 and ISO/IEC 18004:2015.

## Format & Validation Rules
- **Data Type:** barcode (QR Code)
- **Length:** reference capacity of 503 alpha-numeric characters
- **Pattern/Regex:** Not specified in spec — content per LabelFree business requirements
- **Allowed Values:** Not restricted
- **Required:** conditional — used in LabelFree scenarios

## Examples from Spec
No examples in spec.

## ZPL Rendering
- **Typical Position:** placed on screen/label to maximize quiet zone and protect finder patterns; minimum margin to border of 4 modules
- **Font / Size:** Data contents not shown verbatim; excerpts may be displayed similar to 1D codes
- **Field Prefix:** None — barcode
- **ZPL Command:** ^BQ (QR Code)

## Edge Cases & Notes
- Module size: 0.51mm / 20 mil.
- Symbol matrix version: 17 (85x85 modules + 4x4 modules quiet zone).
- Symbol size: 44x44mm including quiet zone.
- Error correction level: H (highest).
- Quiet zone: 4×4 modules.
- Quality grade: C per ISO/IEC 15415 and ISO/IEC 16480.
- Primarily intended for LabelFree business context.

## Claude Confidence
MEDIUM — described in symbology section but specific to LabelFree context

## Review Status
- [ ] Reviewed by human