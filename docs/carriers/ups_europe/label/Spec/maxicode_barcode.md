# Field: maxicode_barcode

## Display Name
MaxiCode Barcode

## Field Description
A 2D MaxiCode barcode that encodes shipment routing information including postal code, country code, service class, and tracking number. This is a primary sort barcode used by UPS.

## Format & Validation Rules
- **Data Type:** barcode (2D MaxiCode)
- **Length:** Per MaxiCode specification
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Encoded routing and shipment data
- **Required:** yes

## Examples from Spec
No textual examples — appears as a graphic barcode on all label images.

## Position on Label
Middle-right area of the label, adjacent to the routing code. Appears as a circular/hexagonal 2D barcode symbol.

## ZPL Rendering
- **Typical Position:** Middle-right, next to routing code text
- **Font / Size:** Not applicable — barcode graphic
- **Field Prefix:** None — barcode
- **ZPL Command:** ^BD (MaxiCode barcode)

## Edge Cases & Notes
The MaxiCode encodes essential routing data. The spec includes detailed information about MaxiCode encoding modes. The barcode appears on every label example.

## Claude Confidence
HIGH — MaxiCode is the signature UPS barcode, clearly shown on all labels

## Review Status
- [ ] Reviewed by human