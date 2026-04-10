# Field: tracking_number

## Display Name
Tracking Number

## Field Description
The unique 1Z tracking number assigned by UPS to identify and track each individual package throughout the shipping network. This is the primary identifier for a UPS shipment.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 18 characters (including "1Z" prefix)
- **Pattern/Regex:** `1Z\s?[A-Z0-9]{3}\s?[A-Z0-9]{3}\s?[A-Z0-9]{2}\s?[0-9]{4}\s?[0-9]{4}`
- **Allowed Values:** Must begin with "1Z" prefix
- **Required:** yes

## Examples from Spec
- `1Z 1X2 X3X 66 1234 5676`
- `1Z 1X2 X3X 67 1234 5674`
- `1Z 1X2 X3X 03 0000 5772`
- `1Z 1X2 X3X 67 0000 5410`
- `1Z 1X2 X3X 04 0000 5403`
- `1Z 1X2 X3X 01 1234 5672`
- `1Z 1X2 X3X 54 0000 5408`
- `1Z 1X2 X3X 66 9500 5404`
- `1Z 1X2 X3X AA 0000 5601`
- `1Z 1X2 X3X YN 1234 5678`
- `1Z 1X2 X3X V3 0000 6705`
- `1Z 1X2 X3X V4 0000 5400`
- `1Z 1X2 X3X EN 0000 5450`
- `1Z 1X2 X3X E1 0000 5403`
- `1Z 1X2 X3X 68 0000 5409`
- `1Z 1X2 X3X DY 0000 5404`
- `1Z 1X2 X3X 6H 0000 5407`
- `1Z 1X2 X3X 9T 0000 5400`
- `1Z 1X2 X3X 90 0000 5402`
- `1Z 1X2 X3X 67 1100 5408`

## Position on Label
Displayed prominently in the lower portion of the label, preceded by the label text "TRACKING #:". Also encoded in a barcode (1D barcode) directly associated with the tracking number.

## Edge Cases & Notes
The tracking number is displayed with spaces for human readability but the underlying data is continuous. The two characters after the shipper number portion appear to encode the service type. The tracking number must be visible even when World Ease over-labels are applied.

## Claude Confidence
HIGH — Tracking number is clearly and consistently defined across all label examples with the "TRACKING #:" prefix.

## Review Status
- [ ] Reviewed by human