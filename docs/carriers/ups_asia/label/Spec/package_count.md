# Field: package_count

## Display Name
Package in Shipment N/X (Package Count)

## Field Description
Indicates which package this is within the shipment (package N of X total packages), encoded in the MaxiCode data string and displayed as human-readable text on the label.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 3-7 characters (n 1…3 / n 1…3 with "/" separator)
- **Pattern/Regex:** `\d{1,3}/\d{1,3}`
- **Allowed Values:** N must be ≤ X; "/" character required as separator
- **Required:** yes

## Examples from Spec
- `1/1` (single package shipment, all MaxiCode examples)
- `1 OF 1` (human-readable format shown on label example: "1 OF 1")

## Position on Label
Encoded in the MaxiCode barcode. Human-readable version ("1 OF 1") displayed on label near the tracking number area.

## Edge Cases & Notes
- The "/" character must be encoded to separate N/X in the MaxiCode data string.
- For UPS Worldwide Express Freight, "pallets" and "packages" are used interchangeably.
- Label shows "1 OF 1" format for human-readable text, while MaxiCode uses "1/1" format.

## Claude Confidence
HIGH — spec clearly defines format with "/" separator requirement and provides examples.

## Review Status
- [ ] Reviewed by human