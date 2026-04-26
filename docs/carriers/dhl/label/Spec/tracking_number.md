# Field: tracking_number

## Display Name
Tracking Number (Waybill Number / AWB Number)

## Field Description
The primary DHL shipment tracking number, also known as the Air Waybill (AWB) number. This is the unique identifier for the shipment within DHL's global network. It appears both as human-readable text and as a barcode on the label.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 10-11 digits for DHL Express AWB; may vary by service
- **Pattern/Regex:** ^\d{10,11}$
- **Allowed Values:** DHL-assigned numeric range; typically starts with specific prefixes by region
- **Required:** yes

## Examples from Spec
No examples in extracted spec text.

## ZPL Rendering
- **Typical Position:** prominent position, often center or bottom of label with associated barcode
- **Font / Size:** Large, bold font for human-readable portion
- **Field Prefix:** None — appears as both text and barcode
- **ZPL Command:** ^BC (Code 128) for the barcode rendering; ^FD for human-readable text

## Edge Cases & Notes
DHL Express uses a 10-digit waybill number. DHL eCommerce and DHL Parcel may use different tracking number formats and lengths. The tracking number barcode is typically Code 128 or Interleaved 2 of 5. For multi-piece shipments, each piece gets a unique tracking number derived from the master AWB.

## Claude Confidence
MEDIUM — core DHL field but minimal extracted spec detail

## Review Status
- [ ] Reviewed by human