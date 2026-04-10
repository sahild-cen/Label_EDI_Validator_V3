# Field: tracking_number_barcode

## Display Name
Tracking Number Barcode (Code 128)

## Field Description
A Code 128 barcode encoding the full 1Z tracking number. This is the primary machine-readable barcode on the shipping label used for package tracking and sortation.

## Format & Validation Rules
- **Data Type:** barcode (Code 128)
- **Length:** 18 characters encoded (full 1Z tracking number)
- **Pattern/Regex:** Starts with subset A for "1Z", shifts to subset C for numeric compression
- **Allowed Values:** Full 1Z tracking number
- **Required:** yes

## Examples from Spec
- Barcode encoding `1Z12345675` shown in MaxiCode printer command examples
- Diagram showing 15 total characters after subset shifting (1Z in subset A, pairs of digits in subset C)

## Position on Label
Not explicitly stated in extracted text, but shown on label examples in the lower portion of the label.

## Edge Cases & Notes
- Start with subset A and use uppercase for all alpha characters.
- Shift to subset C after "1Z" if no alpha characters in shipper number or service level indicator.
- Shift to subset C after the last occurrence of an alpha character and an even number of numeric characters remain (e.g., Start A 1Z 123 4X5 Shift C 01 1234 5679).
- Minimum barcode width = 2.84 inches (2.34 inches + 0.50 inches quiet zones).
- Maximum barcode width = 4.47 inches (3.97 inches + 0.50 inches quiet zones).
- Minimum barcode height = 0.7 inches.
- Minimum ANSI Grade B print quality required.

## Claude Confidence
HIGH — spec provides detailed Code 128 symbology requirements, dimensional tolerances, and subset shifting rules.

## Review Status
- [ ] Reviewed by human