# Field: shipment_id_number

## Display Name
Shipment ID Number

## Field Description
An optional identifier for the shipment, encoded in the MaxiCode secondary message. When not provided, a placeholder (empty field with GS delimiter) must still be included in the data string.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 1-30 characters (variable)
- **Pattern/Regex:** `^[A-Z0-9]{1,30}$` (if provided)
- **Allowed Values:** Not restricted
- **Required:** no (optional)

## Examples from Spec
- Empty/blank in all provided MaxiCode examples (placeholder `<GS>` used)

## Position on Label
Encoded within MaxiCode secondary message.

## ZPL Rendering
- **Typical Position:** Encoded within MaxiCode
- **Font / Size:** Not applicable
- **Field Prefix:** None
- **ZPL Command:** Encoded within ^BD (MaxiCode)

## Edge Cases & Notes
- Even when blank, the `<GS>` group separator must be included as a placeholder to separate this field from the package count field.
- If the MaxiCode data string exceeds maximum length, the Shipment ID Number should be completely cleared first (saves approximately 11 characters).

## Claude Confidence
HIGH — spec clearly defines the field as optional with placeholder requirement

## Review Status
- [ ] Reviewed by human