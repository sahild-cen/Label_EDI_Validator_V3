# Field: tracking_number

## Display Name
Tracking Number (UPS Tracking Number)

## Field Description
The UPS customized unique package ID used with tracking/tracing services. It is a barcode-encoded and human-readable identifier for each package. The tracking number contains embedded fields including the UPS Account Number (positions 3-8), Service Indicator (positions 9-10), Reference Number (positions 11-17), and a Modified MOD 10 check digit at the end.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 18 characters (1Z + 6-digit account + 2-digit service indicator + 7-digit reference + 1 check digit)
- **Pattern/Regex:** `^1Z[A-Z0-9]{6}[A-Z0-9]{2}[0-9]{7}[0-9]$` (inferred from field position descriptions)
- **Allowed Values:** Starts with "1Z"; positions 3-8 = UPS Account Number; positions 9-10 = Service Indicator; positions 11-17 = Reference Number (must be unique per package); final position = Modified MOD 10 check digit
- **Required:** yes

## Examples from Spec
No exact examples in the extracted appendix text. The spec references "1Z" prefix tracking numbers and states each label should have a unique tracking number.

## Position on Label
Not specified in the extracted text — core label layout sections would define this. Typically rendered as a Code 128 barcode in the primary barcode area of the label.

## ZPL Rendering
- **Typical Position:** Bottom barcode area (primary barcode block) — exact X,Y not specified in extracted text
- **Font / Size:** Not specified in extracted text
- **Field Prefix:** "TRACKING #:" or similar human-readable interpretation below barcode
- **ZPL Command:** ^BC (Code 128 barcode) for barcode rendering; ^FD (text field) for human-readable interpretation

## Edge Cases & Notes
- The spec defines that each label submitted must have a unique tracking number.
- The tracking number uses Code 128 symbology, specifically starting with Subset A and switching to Subset C for numeric portions to create shorter barcode symbols.
- The Modified MOD 10 check digit must be correctly calculated and appended.
- Reference Number (positions 11-17) must be unique for each package, similar to a progressive number.

## Claude Confidence
MEDIUM — Field is clearly defined in the glossary/definitions section, but exact label positioning, ZPL coordinates, and font details are not in the extracted text.

## Review Status
- [ ] Reviewed by human