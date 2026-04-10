# Field: label_certification_identifier

## Display Name
Label Certification Identifier

## Field Description
A unique identifier assigned by the GCoCL team that certifies the transport label has been approved for production and use within the DHL Express network. Can be permanent or temporary.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable (follows sequential scheme managed by GCoCL team)
- **Pattern/Regex:** Permanent follows a sequential convention; Temporary starts with a fixed suffix followed by serial number and date
- **Allowed Values:** Centrally managed by GCoCL team
- **Required:** yes — mandatory (permanent); temporary certification valid for 6 months

## Examples from Spec
No specific identifier examples provided in the extracted text.

## Position on Label
Part of the combined segment: "[PRINTING APPLICATION]"/"[PRINTING DATE]"/"* [CERTIFICATION IDENTIFIER]*". Font size is 1.5mm or 5 points.

## Edge Cases & Notes
- Permanent and temporary identifiers follow different naming conventions
- Temporary certification must be reviewed after 6 months; once fully compliant, temporary ID changed to permanent
- A Label Certification Identifier is a pre-condition for a Transport Label to be released for production use

## Claude Confidence
MEDIUM — spec describes purpose and rules but specific format/regex is not fully detailed in extracted text

## Review Status
- [ ] Reviewed by human