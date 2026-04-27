# Field: tracking_barcode

## Display Name
Tracking Number Barcode (Code 128)

## Field Description
A 1D barcode encoding the UPS Tracking Number using Code 128 symbology. Code 128 is a variable length, continuous, self-checking, alphanumeric barcode using subsets A and C.

## Format & Validation Rules
- **Data Type:** barcode (1D Code 128)
- **Length:** variable — encodes full tracking number
- **Pattern/Regex:** Code 128 encoding; Subset A used at beginning for alphanumeric data, Subset C used for numeric pairs (00-99)
- **Allowed Values:** Full ASCII 128 character set capability; each character consists of 3 bars and 3 spaces consuming 11 modules
- **Required:** yes

## Examples from Spec
No examples in spec.

## Position on Label
Within the UPS Barcode block, bounded by highlighting bars.

## Edge Cases & Notes
- Code 128 has three subsets (A, B, C); Subset A is used at the beginning of the Tracking Number, and Subset C is used for adjacent numeric character pairs.
- Highlighting bars (one-tenth inch solid black lines) are located immediately above and below the UPS Barcode block.
- Human-readable interpretation of the barcode data must accompany the barcode.

## Claude Confidence
HIGH — Definitions section provides detailed Code 128 and subset descriptions.

## Review Status
- [x] Reviewed by human