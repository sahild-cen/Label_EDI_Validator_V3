# Field: maxicode

## Display Name
MaxiCode (2D Barcode)

## Field Description
A 2D barcode symbology used on UPS labels to encode shipment data including postal code, country code, and service class information. Uses Mode 2 for U.S. destinations and Mode 3 for non-U.S. destinations.

## Format & Validation Rules
- **Data Type:** barcode (2D MaxiCode)
- **Length:** variable — data string length depends on mode and content
- **Pattern/Regex:** Compressed or uncompressed data string format; postal code field varies by mode
- **Allowed Values:** Mode 2 for U.S. destinations, Mode 3 for non-U.S. destinations
- **Required:** yes

## Examples from Spec
**Uncompressed Mode 2 (U.S. Destinations):**
- Postal Code: 84170-6672 → `<GS>96841706672<GS>` (9 digits, no hyphens)
- Postal Code: 28501 → `<GS>9628501<GS>` (5 digits)

**Uncompressed Mode 3 (Non-U.S. Destinations):**
- Postal Code "A41460" → Postal Code field: "A41460" (6 characters)
- Postal Code "TW137DY" → Truncated to "TW137D" (max 6 characters)
- Postal Code "W1T 1JY" → Spaces removed: "W1T1JY"

## Position on Label
Not specified in this extract.

## Edge Cases & Notes
- Postal code should NOT contain any spaces or special characters in the MaxiCode data string.
- For non-U.S. destinations: if postal code exceeds 6 characters, TRUNCATE any character over 6.
- For non-U.S. destinations: if postal code is shorter than 6 characters, padding may apply.
- Spaces within postal codes must be removed before encoding.
- Some label creation software providers and printer manufacturers have interpreted Mode 2 for U.S. destinations and Mode 3 for non-U.S. destinations exclusively.
- Compressed MaxiCode data string formats (Mode 2 and Mode 3) are not covered in this guide.

## Claude Confidence
HIGH — Definitions section provides detailed encoding rules and examples for both modes.

## Review Status
- [x] Reviewed by human