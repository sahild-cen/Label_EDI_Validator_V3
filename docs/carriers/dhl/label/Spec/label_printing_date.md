# Field: label_printing_date

## Display Name
Label Printing Date

## Field Description
The date on which the label was printed/rendered, conforming to ISO 8601 standard. It follows the identification of the Rendering Application in the label segment.

## Format & Validation Rules
- **Data Type:** date
- **Length:** 10 characters (exact)
- **Pattern/Regex:** \d{4}-\d{2}-\d{2}
- **Allowed Values:** Valid date in yyyy-mm-dd format
- **Required:** yes

## Examples from Spec
Format is yyyy-mm-dd where "YYYY" refers to the year, "mm" to the month and "dd" to the date. In the case of GLS it is based on the server's date and time.

## ZPL Rendering
- **Typical Position:** top-left area, following the Printing Application identifier
- **Font / Size:** Not specified
- **Field Prefix:** None — part of composite line separated by "/"
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Date follows ISO 8601 standard. When using GLS rendering, the date is based on the server's date and time, not the local client time.

## Claude Confidence
HIGH — clearly specified format and requirement

## Review Status
- [ ] Reviewed by human