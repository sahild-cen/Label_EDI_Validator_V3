# Field: delivery_time

## Display Name
Delivery Time

## Field Description
Shows the delivery time window code, indicating the time constraint for delivery. Displayed with a "Time" header and encoded in the routing barcode. If a time window is chosen, the corresponding code is shown on the label.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 1 digit in routing barcode; variable text on label (e.g., "X09", "X10", "X12")
- **Pattern/Regex:** Routing barcode: `\d{1}`; Label text: `X\d{2}` or similar
- **Allowed Values:** "0" = no fixed delivery time (no label display); "1" = Pre 09:00 → "X09"; "3" = Pre 10:30 → "X10"; "2" = Pre 12:00 → "X12"
- **Required:** conditional — coded mandatorily in routing barcode (with "0" default); displayed on label only when a time feature is selected

## Examples from Spec
- "0" in routing barcode → no label display
- "1" → "X09" on label
- "3" → "X10" on label
- "2" → "X12" on label

## ZPL Rendering
- **Typical Position:** handling information segment, under "Time" header, adjacent to delivery date
- **Font / Size:** Not specified explicitly
- **Field Prefix:** "Time" header text
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
- The "Time" header may be in local language for domestic shipments but must include English for international.
- A "-" separator between Date and Time fields is required whenever at least one of both features is chosen.
- Always coded in routing barcode with "0" if no delivery time specified.

## Claude Confidence
HIGH — clearly specified with code-to-display mapping

## Review Status
- [x] Reviewed by human