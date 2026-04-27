# Field: ups_routing_code_version

## Display Name
UPS Routing Code Version and Date

## Field Description
The version number and effective date of the UPS Routing Code (URC) file used when generating the label, printed in the lower right-hand corner.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 13 characters (for customer format)
- **Pattern/Regex:** `[0-9]{1,2}\.[0-9][A-Z] [0-9]{2}/[0-9]{4}` (customer format)
- **Allowed Values:** Version from URC file header + month/year
- **Required:** yes

## Examples from Spec
- `18.0A 04/2018`
- `18.5A 01/2020`

## Position on Label
Lower right-hand corner of the address label.

## Edge Cases & Notes
- Data Content: Positions 1-5 = UPS Routing Code version (include decimal point), Position 6 = Space, Positions 7-8 = Two-digit month, Position 9 = "/", Positions 10-13 = Four-digit year
- Font Size = 6 pt.
- Version is found in the header of the URC file

## Claude Confidence
HIGH — spec clearly defines format with positional breakdown and examples

## Review Status
- [x] Reviewed by human