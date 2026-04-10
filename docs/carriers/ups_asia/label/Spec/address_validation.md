# Field: address_validation

## Display Name
Address Validation (Y or N)

## Field Description
A single-character flag indicating whether the delivery address has been validated against a USPS CASS-certified database. Encoded in the MaxiCode data string.

## Format & Validation Rules
- **Data Type:** alphabetic
- **Length:** 1 (exact)
- **Pattern/Regex:** `[YN]`
- **Allowed Values:** `Y` (validated) or `N` (not validated)
- **Required:** yes

## Examples from Spec
- `Y` (validated address example with primary/secondary address format)
- `N` (non-validated address examples, international examples)

## Position on Label
Encoded within the MaxiCode barcode (secondary message).

## Edge Cases & Notes
- Set to "Y" when the delivery address is compared to a USPS CASS-certified database.
- When set to "Y", the address format `(an 1...10<FS>an1...8)` can be used with primary and secondary address numbers.
- International shipments typically use "N".

## Claude Confidence
HIGH — spec clearly defines the two allowed values and conditions for each.

## Review Status
- [ ] Reviewed by human