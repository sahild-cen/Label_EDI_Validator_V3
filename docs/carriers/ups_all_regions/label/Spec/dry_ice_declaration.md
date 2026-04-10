# Field: dry_ice_declaration

## Display Name
Dry Ice Declaration Line

## Field Description
A mandatory text string that must appear on the label when shipping dry ice, indicating the UN number, proper shipping name, hazard class, quantity, and weight in kilograms of the dry ice contained in the package.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 38 characters total
- **Pattern/Regex:** `^UN1845, DRY ICE, CLASS 9, 1 x\s{1}\d{1,4}\.?\d?\sKG$`
- **Allowed Values:** Positions 1-29 = static text "UN1845, DRY ICE, CLASS 9, 1 x"; Position 30 = space; Positions 31-35 = up to five numeric characters (inclusive of decimal point) for dry ice weight; Position 36 = space; Positions 37-38 = "KG"
- **Required:** conditional — required when shipping dry ice

## Examples from Spec
- "UN1845, DRY ICE, CLASS 9, 1 x 12.5 KG"
- "UN 1845, DRY ICE, CLASS 9, 1 x 6 KG" (from label examples)

## Position on Label
Prints in the Additional Routing Instructions block of the label, immediately below the Description of Goods.

## Edge Cases & Notes
- Positions 1-29 are static text — identical for all Dry Ice shipments.
- Weight must always be in kilograms and rounded to the next tenth.
- Font Size = 10 pt.
- Dry ice is a general service offering for certain US and Puerto Rico domestic shipments but also applies internationally.
- The service may be used with UPS Returns™ or UPS Import Control™.

## Claude Confidence
HIGH — spec provides exact positional data, format rules, and examples.

## Review Status
- [ ] Reviewed by human