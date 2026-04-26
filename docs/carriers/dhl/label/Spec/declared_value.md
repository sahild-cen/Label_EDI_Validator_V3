# Field: declared_value

## Display Name
Declared Value / Customs Value

## Field Description
The declared monetary value of the shipment contents for customs and insurance purposes. Required for international non-document shipments and optional insurance declarations.

## Format & Validation Rules
- **Data Type:** numeric with currency
- **Length:** variable
- **Pattern/Regex:** ^\d+(\.\d{2})?$
- **Allowed Values:** Positive numeric values with currency code
- **Required:** conditional — required for international non-document shipments

## Examples from Spec
No examples in extracted spec text.

## ZPL Rendering
- **Typical Position:** customs information area, near description of goods
- **Font / Size:** Not specified
- **Field Prefix:** "Value:" or "Declared Value:" with currency code (e.g., "USD", "EUR")
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Currency should be specified using ISO 4217 3-letter currency codes. The declared value must match the commercial invoice. DHL may impose maximum declared value limits by service and destination. Shipment value affects customs duties and DHL's liability.

## Claude Confidence
MEDIUM — standard international shipping field

## Review Status
- [x] Reviewed by human