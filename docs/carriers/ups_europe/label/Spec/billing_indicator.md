# Field: billing_indicator

## Display Name
Billing Indicator

## Field Description
Indicates the billing method for the shipment (e.g., prepaid, collect, third party).

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** "P/P" (Prepaid) shown in examples; other values likely include collect and third-party billing codes
- **Required:** yes

## Examples from Spec
- `BILLING: P/P`

## Position on Label
Located in the lower portion of the Carrier Segment, below the tracking number barcode.

## ZPL Rendering
- **Typical Position:** Below tracking number barcode area
- **Font / Size:** 10pt
- **Field Prefix:** "BILLING:"
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
- "P/P" appears to indicate Prepaid billing.
- Full list of billing indicator values not enumerated in extracted spec text.

## Claude Confidence
MEDIUM — spec shows examples but does not enumerate all allowed values

## Review Status
- [ ] Reviewed by human