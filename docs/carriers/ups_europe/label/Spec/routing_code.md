# Field: routing_code

## Display Name
Routing Code

## Field Description
The UPS routing code that identifies the destination sort facility and delivery route. Appears in a prominent position on the label, typically showing country code, facility number, and route code.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec — format appears to be `[A-Z]{2,3} \d{3} \d-\d{2}`
- **Allowed Values:** Not restricted — determined by UPS routing system
- **Required:** yes

## Examples from Spec
"DEU 063 9-39", "FRA 753 7-00", "DEU 091 0-00", "AZ 852 1-21", "IL 606 9-02", "JPN 106 1-00", "CAN 527 9-00", "GA 300 9-05", "DEU 202 0-00", "FRA 751 3-75", "LUX 202 6-00", "BEL 344 9-14", "DEU 415 9-00", "SGP 256 2-00"

## Position on Label
Appears in the middle section of the label, between the ship-to address and the service/tracking area. Shown both as human-readable text and encoded in the MaxiCode barcode. Often appears twice — once above and once in/near the routing barcode area.

## ZPL Rendering
- **Typical Position:** Middle section, below ship-to address block; appears both as large text and repeated in barcode zone
- **Font / Size:** 24 pt per spec (for the large human-readable version)
- **Field Prefix:** None — displayed as standalone routing code
- **ZPL Command:** ^FD (text field) for human-readable; also encoded in MaxiCode

## Edge Cases & Notes
Format varies by country — international routes use 3-letter ISO country codes (DEU, FRA, JPN, CAN, etc.) while US domestic uses 2-letter state codes (AZ, IL, GA). The routing code is a critical sort/delivery element.

## Claude Confidence
HIGH — appears prominently on every label example, consistently positioned

## Review Status
- [ ] Reviewed by human