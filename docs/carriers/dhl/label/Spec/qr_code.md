# Field: qr_code

## Display Name
QR Code (Customer-Facing / LabelFree)

## Field Description
A QR Code barcode used to encode operational data for PUD (Pick-Up and Delivery) and In-Facility domains, particularly in the context of LabelFree scenarios. May encode alphabetic characters, numbers, double characters, and URLs.

## Format & Validation Rules
- **Data Type:** barcode (2D QR Code)
- **Length:** Variable
- **Pattern/Regex:** Per ISO/IEC 18004:2006 and ISO/IEC 18004:2015
- **Allowed Values:** Alphabetic characters, numbers, double characters, URLs
- **Required:** conditional — used in LabelFree scenarios

## Examples from Spec
No specific encoded data examples in the extracted text.

## Position on Label
Not specified in the extracted text for exact position; used in LabelFree context.

## Edge Cases & Notes
- Implementation is based on ISO/IEC 18004:2006 and compliant with ISO/IEC 18004:2015.
- Referenced under "Global SOP Customer-Facing QR-Code Specifications" as a separate document.
- Uses square modules with a unique perimeter pattern for scanner cell location determination.

## Claude Confidence
MEDIUM — The spec describes the symbology and its use case but detailed content specifications are in a separate referenced document.

## Review Status
- [ ] Reviewed by human