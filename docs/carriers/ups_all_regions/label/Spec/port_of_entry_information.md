# Field: port_of_entry_information

## Display Name
Port of Entry Information

## Field Description
Contains the UPS import site port name, country name, and postal code sourced from the Port of Entry (POE) table. Used for World Ease single labels.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Values from Port of Entry (POE) table
- **Required:** yes — for World Ease shipments

## Examples from Spec
- First Block: "SORT TO:"
- Second Block: Port Name / Country Name Postal Code (e.g., "COLOGNE / GERMANY 51147")

## Position on Label
For single labels: three blocks — First: "SORT TO:", Second: Port Name and Country Name Postal Code, Third: UPS Routing Code. Font Size = 10 pt. (port info), 16 pt. bold (routing code).

## Edge Cases & Notes
Contact UPS Account Executive for POE tables. All characters must be uppercase. All labels in a shipment must display the same port of entry.

## Claude Confidence
HIGH — spec provides detailed block structure and examples

## Review Status
- [ ] Reviewed by human