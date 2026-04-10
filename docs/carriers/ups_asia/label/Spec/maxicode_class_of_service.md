# Field: maxicode_class_of_service

## Display Name
Class of Service (MaxiCode)

## Field Description
A 3-digit numeric code representing the UPS service level, encoded in the MaxiCode data string. Can be derived from the 2-character 1Z Service Level Indicator through a conversion calculation.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 3 (exact)
- **Pattern/Regex:** `\d{3}`
- **Allowed Values:** Derived from 1Z Service Level Indicator conversion (values 0-992+)
- **Required:** yes

## Examples from Spec
- `001` (appears in multiple MaxiCode examples)
- `066` (international example)
- `426` (converted from service level indicator "EA": E=416 + A=10 = 426)

## Position on Label
Encoded within the MaxiCode barcode (primary message, third data field).

## Edge Cases & Notes
- Conversion from 2-character alphanumeric 1Z Service Level Indicator to 3-digit numeric: First character value (from lookup table, multiples of 32) + second character value (0-31).
- If the Class of Service value is less than 100, no conversion takes place (backward compatibility).
- Detailed conversion tables provided in spec with first character values (0-992 in steps of 32) and second character values (0-31).

## Claude Confidence
HIGH — spec provides detailed conversion method, lookup tables, and examples.

## Review Status
- [ ] Reviewed by human