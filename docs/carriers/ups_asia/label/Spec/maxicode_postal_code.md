# Field: maxicode_postal_code

## Display Name
MaxiCode Postal Code Field

## Field Description
The postal code as encoded within the MaxiCode data string. For U.S. destinations (Mode 2), this is a numeric field of 5 or 9 characters. For non-U.S. destinations (Mode 3), this is an alphanumeric field of up to 6 characters.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** Mode 2 (U.S.): 5 or 9 numeric characters; Mode 3 (non-U.S.): up to 6 alphanumeric characters (truncate if longer)
- **Pattern/Regex:** Mode 2: `^\d{5}(\d{4})?$`; Mode 3: `^[A-Za-z0-9]{1,6}$`
- **Allowed Values:** Valid postal codes with spaces and special characters removed
- **Required:** yes — within MaxiCode data string

## Examples from Spec
**Mode 2 (U.S.):**
- 84170-6672 → `841706672`
- 28501 → `28501`

**Mode 3 (non-U.S.):**
- A41460 → `A41460`
- TW137DY → `TW137D` (truncated to 6)
- W1T 1JY → `W1T1JY` (spaces removed)

## Position on Label
Encoded within the MaxiCode symbol; not separately displayed.

## Edge Cases & Notes
- Remove ALL spaces and special characters (including hyphens) from postal codes before encoding.
- For non-U.S. postal codes longer than 6 characters, truncate characters beyond the 6th position.
- For U.S. ZIP+4 codes, remove the hyphen (e.g., 84170-6672 becomes 841706672).
- The `<GS>96` prefix appears before the postal code in the MaxiCode data string for U.S. destinations.

## Claude Confidence
HIGH — Multiple detailed examples and explicit rules provided.

## Review Status
- [ ] Reviewed by human