# Field: trade_direct_sub_pro_number

## Display Name
Trade Direct Sub Pro Number

## Field Description
A 19-character identifier used for UPS Trade Direct™ Service shipments. The Sub Pro number includes an 18-character base number plus a Mod-10 check digit as the 19th digit, used by scanning systems and data entry programs to ensure the captured number is accurate and complete.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 19 characters (18-character base + 1 check digit)
- **Pattern/Regex:** `^[0-9A-Z]{18}[0-9]$` (alphanumeric base with numeric check digit)
- **Allowed Values:** Alpha characters A-Z and digits 0-9 in the first 18 positions; digit 0-9 in position 19 (check digit)
- **Required:** conditional — required for UPS Trade Direct™ Service shipments

## Examples from Spec
- Sub Pro number without check digit: `93009123ABC0000001`
- Resulting Sub Pro number with check digit: `93009123ABC00000012`

## Position on Label
Not specified in spec.

## Edge Cases & Notes
- The 19th digit is a Modified MOD-10 check digit calculated as follows:
  1. Convert all alpha characters to numeric equivalents using the specified conversion table.
  2. From left, add all odd-position digits.
  3. From left, add all even-position digits and multiply the sum by two.
  4. Add the results of steps 2 and 3.
  5. Subtract the result from the next highest multiple of 10.
  6. The remainder is the check digit. If the remainder is 10, the check digit is 0.
- Alpha to Numeric Conversion Table:
  - A=2, B=3, C=4, D=5, E=6, F=7, G=8, H=9, I=0, J=1
  - K=2, L=3, M=4, N=5, O=6, P=7, Q=8, R=9, S=0, T=1
  - U=2, V=3, W=4, X=5, Y=6, Z=7
- Note: The spec references steps "3 and 4" in step 4 but contextually means steps 2 and 3 (odd-position sum and doubled even-position sum).
- The conversion table follows a repeating cycle pattern (2-9, 0-1) across the alphabet.

## Claude Confidence
HIGH — spec provides explicit calculation algorithm, conversion table, and a worked example with the resulting 19-character Sub Pro number.

## Review Status
- [ ] Reviewed by human