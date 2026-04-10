# Field: shipment_id_number

## Display Name
Shipment ID Number

## Field Description
An optional identifier for the shipment, encoded in the MaxiCode data string. When not provided, a placeholder (GS separator) must still be included.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 1-30 (variable)
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** no (optional)

## Examples from Spec
- All MaxiCode examples show this field as blank with a `<GS>` placeholder.

## Position on Label
Encoded within the MaxiCode barcode (secondary message).

## Edge Cases & Notes
- When left blank, the `<GS>` separator must still be provided as a placeholder.

## Claude Confidence
HIGH — spec explicitly marks as optional with 1-30 character length and shows blank placeholders in examples.

## Review Status
- [ ] Reviewed by human