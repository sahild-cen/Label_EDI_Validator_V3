# Field: delivery_date_code

## Display Name
Delivery Date Code

## Field Description
A 2-digit numeric code within the routing barcode indicating the delivery date requirement. Specifies either a fixed day of the month (01–31), a special delivery arrangement code, or "00" for no fixed date delivery.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 2 digits (fixed length)
- **Pattern/Regex:** `\d{2}`
- **Allowed Values:** 
  - `00` — No fixed date delivery
  - `01` to `31` — Fixed day delivery (day of the month)
  - `50` — Saturday only delivery
  - `51` — Delivery on appointment
  - `52` — Hold at depot (no delivery)
- **Required:** yes — mandatory in routing barcode; if no date specified, must be populated with "00"

## Examples from Spec
- `00` — No fixed date (DOM EUROPACK Germany example)
- `31` — 31st of month (EUROPACK Belgium example)
- `10` — 10th of month (EXPRESS WORLDWIDE Netherlands example)
- `52` — Hold at depot (ECONOMY SELECT Switzerland example)

## ZPL Rendering
- **Typical Position:** Encoded within routing barcode; part of human-readable routing code
- **Font / Size:** Not specified
- **Field Prefix:** None — positional within routing string
- **ZPL Command:** Encoded within routing barcode (^BC)

## Edge Cases & Notes
- Even though the delivery date is optional at data capture level, the field is MANDATORY in the barcode and must be populated with "00" if no valid delivery date is available.
- Label codes differ from barcode codes for some values (e.g., code 51 in barcode = "A" on label, code 50 = "S", code 52 = "H").

## Claude Confidence
HIGH — explicitly defined with enumerated values and barcode/label code mappings

## Review Status
- [x] Reviewed by human