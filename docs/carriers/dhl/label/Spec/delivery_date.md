# Field: delivery_date

## Display Name
Delivery Date

## Field Description
Shows the delivery date feature, indicating when the shipment should be delivered. Displayed with a "Day" header (which may be in local language for domestic but must include English for international shipments). The value is encoded in the routing barcode and displayed on the label. A separator "-" between Date and Time fields is required whenever at least one feature is chosen.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 2 characters (or single alpha character for special codes)
- **Pattern/Regex:** `\d{2}` for numeric dates (01–31, 00 for no fixed date), or single alpha (`A`, `S`, `H`, etc.) for special delivery instructions
- **Allowed Values:** "00" = no fixed date; "01"–"31" = day of month; "50" = Saturday only; "51" = Delivery on appointment (label shows "A"); "52" = Hold at depot (label shows "H")
- **Required:** conditional — coded mandatorily in routing barcode (with "00" default); displayed on label only when a delivery date feature is selected

## Examples from Spec
- "00" in routing barcode → no label display
- "01"–"31" → displayed as 2-digit day on label (e.g., "31")
- "51" in routing barcode → "A" on label (delivery on appointment)
- "50" in routing barcode → "S" on label (Saturday only)
- "52" in routing barcode → "H" on label (hold at depot)

## ZPL Rendering
- **Typical Position:** handling information segment, under "Day" header
- **Font / Size:** Not specified explicitly; header "Day" in specified font
- **Field Prefix:** "Day" header text
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
- The "Day" header may be written in local language for domestic shipments, but English "Day" must also appear for international shipments.
- The day of month is represented in 2-digit numeric format with leading zeroes.
- May contain non-numeric values representing delivery instructions that cannot be combined with a certain date.
- Always coded in routing barcode (mandatory at barcode level with "00" if no date specified).

## Claude Confidence
HIGH — detailed specification with clear encoding rules and examples

## Review Status
- [x] Reviewed by human