# Field: printing_application_identifier

## Display Name
Printing Application, Date and Label Certification Identifier

## Field Description
A composite text line identifying the label printing application name, its version, the printing date, and the associated Label Certification Identifier. The full format is: "[PRINTING APPLICATION]"/"[PRINTING DATE]"/"* [CERTIFICATION IDENTIFIER]*"

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** .+\/\d{4}-\d{2}-\d{2}\/\*[A-Z0-9\-]+\*
- **Allowed Values:** Not restricted (application name is free text; version follows X.XX.XXX format)
- **Required:** yes

## Examples from Spec
Full format: "[PRINTING APPLICATION]"/"[PRINTING DATE]"/"* [CERTIFICATION IDENTIFIER]*". Application version format: X.XX.XXX. Example application: "Express Logistics Platform - ELP".

## ZPL Rendering
- **Typical Position:** underneath the Product Short Name, top-left area
- **Font / Size:** Not specified for application name; Certification Identifier is 1.5mm font size or 5 points
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
There is no binding format for the Printing Application name itself, but its version must follow X.XX.XXX format. The field is located underneath the Product Short Name. This is a single printed line combining multiple data elements.

## Claude Confidence
MEDIUM — format described but exact rendering details are limited

## Review Status
- [ ] Reviewed by human