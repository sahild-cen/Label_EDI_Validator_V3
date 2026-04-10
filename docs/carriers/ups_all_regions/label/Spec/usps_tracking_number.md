# Field: usps_tracking_number

## Display Name
USPS Tracking Number (eVS)

## Field Description
The USPS tracking number used for the final-mile delivery portion of UPS SurePost shipments. This is a USPS eVS (Electronic Verification System) barcode/number.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 34 digits (displayed with spaces in groups of 4)
- **Pattern/Regex:** `9[0-9]{33}` (starts with 9)
- **Allowed Values:** USPS eVS tracking number format
- **Required:** conditional — Required for UPS SurePost shipments

## Examples from Spec
- `9274 8123 4567 8958 1000 0000 18`

## Position on Label
Printed in the USPS delivery section at the bottom of SurePost labels with the label "USPS TRACKING # eVS".

## Edge Cases & Notes
This appears on UPS SurePost labels only, which combine UPS Ground pickup/linehaul with USPS final delivery. The label also shows "Return Service Requested", "U.S. POSTAGE PAID", and "USPS DELIVER TO:" sections.

## Claude Confidence
HIGH — Clear example shown on SurePost label sample.

## Review Status
- [ ] Reviewed by human