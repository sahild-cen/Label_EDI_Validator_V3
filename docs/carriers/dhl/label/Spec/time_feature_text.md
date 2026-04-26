# Field: time_feature_text

## Display Name
Time Feature Handling Information Text

## Field Description
Human-readable text printed on the label indicating the delivery time feature. This corresponds to the delivery time code in the routing barcode and serves as visible handling information for operations.

## Format & Validation Rules
- **Data Type:** string
- **Length:** 3 characters
- **Pattern/Regex:** `X(09|10|12)` or blank
- **Allowed Values:**
  - (none/blank) — No fixed delivery time
  - `X09` — Pre 09:00 delivery
  - `X10` — Pre 10:30 delivery
  - `X12` — Pre 12:00 delivery
- **Required:** conditional — only printed when a time feature is selected

## Examples from Spec
- `X09` for pre-09:00 delivery
- `X10` for pre-10:30 delivery
- `X12` for pre-12:00 delivery

## ZPL Rendering
- **Typical Position:** Handling information area of label
- **Font / Size:** Not specified — likely prominent for operational visibility
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
- Not printed when no fixed delivery time is selected (time code 0).
- This is the visible handling information complement to the barcode time code.

## Claude Confidence
HIGH — explicitly defined in the time feature table

## Review Status
- [ ] Reviewed by human