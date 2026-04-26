# Field: description_of_goods

## Display Name
Description of Goods (Contents)

## Field Description
A text description of the shipment contents. Required for international shipments for customs clearance purposes. May also appear on domestic shipments for certain DHL services.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable, up to 70-90 characters
- **Pattern/Regex:** .{1,90}
- **Allowed Values:** Not restricted — must accurately describe contents
- **Required:** conditional — required for international/non-document shipments

## Examples from Spec
No examples in extracted spec text.

## ZPL Rendering
- **Typical Position:** mid to lower section of label, customs information area
- **Font / Size:** Not specified
- **Field Prefix:** "Contents:" or "Description:" or similar
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
For DHL Express international shipments, an accurate goods description is legally required for customs processing. Generic descriptions like "goods" or "samples" may cause customs delays. This field should match the commercial invoice description.

## Claude Confidence
MEDIUM — standard international shipping field

## Review Status
- [x] Reviewed by human