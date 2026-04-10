# Field: delivery_date_code

## Display Name
Delivery Date Code

## Field Description
A 2-digit numeric code within the routing barcode indicating the delivery date or delivery scheduling option. Represents either a specific day of the month, or a special delivery arrangement code.

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
- **Required:** yes (mandatory in routing barcode; if no date specified, populate with "00")

## Examples from Spec
- `31` — Delivery on the 31st day of the month (EUROPACK example)
- `00` — No fixed date (DOM EUROPACK Germany example)
- `52` — Hold at depot (ECONOMY SELECT Switzerland example)
- `10` — Delivery at 10th of month (EXPRESS WORLDWIDE Netherlands example)

## Position on Label
Within the routing barcode, immediately after the product code. Also appears as human-readable label code (e.g., "01"–"31", "A" for appointment, "S" for Saturday, "H" for hold at depot).

## Edge Cases & Notes
- At the barcode level, this field is mandatory and may NOT remain empty — must be populated with "00" if no valid delivery date is available.
- The human-readable label code differs from the barcode code for some values (e.g., barcode "51" = label "A", barcode "50" = label "S", barcode "52" = label "H").

## Claude Confidence
HIGH — Spec provides clear enumeration of codes and explicit examples.

## Review Status
- [ ] Reviewed by human