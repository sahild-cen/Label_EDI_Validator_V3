# Field: delivery_date_label_code

## Display Name
Delivery Date Label Code

## Field Description
The human-readable label representation of the delivery date, printed on the label in the routing/handling information area. This is distinct from the numeric code encoded in the routing barcode — some values have alphabetic label representations.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 1-2 characters
- **Pattern/Regex:** `[0-9ASH]{1,2}`
- **Allowed Values:**
  - (none) — No fixed date delivery
  - `01` to `31` — Fixed day of month
  - `A` — Delivery on appointment
  - `S` — Saturday only delivery
  - `H` — Hold at depot
- **Required:** conditional — printed only when a delivery date feature is selected

## Examples from Spec
- `A` for delivery on appointment (barcode code 51)
- `S` for Saturday only delivery (barcode code 50)
- `H` for hold at depot (barcode code 52)

## ZPL Rendering
- **Typical Position:** Handling information / routing area of label
- **Font / Size:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
- When no fixed date delivery is selected, no label code is printed (blank).
- The label code differs from the barcode code for special delivery types (appointment = "A", Saturday = "S", hold = "H").

## Claude Confidence
MEDIUM — the mapping is shown in the table but the precise label rendering location is not fully described in extracted text

## Review Status
- [x] Reviewed by human