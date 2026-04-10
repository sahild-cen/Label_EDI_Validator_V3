# Field: routing_code

## Display Name
Routing Code

## Field Description
The UPS postal routing code that directs the package through the UPS network. Consists of a country ISO code, a three-digit postal zone indicator, and a sort code suffix. This code is used for sort and routing operations.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable, typically in format "XXX NNN N-NN"
- **Pattern/Regex:** `[A-Z]{2,3}\s\d{3}\s\d-\d{2}` (approximate)
- **Allowed Values:** Country ISO code + postal zone + sort code
- **Required:** yes

## Examples from Spec
- `DEU 091 0-00`
- `CHN 710 0-00`
- `JPN 106 1-00`
- `CAN 527 9-00`
- `CAN 400 5-00`
- `IL 606 9-02`
- `GA 301 9-01`
- `AZ 852 1-21`
- `MI 490 9-02`
- `ESP 285 4-40`
- `FRA 751 3-75`
- `FRA 196 3-75`
- `DEU 063 9-39`
- `DEU 510 9-00`
- `PRI 009 4-00`
- `DEU 415 9-00`

## Position on Label
Appears in a prominent position in the middle of the label, typically displayed twice — once in large text and once in smaller text or as part of a barcode area. Positioned below the ship-to address and above the service type.

## Edge Cases & Notes
For domestic US shipments, the routing code uses the state abbreviation (e.g., "IL 606 9-02", "GA 301 9-01") instead of a three-letter country code. For international shipments, the three-letter ISO country code is used (e.g., "DEU", "JPN", "CHN", "CAN", "ESP", "FRA", "PRI"). Some routing codes have a "P" or "V" suffix appended (e.g., "GA 301 9-01 P", "GA 301 9-01 V"). The "P" suffix appears to indicate a specific sort type (possibly premium), and "V" appears related to a different sort indicator.

## Claude Confidence
HIGH — Routing codes are consistently present on all label examples with clear format patterns.

## Review Status
- [ ] Reviewed by human