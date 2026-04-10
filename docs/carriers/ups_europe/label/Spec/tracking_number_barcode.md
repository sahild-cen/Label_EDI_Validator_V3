# Field: tracking_number_barcode

## Display Name
Tracking Number Barcode (Code 128)

## Field Description
A Code 128 barcode encoding the full 1Z tracking number. This is the primary machine-readable barcode on the UPS shipping label used for package scanning and tracking throughout the UPS network.

## Format & Validation Rules
- **Data Type:** barcode (Code 128)
- **Length:** 18 characters (full 1Z tracking number)
- **Pattern/Regex:** Not applicable (barcode symbology)
- **Allowed Values:** Full 1Z tracking number
- **Required:** yes

## Examples from Spec
- Encodes values like `1Z12345675...` (full 18-character tracking number)

## Position on Label
Bottom barcode area of the label.

## ZPL Rendering
- **Typical Position:** Bottom portion of label, primary barcode area
- **Font / Size:** Minimum barcode height = 1.00 inches
- **Field Prefix:** None — barcode
- **ZPL Command:** ^BC (Code 128)

## Edge Cases & Notes
- Start with subset A, use uppercase for all alpha characters. Shift to subset C after "1Z" if no alpha characters in shipper number or service level indicator. Shift to subset C after the last alpha character when an even number of numeric characters remain.
- Minimum barcode width = 2.84 inches (including quiet zones); Maximum = 4.47 inches.
- Minimum ANSI Grade B print quality required.
- Narrow Width (X) = 18 mil +/- 3 mil (must fall between 15 and 21 mil).
- Minimum quiet zone left and right = 1/4 inch; top and bottom = 1/16 inch.
- Total encoded character count including shifts is 15 characters for the 1Z barcode.

## Claude Confidence
HIGH — spec provides detailed Code 128 specifications, dimensions, and encoding rules

## Review Status
- [ ] Reviewed by human