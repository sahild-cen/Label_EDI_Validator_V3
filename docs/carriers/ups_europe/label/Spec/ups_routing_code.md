# Field: ups_routing_code

## Display Name
UPS Routing Code (URC)

## Group Description
Identifies the UPS delivery facility. The URC is derived by comparing the receiver's postal code to a data table provided by UPS. It prints to the right of the MaxiCode symbology, beneath the horizontal separating line and above the postal barcode.

## Sub-Fields

### routing_code
- **Data Type:** alphanumeric
- **Length:** 12 (positions 1-12)
- **Pattern/Regex:** `^[A-Z ]{3}\s\d{3}\s\d-\d{2}$`
- **Allowed Values:** Not restricted — derived from UPS routing data table
- **Required:** yes
- **Description:** UPS Routing Code identifying the delivery facility. Positions 1-3 = two-character state abbreviation preceded by a space or three-character country abbreviation; Position 4 = space; Positions 5-7 = three-digit building code; Position 8 = space; Position 9 = one-digit building code; Position 10 = dash; Positions 11-12 = two-digit inbuilding indicator.
- **Detect By:** spatial:middle_right, pattern matching state/country abbreviation + building codes
- **Position on Label:** right of MaxiCode, beneath horizontal line, above postal barcode
- **ZPL Font:** 24pt
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Examples from Spec
- `GA  301 9-01` (U.S. destination)
- `CAN 123 5-27` (Non-U.S. destination)
- `FRA 753 7-00`
- `SGP 256 2-00`

## Edge Cases & Notes
- URC data file must be updated monthly from https://www.ups.com/hcic/hcic?loc=en_US
- If a routing code does not exist in the data table for a given destination, leave that area blank
- Automated shipping systems derive the URC by comparing receiver's postal code to a UPS-provided table
- For U.S. destinations: 2-character state abbreviation preceded by a space (e.g., " GA")
- For non-U.S. destinations: 3-character country abbreviation (e.g., "CAN", "FRA")

## Claude Confidence
HIGH — spec provides detailed positional format, examples, and data source instructions

## Review Status
- [x] Reviewed by human