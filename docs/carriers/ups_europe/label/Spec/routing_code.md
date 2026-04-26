# Field: routing_code

## Display Name
Routing Code

## Group Description
The UPS routing code that appears in the center of the label, used for package sorting and routing. Displayed both as human-readable text and within a barcode. Format consists of a country code abbreviation, a 3-digit code, and additional routing digits.

## Sub-Fields

### routing_code_text
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** `^[A-Z]{2,3}\s+\d{3}\s+\d-\d{2}$`
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Human-readable routing code for package sortation, typically formatted as country abbreviation + space + 3-digit area code + space + routing suffix
- **Detect By:** spatial:center_label, pattern matching country code + digits
- **Position on Label:** center of label, appears twice (once large, once smaller near barcode)
- **ZPL Font:** 24 pt per font chart (large instance)
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Examples from Spec
- "DEU 063 9-39"
- "FRA 753 7-00"
- "SGP 256 2-00"
- "DEU 091 0-00"
- "AZ 852 1-21"
- "IL 606 9-02"
- "JPN 106 1-00"
- "GA 300 9-05"
- "CAN 527 9-00"
- "DEU 202 0-00"
- "DEU 415 9-00"
- "LUX 202 6-00"
- "BEL 344 9-14"
- "FRA 751 3-75"

## Edge Cases & Notes
- The routing code appears twice on the label: once in large text (24 pt) and once near/below the routing barcode.
- International routing codes use 3-letter country abbreviations (DEU, FRA, SGP, JPN, CAN, LUX, BEL).
- US domestic routing codes use 2-letter state abbreviations (AZ, IL, GA).
- The routing code is also encoded in a barcode (see routing_barcode entry).

## Claude Confidence
HIGH — Consistently appears across all label examples with clear pattern.

## Review Status
- [x] Reviewed by human