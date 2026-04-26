# Field: label_certification_identifier

## Display Name
Label Certification Identifier

## Field Description
A unique identifier assigned by DHL's Global Competence Center for Labels (GCoCL) that certifies the transport label has been approved for production use within the DHL Express network. There are permanent and temporary variants.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable — follows sequential scheme managed centrally by GCoCL
- **Pattern/Regex:** Not fully specified in extracted text; permanent and temporary follow different naming conventions. Temporary starts with a fixed suffix followed by serial number and date.
- **Allowed Values:** Centrally managed by GCoCL team
- **Required:** yes

## Examples from Spec
Permanent Label Certification Identifier follows a sequential scheme. Temporary certification follows a different naming convention starting with a fixed suffix followed by a serial number and date. Temporary must be reviewed after 6 months.

## ZPL Rendering
- **Typical Position:** top-left area, part of the printing application line
- **Font / Size:** 1.5mm font size or 5 points
- **Field Prefix:** Enclosed in asterisks: "* [ID] *"
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Temporary certifications are valid for a limited period and must be reviewed after 6 months. Once fully compliant, the temporary ID is changed to a permanent ID. A DHL Label Certification Identifier is a pre-condition for a Transport Label to be released for production use.

## Claude Confidence
MEDIUM — structure described but exact regex/format not fully visible in extracted text

## Review Status
- [ ] Reviewed by human