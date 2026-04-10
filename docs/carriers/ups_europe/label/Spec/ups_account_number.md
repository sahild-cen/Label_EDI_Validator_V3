# Field: ups_account_number

## Display Name
UPS Account Number

## Field Description
The unique number assigned by UPS to the shipper, contained in positions 3-8 of the Tracking Number. This identifies the billing/shipping account.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 6 characters (positions 3-8 of tracking number)
- **Pattern/Regex:** `[A-Z0-9]{6}`
- **Allowed Values:** Assigned by UPS to each shipper
- **Required:** yes — embedded within tracking number; may also appear separately on label

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in the extracted text. The account number is embedded within the tracking number and may also appear in the shipper information area.

## ZPL Rendering
- **Typical Position:** Embedded in tracking number barcode; may also appear in shipper info block
- **Font / Size:** Not specified
- **Field Prefix:** None when embedded in tracking number
- **ZPL Command:** ^FD (text field) if displayed separately; otherwise part of tracking number barcode data

## Edge Cases & Notes
- The submission form must list all UPS account numbers, but the number of accounts does not affect total label count for certification.
- Multiple account numbers can be included on a submission form if they are for the same customer name and address.

## Claude Confidence
MEDIUM — Defined in glossary as positions 3-8 of tracking number, but standalone label rendering details not in extracted text.

## Review Status
- [ ] Reviewed by human