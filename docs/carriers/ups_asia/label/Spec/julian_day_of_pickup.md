# Field: julian_day_of_pickup

## Display Name
Julian Day of Pickup

## Field Description
The Julian day (day of year, 1-366) representing the pickup/collection date, encoded in the MaxiCode data string.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 3 (exact)
- **Pattern/Regex:** `\d{3}` (values 001-366)
- **Allowed Values:** 001 to 366
- **Required:** yes

## Examples from Spec
- `187` (used in all MaxiCode examples)

## Position on Label
Encoded within the MaxiCode barcode (secondary message).

## Edge Cases & Notes
- Represents the ordinal day of the year (e.g., January 1 = 001, July 6 = 187).

## Claude Confidence
HIGH — spec clearly defines as 3-digit numeric field with examples.

## Review Status
- [x] Reviewed by human