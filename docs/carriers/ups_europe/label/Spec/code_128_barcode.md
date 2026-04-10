# Field: code_128_barcode

## Display Name
Code 128 Barcode (Tracking Number Barcode)

## Field Description
A variable-length, continuous, self-checking, alphanumeric barcode used to encode the UPS tracking number. Code 128 uses three subsets (A, B, C), with the tracking number starting in Subset A and switching to Subset C for numeric portions. Each character consists of three bars and three spaces consuming 11 modules.

## Format & Validation Rules
- **Data Type:** barcode (1D Code 128)
- **Length:** Variable — encodes full tracking number
- **Pattern/Regex:** Code 128 symbology specification (AIM USS 128)
- **Allowed Values:** Full ASCII 128 character set; Subset C encodes digit pairs 00-99
- **Required:** yes

## Examples from Spec
No barcode image examples in extracted text.

## Position on Label
Not specified in extracted text — typically in the primary barcode block area of the UPS label.

## ZPL Rendering
- **Typical Position:** Primary barcode block area
- **Font / Size:** Not applicable — barcode element
- **Field Prefix:** None — barcode
- **ZPL Command:** ^BC (Code 128 barcode)

## Edge Cases & Notes
- Must include highlighting bars: one-tenth inch solid black lines located immediately above and below the UPS Barcode block.
- Subset A is used at the beginning of the Tracking Number.
- Subset C is used for adjacent numeric character sequences to produce shorter barcode symbols.
- Human-readable interpretation text must accompany the barcode.
- Bars and spaces may be 1, 2, 3, or 4 modules wide.

## Claude Confidence
HIGH — Code 128 is well-defined in the glossary/definitions section with technical details about subsets and structure.

## Review Status
- [ ] Reviewed by human