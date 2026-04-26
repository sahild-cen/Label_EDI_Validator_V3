# Field: shipment_date

## Display Name
Shipment Date

## Field Description
The date the shipment is tendered to DHL or the date the label is created. This date is used for transit time calculations and service level commitments.

## Format & Validation Rules
- **Data Type:** date
- **Length:** 10 characters in DD-MMM-YYYY or similar format
- **Pattern/Regex:** ^\d{2}[-/]\w{3}[-/]\d{4}$ or ^\d{2}[-/]\d{2}[-/]\d{4}$
- **Allowed Values:** Valid calendar dates
- **Required:** yes

## Examples from Spec
No examples in extracted spec text.

## ZPL Rendering
- **Typical Position:** upper portion of label, near shipper info or in header area
- **Font / Size:** Not specified
- **Field Prefix:** "Date:" or "Ship Date:" or similar
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Date format may vary by country of origin. DHL may use DD-MMM-YYYY (e.g., 15-JAN-2024) format in some regions and DD/MM/YYYY in others.

## Claude Confidence
MEDIUM — standard shipping label field

## Review Status
- [ ] Reviewed by human