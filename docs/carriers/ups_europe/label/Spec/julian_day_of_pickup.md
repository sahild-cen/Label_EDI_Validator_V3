# Field: julian_day_of_pickup

## Display Name
Julian Day of Pickup

## Field Description
The Julian day (day of the year, 001-366) representing the date the package is picked up by UPS. This is encoded in the MaxiCode secondary message.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 3 digits
- **Pattern/Regex:** `^[0-9]{3}$`
- **Allowed Values:** 001-366
- **Required:** yes

## Examples from Spec
- `187` (all MaxiCode examples)

## Position on Label
Encoded within MaxiCode secondary message.

## ZPL Rendering
- **Typical Position:** Encoded within MaxiCode
- **Font / Size:** Not applicable
- **Field Prefix:** None
- **ZPL Command:** Encoded within ^BD (MaxiCode)

## Edge Cases & Notes
- Julian day 187 corresponds to approximately July 6 in a non-leap year.
- Must be zero-padded to 3 digits (e.g., day 5 = "005").

## Claude Confidence
HIGH — spec clearly defines the field with consistent examples

## Review Status
- [ ] Reviewed by human