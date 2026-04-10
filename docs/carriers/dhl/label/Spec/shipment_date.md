# Field: shipment_date

## Display Name
Shipment Date (Ship Date)

## Field Description
The date the shipment is tendered to DHL for transportation.

## Format & Validation Rules
- **Data Type:** date
- **Length:** 10 characters (formatted) or 8 digits (YYYYMMDD)
- **Pattern/Regex:** `^\d{2}[A-Z]{3}\d{4}$` or similar date format
- **Allowed Values:** Valid dates
- **Required:** yes

## Examples from Spec
No examples in spec.

## Position on Label
Typically in the shipment details area of the label.

## Edge Cases & Notes
DHL commonly uses the format DD-MMM-YYYY (e.g., 15-JAN-2024) or similar. The shipment date affects transit time calculations and service commitments.

## Claude Confidence
HIGH — Standard element on all DHL labels.

## Review Status
- [ ] Reviewed by human