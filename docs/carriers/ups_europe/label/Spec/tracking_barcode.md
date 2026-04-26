# Field: tracking_barcode

## Display Name
Tracking Number Barcode (Code 128)

## Group Description
The 1D Code 128 barcode encoding the 18-character UPS tracking number. This barcode is the primary scanning element on the label for package identification and tracking.

## Sub-Fields

### tracking_barcode
- **Data Type:** barcode
- **Length:** 18 characters (fixed)
- **Pattern/Regex:** `^1Z[A-Z0-9]{6}[A-Z0-9]{2}\d{7}\d{1}$`
- **Allowed Values:** 18-character tracking number: positions 1-2 = "1Z" (data identifier), positions 3-8 = UPS account number, positions 9-10 = service indicator, positions 11-17 = reference number, position 18 = check digit
- **Required:** yes
- **Description:** Code 128 barcode encoding the full 18-digit tracking number without spaces. Alpha characters may only appear in the 1Z data identifier, account number, or service indicator fields.
- **Detect By:** barcode_data:^1Z, zpl_command:^BC
- **Position on Label:** Center of label, tracking number barcode block, left-justified
- **ZPL Font:** Not applicable
- **Field Prefix:** None
- **ZPL Command:** ^BC (Code 128)

### tracking_number_data
- **Data Type:** alphanumeric
- **Length:** 18 characters (fixed)
- **Pattern/Regex:** `^1Z[A-Z0-9]{6}[A-Z0-9]{2}\d{7}\d{1}$`
- **Allowed Values:** Structure: 1Z + 6-char account + 2-char service indicator + 7-digit reference number + 1 check digit
- **Required:** yes
- **Description:** The underlying 18-character tracking number data encoded in the barcode. Spaces are not encoded. All alpha characters must be uppercase. The reference number is determined by shipper/shipping system and must be unique for one year.
- **Detect By:** barcode_data:^1Z
- **Position on Label:** Encoded within the tracking barcode
- **ZPL Font:** Not applicable
- **Field Prefix:** None
- **ZPL Command:** ^BC (Code 128)

## Examples from Spec
```
1Z1X2X3XA112345671
```
Breakdown:
```
Data Identifier: 1Z
Account Number: 1X2X3X
Service Indicator: A1
Reference Number: 1234567
Check Digit: 1
```

## Edge Cases & Notes
- Spaces are NOT encoded in the barcode (only in the human-readable interpretation).
- All alpha characters must be uppercase.
- Alpha characters may only appear in the 1Z data identifier, account number, or service indicator fields. The reference number must be numeric.
- The entire 18-digit tracking number must remain unique for one year.
- Barcode height minimum = 0.7 inches, width = variable.
- See Appendix B for Code 128 specifications.

## Claude Confidence
HIGH — spec provides detailed breakdown of all 18 positions, formatting rules, and examples.

## Review Status
- [x] Reviewed by human