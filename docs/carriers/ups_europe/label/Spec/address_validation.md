# Field: address_validation

## Display Name
Address Validation (Y or N)

## Field Description
A single character flag indicating whether the ship-to address has been validated against a USPS CASS-certified database for ZIP+4 matching. Set to "Y" for validated addresses, "N" for non-validated.

## Format & Validation Rules
- **Data Type:** alphabetic
- **Length:** 1 character
- **Pattern/Regex:** `^[YN]$`
- **Allowed Values:** "Y" (validated) or "N" (not validated)
- **Required:** yes

## Examples from Spec
- `Y` (validated address example with CASS-certified matching)
- `N` (non-validated, international, and letter/envelope examples)

## Position on Label
Encoded within MaxiCode secondary message only.

## ZPL Rendering
- **Typical Position:** Encoded within MaxiCode
- **Font / Size:** Not applicable
- **Field Prefix:** None
- **ZPL Command:** Encoded within ^BD (MaxiCode)

## Edge Cases & Notes
- When set to "Y", the alternate address format `(an 1...10<FS>an1...8)` with primary and secondary address numbers separated by `<FS>` is allowed in uncompressed MaxiCode.
- The `<FS>` (field separator, decimal 28) is used between primary and secondary address numbers only when Address Validation = "Y".

## Claude Confidence
HIGH — spec clearly defines the field with Y/N values and associated address format rules

## Review Status
- [ ] Reviewed by human