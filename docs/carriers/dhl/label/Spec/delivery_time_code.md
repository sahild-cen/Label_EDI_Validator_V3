# Field: delivery_time_code

## Display Name
Delivery Time Code

## Field Description
A single-digit numeric code within the routing barcode indicating the delivery time feature for the shipment.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 1 digit (fixed length)
- **Pattern/Regex:** `\d{1}`
- **Allowed Values:**
  - `0` — No fixed delivery time
  - `1` — Pre 09:00 (handling info: "X09")
  - `2` — Pre 12:00 (handling info: "X12")
  - `3` — Pre 10:30 (handling info: "X10")
- **Required:** yes (mandatory in routing barcode; if no delivery time, populate with "0")

## Examples from Spec
- `1` — Time code 1 / Pre 09:00 (EUROPACK Belgium example, also Netherlands example)
- `0` — No fixed time (DOM EUROPACK Germany example, ECONOMY SELECT Switzerland example)

## Position on Label
Within the routing barcode, immediately after the delivery date code. Human-readable handling information shows "X09", "X10", or "X12" as applicable.

## Edge Cases & Notes
- Must always be populated with at least "0" if no delivery time is specified.
- The handling information text ("X09", "X10", "X12") appears separately on the label in the handling information area.

## Claude Confidence
HIGH — Spec provides clear enumeration and examples.

## Review Status
- [ ] Reviewed by human