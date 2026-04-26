# Field: urc_version_number

## Display Name
URC Version Number

## Group Description
The version number of the UPS Routing Code data file, printed on the label to indicate which version of the routing table was used.

## Sub-Fields

### urc_version_number
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** `r'.+ \d{2}/\d{4}$'`
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Version identifier for the UPS routing code data file used when generating the label
- **Detect By:** spatial:bottom_right, pattern matching version format (e.g., "18.5A 01/2020")
- **Position on Label:** bottom area, near tracking barcode block
- **ZPL Font:** 6pt
- **Field Prefix:** " "
- **ZPL Command:** ^FD (text field)

## Examples from Spec
- ` 18.5A 01/2020`

## Edge Cases & Notes
- Appears consistently across all label examples in the spec
- Very small font size (6pt)
- Format appears to be version number + letter designation + month/year

## Claude Confidence
MEDIUM — spec shows this field on label diagrams with font size but does not provide detailed format description

## Review Status
- [x] Reviewed by human