# Field: ups_routing_code

## Display Name
UPS Routing Code (URC)

## Field Description
Identifies the UPS delivery facility for the destination. It is one of the five key data elements on the UPS Smart Label. Automated shipping systems derive the URC by comparing the receiver's Postal Code to a table provided by UPS.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 12 positions
- **Pattern/Regex:** Positions 1-3 = two-character state abbreviation preceded by a space OR three-character country abbreviation; Position 4 = space; Positions 5-7 = three-digit building code; Position 8 = space; Position 9 = one-digit building code; Position 10 = dash; Positions 11-12 = two-digit inbuilding indicator
- **Allowed Values:** Derived from UPS routing data file
- **Required:** yes (leave blank if routing code does not exist in data table for given destination)

## Examples from Spec
- U.S. destination: `GA 301 9-01` (positions: space-G-A-space-3-0-1-space-9-dash-0-1)
- Non-U.S. destination: `CAN 123 5-27`
- `FRA 753 7-00`
- `SGP 256 2-00`

## Position on Label
Must print to the right of the MaxiCode™ symbology, beneath the horizontal separating line and above the Postal Barcode.

## ZPL Rendering
- **Typical Position:** Middle of carrier segment, right of MaxiCode, above postal barcode
- **Font / Size:** 24pt (as specified in spec)
- **Field Prefix:** None — displayed as data only
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
- If a Routing Code does not exist in the data table for a given destination, leave that area on the label blank.
- The URC data file must be updated monthly to ensure the most accurate routing information.
- Data file downloadable at: https://www.ups.com/hcic/hcic?loc=en_US
- For non-U.S. destinations, positions 1-3 use a three-character country abbreviation (e.g., CAN, FRA, SGP).

## Claude Confidence
HIGH — spec provides detailed position-by-position data content, examples, and clear placement rules

## Review Status
- [ ] Reviewed by human