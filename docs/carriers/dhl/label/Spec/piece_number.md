# Field: piece_number

## Display Name
Piece Number (Piece Sequence)

## Field Description
The sequential number identifying this specific piece within a multi-piece shipment.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 1-4 digits
- **Pattern/Regex:** `^\d{1,4}$`
- **Allowed Values:** Positive integers from 1 to total piece count
- **Required:** yes (for multi-piece shipments)

## Examples from Spec
No examples in spec.

## Position on Label
Displayed alongside piece count, typically as "X of Y" format.

## Edge Cases & Notes
For single-piece shipments, this is "1 of 1". For multi-piece shipments, each piece label has a unique sequence number.

## Claude Confidence
HIGH — Standard element on all DHL labels.

## Review Status
- [ ] Reviewed by human