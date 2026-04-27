# Field: service_icon

## Display Name
Service Icon

## Field Description
A graphical icon consisting of three fixed positions that indicates the class of service, time of day, and day of delivery for the shipment. Appears to the right of the Service Title.

## Format & Validation Rules
- **Data Type:** alphanumeric (3 positions)
- **Length:** 3 positions
- **Pattern/Regex:** Position 1 = [1-3], Position 2 = [+APspace], Position 3 = [Sspace]
- **Allowed Values:** Position 1: 1 (express), 2 (expedited), 3 (ground/3-day); Position 2: + (plus), A (AM), P (PM), space; Position 3: S (Saturday), space. Exceptions: Black 0.35 inch square for UPS GROUND (U.S.) and UPS STANDARD (International); Open circle for Economy (Canada); Blank for UPS Today (Poland)
- **Required:** yes

## Examples from Spec
- `1+` (UPS EXPRESS PLUS)
- `1` (UPS EXPRESS)
- `1 S` (UPS EXPRESS with Saturday Delivery)
- `1P` (UPS SAVER, UPS EXPRESS FREIGHT)
- `2` (UPS EXPEDITED)
- `3` (UPS 3 DAY SELECT)
- `1PS` (Express Freight with Saturday)
- Black Square (UPS STANDARD)

## Position on Label
Beneath the MaxiCode Symbology and Postal Barcode Blocks, to the right of the Service Title and Human-Readable Interpretation. Right justified with the right edge of the Tracking Number Block.

## Edge Cases & Notes
- Each icon position remains fixed
- UPS GROUND and UPS STANDARD use a black 0.35 inch square instead of the standard 3-position icon
- UPS Economy (Canada) uses an open circle
- UPS Today (Poland) is blank

## Claude Confidence
HIGH — spec provides detailed positional breakdown and extensive service-to-icon mapping tables

## Review Status
- [x] Reviewed by human