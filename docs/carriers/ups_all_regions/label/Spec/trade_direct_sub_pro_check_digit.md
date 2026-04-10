# Field: trade_direct_sub_pro_check_digit

## Display Name
Trade Direct Sub Pro Number Check Digit

## Field Description
The 19th digit of the UPS Trade Direct Sub Pro Number, calculated using a Modified MOD-10 algorithm. It serves as a validation mechanism for scanning systems and data entry programs to ensure the Sub Pro number is accurate and complete.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 1 digit (position 19 of the Sub Pro number)
- **Pattern/Regex:** `^[0-9]$`
- **Allowed Values:** 0-9 (if the MOD-10 calculation remainder equals 10, the check digit is 0)
- **Required:** yes — always present as the 19th character of a complete Sub Pro number

## Examples from Spec
- For base Sub Pro `93009123ABC0000001`, the check digit is `2`
- Calculation walkthrough: odd positions sum = 26, even positions sum × 2 = 22, total = 48, next multiple of 10 = 50, check digit = 50 - 48 = 2

## Position on Label
Not specified in spec (embedded as position 19 within the Sub Pro number).

## Edge Cases & Notes
- If the subtraction result equals 10, the check digit defaults to 0 (not 10).
- Alpha characters in the base Sub Pro number must first be converted to their numeric equivalents before the MOD-10 calculation is performed.
- The odd/even position numbering starts from the left (position 1 = odd).

## Claude Confidence
HIGH — spec provides explicit algorithm, full worked example, and edge case handling for remainder of 10.

## Review Status
- [ ] Reviewed by human