# Field: package_in_shipment

## Display Name
Package In Shipment (N/X)

## Field Description
Indicates the package number (N) out of the total number of packages (X) in the shipment, in the format N/X. This is encoded in the MaxiCode secondary message.

## Format & Validation Rules
- **Data Type:** alphanumeric (numeric with "/" separator)
- **Length:** 3-7 characters (n1-3 "/" n1-3)
- **Pattern/Regex:** `^[0-9]{1,3}/[0-9]{1,3}$`
- **Allowed Values:** Package number / total packages (e.g., 1/1, 2/5, 15/100)
- **Required:** yes

## Examples from Spec
- `1/1` (all MaxiCode examples — single-package shipments)

## Position on Label
Encoded within MaxiCode secondary message. May also appear as human-readable text on the label.

## ZPL Rendering
- **Typical Position:** Encoded within MaxiCode
- **Font / Size:** Not specified
- **Field Prefix:** None
- **ZPL Command:** Encoded within ^BD (MaxiCode)

## Edge Cases & Notes
- The "/" character must be encoded to separate the N and X values.
- Both N and X can be 1-3 digits each.

## Claude Confidence
HIGH — spec clearly defines the format with the "/" separator requirement

## Review Status
- [ ] Reviewed by human