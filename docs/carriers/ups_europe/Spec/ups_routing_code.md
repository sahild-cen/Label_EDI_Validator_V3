# Field: ups_routing_code

## Display Name
UPS Routing Code (URC)

## Field Description
Identifies the UPS delivery facility for routing purposes. It is one of the five key data elements on a UPS Smart Label. Automated shipping systems derive the URC by comparing the receiver's Postal Code to a table provided by UPS.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 12 positions
- **Pattern/Regex:** Positions 1-3: Two-character state abbreviation preceded by a space OR three-character country abbreviation; Position 4: Space; Positions 5-7: Three-digit building code; Position 8: Space; Position 9: One-digit building code; Position 10: Dash; Positions 11-12: Two-digit inbuilding indicator
- **Allowed Values:** Derived from UPS routing data file
- **Required:** conditional — required when routing code exists in the data table for the destination; leave blank if no routing code exists

## Examples from Spec
- U.S. destination: `GA 301 9-01`
- Non-U.S. destination: `CAN 123 5-27`
- Label samples: `FRA 753 7-00`, `SGP 256 2-00`

## Position on Label
Must print to the right of the MaxiCode™ symbology, beneath the horizontal separating line and above the Postal Barcode. Font size = 24pt.

## Edge Cases & Notes
- If a Routing Code does not exist in the data table for a given destination, leave that area on the label blank.
- The URC data file must be updated monthly to ensure the most accurate routing information.
- The file can be downloaded at: https://www.ups.com/hcic/hcic?loc=en_US

## Claude Confidence
HIGH — spec provides detailed positional format and multiple examples

## Review Status
- [x] Reviewed by human