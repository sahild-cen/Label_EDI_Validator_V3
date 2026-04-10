# Field: pdf417_barcode

## Display Name
PDF417 Barcode

## Field Description
A 2D barcode (PDF417 symbology) that must print on international shipping labels when required, containing shipment data. Used particularly with UPS Paperless Invoice shipments and when a forward or return indicator is needed for exchange services.

## Format & Validation Rules
- **Data Type:** barcode (PDF417)
- **Length:** variable
- **Pattern/Regex:** Not specified in spec (refers to separate PDF417 Barcode Symbology document)
- **Allowed Values:** Not restricted
- **Required:** conditional — required for international paperless shipments and certain exchange service labels

## Examples from Spec
Shown as "SAMPLE" barcode image on multiple label examples (Paperless Invoice 4x4.25 and 4x6 formats, International Forms Image Upload labels).

## Position on Label
- On 4" x 4.25" label format: prints on a 2nd label (backup document)
- On 4" x 6" label format: prints at the bottom of the label

## Edge Cases & Notes
- The spec states "For details on the PDF417 Barcode, please refer to the PDF417 Barcode Symbology document."
- For UPS Returns Exchange Service, the PDF417 must contain a forward or return indicator.
- The backup document label also shows "TR#" (tracking number) and "SHP#" (shipper number) alongside the PDF417.

## Claude Confidence
MEDIUM — the field is clearly required but detailed encoding specs are in a separate document.

## Review Status
- [ ] Reviewed by human