# Field: pdf417_barcode

## Display Name
PDF417 Barcode

## Field Description
A 2D barcode (PDF417 symbology) that must print on the shipping label when required. Contains additional shipment data. Details are referenced to a separate PDF417 Barcode Symbology document.

## Format & Validation Rules
- **Data Type:** barcode (2D)
- **Length:** variable
- **Pattern/Regex:** Not specified in spec (refers to separate document)
- **Allowed Values:** Not specified in spec
- **Required:** conditional — "must print on the shipping label when required"

## Examples from Spec
Visible in label diagrams for Access Point labels.

## Position on Label
Appears on the shipping label; exact position varies by label format but visible in Access Point label examples.

## ZPL Rendering
- **Typical Position:** Varies by label format; on 4x4.25 second label it appears in the lower section
- **Font / Size:** Not specified
- **Field Prefix:** None — barcode
- **ZPL Command:** ^B7 (PDF417 barcode)

## Edge Cases & Notes
The spec references a separate "PDF417 Barcode Symbology document" for full details. This barcode is conditionally required — it must print when required by UPS but may not be needed for all shipments.

## Claude Confidence
MEDIUM — Spec mentions it but defers details to a separate document

## Review Status
- [ ] Reviewed by human