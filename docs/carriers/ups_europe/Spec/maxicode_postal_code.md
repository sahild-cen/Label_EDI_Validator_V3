# Field: maxicode_postal_code

## Display Name
MaxiCode Postal Code Field

## Field Description
The postal code as encoded within the MaxiCode data string. For U.S. destinations (Mode 2), this is a 5 or 9 digit numeric field. For non-U.S. destinations (Mode 3), this is an alphanumeric field up to 6 characters.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** Mode 2: 5 or 9 digits; Mode 3: up to 6 characters (truncate if longer)
- **Pattern/Regex:** Mode 2: `[0-9]{5,9}`; Mode 3: `[A-Za-z0-9]{1,6}`
- **Allowed Values:** Must not contain spaces or special characters
- **Required:** yes

## Examples from Spec
**Mode 2 (U.S.):**
- 84170-6672 → `841706672` (9 digits, hyphen removed)
- 28501 → `28501` (5 digits)

**Mode 3 (Non-U.S.):**
- "A41460" → "A41460" (6 characters, fits exactly)
- "TW137DY" → "TW137D" (truncated to 6 characters)
- "W1T 1JY" → "W1T1JY" (space removed)

## Position on Label
Encoded within the MaxiCode 2D barcode data string.

## Edge Cases & Notes
- ALL spaces must be removed from postal codes before MaxiCode encoding.
- ALL special characters (hyphens, etc.) must be removed.
- For non-U.S. destinations, if postal code exceeds 6 characters, truncate to 6.
- For Mode 2, the data string format is `<GS>96[postal_code]<GS>`.
- Compressed MaxiCode data string format is not covered in this guide.

## Claude Confidence
HIGH — Spec provides detailed encoding rules and multiple examples for both modes.

## Review Status
- [x] Reviewed by human