# Field: consolidated_movement_shipment_id

## Display Name
Consolidated Movement Shipment ID Number (CM SHIPMENT ID#)

## Field Description
The Consolidated Movement (CM) Shipment ID number for UPS Trade Direct shipments. This uniquely identifies the consolidated movement.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 10 characters (9 numeric + 1 check digit)
- **Pattern/Regex:** `[0-9]{9}[0-9T]`
- **Allowed Values:** Check digit can be numeric or the letter "T"
- **Required:** yes — for Trade Direct labels

## Examples from Spec
- "CM SHIPMENT ID#: 840000028T"

## Position on Label
For small package labels: in the Additional Routing Instructions Block immediately below the Billing Options line. For LTL/TL: below the Ship To address separated by a horizontal line. For Package Pallet: immediately below Ship To address. Font Size = 10 pt. Data content: positions 1-16 = "CM SHIPMENT ID#:", position 17 = space, positions 18-26 = 9 numeric, position 27 = check digit.

## Edge Cases & Notes
Check digit can be numeric or the letter "T". See Appendix A for the Check Digit Calculation example. The terms Consolidated Movement Number (CM) and Unique Shipment Identifier (USI) are synonymous. Also appears as a barcode (Shipment ID Barcode).

## Claude Confidence
HIGH — spec provides explicit format, positional data, check digit rules, and examples

## Review Status
- [ ] Reviewed by human