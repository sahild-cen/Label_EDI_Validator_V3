# Field: ship_to_address

## Display Name
Ship To Address (Street Address)

## Field Description
The street address of the destination/consignee. Encoded in the MaxiCode secondary message. Can use either a full street address format or a primary/secondary address number format for CASS-certified addresses.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 1-35 characters for full address format; or 1-10 + FS + 1-8 for primary/secondary number format
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Valid street address
- **Required:** yes

## Examples from Spec
- `123<FS>567` (validated address: primary address number 123, secondary 567 for "123 MAIN STREET, SUITE 567")
- `19 SOUTH ST` (non-validated address)
- `5 WALDSTRASSE` (international address, Germany)
- `1 MAIN ST` (letter/envelope example)

## Position on Label
Encoded within MaxiCode secondary message. Also printed as human-readable text in the ship-to address block on the label.

## ZPL Rendering
- **Typical Position:** Ship-to address block, center/middle of label
- **Font / Size:** Not specified
- **Field Prefix:** None (part of address block)
- **ZPL Command:** ^FD (text field) for human-readable; encoded within ^BD (MaxiCode)

## Edge Cases & Notes
- Full address format `(an 1...35)`: provides full street address line 1; may be truncated if it reaches the character limit.
- Primary/secondary format `(an 1...10<FS>an1...8)`: only allowed for CASS-certified addresses in uncompressed MaxiCode when Address Validation = "Y". Uses `<FS>` (decimal 28) to separate primary and secondary address numbers.
- If MaxiCode exceeds maximum length and Shipment ID is already cleared, shorten the Ship-To Address field (delete only the minimum characters needed).

## Claude Confidence
HIGH — spec provides clear format options, multiple examples, and truncation rules

## Review Status
- [ ] Reviewed by human