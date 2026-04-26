# Field: delivery_time_code

## Display Name
Delivery Time Code

## Field Description
A single numeric digit within the routing barcode indicating the delivery time requirement. Maps to specific time windows such as pre-09:00, pre-10:30, or pre-12:00 delivery.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 1 digit (fixed length)
- **Pattern/Regex:** `\d{1}`
- **Allowed Values:**
  - `0` — No fixed delivery time
  - `1` — Pre 09:00
  - `2` — Pre 12:00
  - `3` — Pre 10:30
- **Required:** yes — mandatory in routing barcode; if no delivery time, must be populated with "0"

## Examples from Spec
- `0` — No fixed time (Germany, Switzerland examples)
- `1` — Time code 1 (Belgium, Netherlands examples)

## ZPL Rendering
- **Typical Position:** Encoded within routing barcode; part of human-readable routing code
- **Font / Size:** Not specified
- **Field Prefix:** None — positional within routing string
- **ZPL Command:** Encoded within routing barcode (^BC)

## Edge Cases & Notes
- Even though delivery time is optional at data capture level, the field is MANDATORY in the barcode and must be "0" if no time is specified.
- The corresponding handling information text (e.g., "X09", "X10", "X12") is printed separately on the label.

## Claude Confidence
HIGH — explicitly defined with enumerated values

## Review Status
- [x] Reviewed by human