# Field: import_site_information

## Display Name
Import Site Information (SORT TO)

## Field Description
The UPS import site information block used for World Ease shipments, containing the UPS import site port name, country, and postal code. This is the customs clearance location.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Values from the Port of Entry (POE) table provided by UPS Account Executive
- **Required:** yes — for World Ease shipments

## Examples from Spec
- "SORT TO: | UPS / COLOGNE / GERMANY 51147"

## Position on Label
For over-labels: prints to the right of "SORT TO:" title separated by a vertical line. Line 1 = "UPS" (16 pt. bold), Line 2 = Port Name (16 pt. bold), Line 3 = Country Name (14 pt. bold), Line 3 = Postal Code (14 pt. bold). For single labels: positioned to the right of the SHIP TO address just above the Postal Code Line.

## Edge Cases & Notes
All characters must be in bold, uppercase letters. The import site information is sourced from the Port of Entry (POE) table. All labels in a shipment must display the same port of entry in the "Sort To" field. For single labels, the block contains two rows with "UPS WORLD EASE" on top and UPS Routing Code for the import site on bottom.

## Claude Confidence
HIGH — spec provides detailed layout rules and examples

## Review Status
- [ ] Reviewed by human