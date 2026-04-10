# Field: ups_routing_code

## Display Name
UPS Routing Code (URC)

## Field Description
The UPS Routing Code used for package sorting and routing. It is derived from the URC data file which must be updated monthly.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 12 positions
- **Pattern/Regex:** For U.S. destinations: `^\s[A-Z]{2}\s\d{3}\s\d-\d{2}$` (space + 2-char state + space + 3-digit building code + space + 1-digit building code + dash + 2-digit inbuilding indicator). For Non-U.S. destinations: `^[A-Z]{3}\s\d{3}\s\d-\s?\d{2}$` (3-char country abbreviation + space + 3-digit building code + space + 1-digit building code + dash + 2-digit inbuilding indicator)
- **Allowed Values:** Not restricted, derived from URC data file
- **Required:** conditional — if a Routing Code does not exist in the data table for a given destination, leave that area blank

## Examples from Spec
U.S.: `GA  301 9-01` (space + GA + space + 301 + space + 9 + dash + 01)
Non-U.S.: `CHN 132 3-00`, `FRA 753 7-00`, `DEU 063 9-39`, `JPN 106 1-00`

## Position on Label
To the right of the MaxiCode symbology, beneath the horizontal separating line and above the Postal Barcode. Font Size = 24 pt.

## Edge Cases & Notes
- Positions 1-3: Two-character state abbreviation preceded by a space (U.S.) OR three-character country abbreviation (Non-U.S.)
- Position 4: Space
- Positions 5-7: Three-digit building code
- Position 8: Space
- Position 9: One-digit building code
- Position 10: Dash
- Positions 11-12: Two-digit inbuilding indicator
- URC data file must be updated monthly from https://www.ups.com/hcic/hcic?loc=en_US
- If no routing code exists for a destination, the area is left blank on the label.

## Claude Confidence
HIGH — spec clearly defines format with positional breakdown and multiple examples

## Review Status
- [ ] Reviewed by human