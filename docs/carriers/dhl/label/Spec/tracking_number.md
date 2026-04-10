# Field: tracking_number

## Display Name
Tracking Number (Waybill Number / AWB Number)

## Field Description
The primary shipment tracking identifier assigned by DHL. This is the unique identifier used to track the package through the DHL network from origin to destination.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 10-11 digits
- **Pattern/Regex:** `^\d{10,11}$`
- **Allowed Values:** Not restricted (system-generated)
- **Required:** yes

## Examples from Spec
No examples in spec.

## Position on Label
Typically appears in the upper portion of the label, both as human-readable text and as a barcode.

## Edge Cases & Notes
DHL waybill numbers include a check digit. The tracking number is also encoded in the primary 1D barcode on the label. For DHL Express, the tracking number is typically 10 digits. For DHL eCommerce/Parcel, formats may vary.

## Claude Confidence
HIGH — DHL tracking numbers are well-documented across DHL integration guides and are the primary identifier on every DHL label.

## Review Status
- [ ] Reviewed by human