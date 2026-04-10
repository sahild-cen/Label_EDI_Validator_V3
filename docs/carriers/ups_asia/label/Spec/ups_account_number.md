# Field: ups_account_number

## Display Name
UPS Account Number

## Field Description
The 6-character UPS shipper account number, used to identify the billing account for the shipment. Appears on the label, in the MaxiCode data string, and on the manifest summary.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 6
- **Pattern/Regex:** `[A-Z0-9]{6}`
- **Allowed Values:** Not restricted (valid UPS account numbers)
- **Required:** yes

## Examples from Spec
- `1X2X3X` (used throughout MaxiCode examples and manifest summary)
- Account number `9373309024` shown on manifest summary (appears to be a longer format for the manifest)

## Position on Label
Encoded within the MaxiCode barcode. Also displayed on the manifest summary. Part of the 1Z tracking number structure (characters 3-8).

## Edge Cases & Notes
- The account number is also the first 6 characters of the 11-digit shipment number.
- In the MaxiCode data string, it is a separate field from the tracking number.

## Claude Confidence
HIGH — spec clearly defines as alphanumeric 6-character field with examples.

## Review Status
- [ ] Reviewed by human