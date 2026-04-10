# Field: label_printing_date

## Display Name
Label Printing Date

## Field Description
The date on which the label was printed/rendered, following the ISO 8601 standard.

## Format & Validation Rules
- **Data Type:** date
- **Length:** 10 characters (yyyy-mm-dd)
- **Pattern/Regex:** `\d{4}-\d{2}-\d{2}`
- **Allowed Values:** Valid dates in ISO 8601 format
- **Required:** yes — mandatory

## Examples from Spec
No specific date examples given in spec, but format is "yyyy-mm-dd" where YYYY=year, mm=month, dd=date.

## Position on Label
Follows the identification of the Rendering Application, underneath the Product Short Name.

## Edge Cases & Notes
- In the case of GLS, it is based on the server's date and time
- Part of the combined segment format: "[PRINTING APPLICATION]"/"[PRINTING DATE]"/"* [CERTIFICATION IDENTIFIER]*"

## Claude Confidence
HIGH — spec clearly defines ISO 8601 format and mandatory status

## Review Status
- [ ] Reviewed by human