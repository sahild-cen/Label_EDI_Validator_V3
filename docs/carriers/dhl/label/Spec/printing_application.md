# Field: printing_application

## Display Name
Printing Application

## Field Description
Identifies the label printing/rendering application used to generate the label, along with its version number.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable (no binding format for the name)
- **Pattern/Regex:** Version format: `X.XX.XXX` (for the version portion)
- **Allowed Values:** Not restricted (e.g., "Express Logistics Platform - ELP")
- **Required:** yes — mandatory

## Examples from Spec
"Express Logistics Platform - ELP" is given as an example printing application name.

## Position on Label
Located underneath the Product Short Name.

## Edge Cases & Notes
- No binding format for the application name itself, but the version follows the X.XX.XXX convention
- Part of a combined segment: "[PRINTING APPLICATION]"/"[PRINTING DATE]"/"* [CERTIFICATION IDENTIFIER]*"

## Claude Confidence
MEDIUM — spec describes the field but notes "no binding format" for the application name

## Review Status
- [ ] Reviewed by human