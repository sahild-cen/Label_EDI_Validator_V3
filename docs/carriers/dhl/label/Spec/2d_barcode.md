# Field: 2d_barcode

## Display Name
2D Barcode (PDF417 / DataMatrix / QR Code)

## Field Description
A 2D barcode containing encoded shipment data including tracking number, origin, destination, service type, and other shipment details used for automated processing.

## Format & Validation Rules
- **Data Type:** barcode
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** PDF417 or DataMatrix symbology depending on product
- **Required:** conditional — required for DHL Express labels; may vary for other DHL products

## Examples from Spec
No examples in spec.

## Position on Label
Typically in the upper portion of the label, adjacent to or near the 1D tracking barcode.

## Edge Cases & Notes
The 2D barcode typically encodes a concatenation of multiple shipment data elements. For DHL Express, a PDF417 barcode is commonly used. The encoded data string follows DHL's proprietary format specification.

## Claude Confidence
MEDIUM — Standard on DHL Express labels but specific encoding format details are not in the extracted text.

## Review Status
- [ ] Reviewed by human