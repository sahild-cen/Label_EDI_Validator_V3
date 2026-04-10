# Field: biological_substances_indicator

## Display Name
Biological Substances Indicator (ISC-BIO)

## Field Description
A routing instruction indicator that must print on the label when shipping biological substances, alerting UPS Operations that the package contains biological substances.

## Format & Validation Rules
- **Data Type:** string
- **Length:** 7 characters
- **Pattern/Regex:** `^ISC-BIO$`
- **Allowed Values:** "ISC-BIO"
- **Required:** conditional — required when shipping biological substances

## Examples from Spec
"ISC-BIO" (shown on the Biological Substances label example)

## Position on Label
Prints centered in the Additional Routing Instructions block of the label, immediately below the Power of Attorney (POA) line.

## Edge Cases & Notes
- Font Size = 10 pt. bold.
- Biological Substances is offered as a contract service.
- The biological substances label example also shows a Dry Ice declaration and Audit Indicator below the ISC-BIO line, indicating both can appear together.

## Claude Confidence
HIGH — spec clearly defines the exact text, font, and placement.

## Review Status
- [ ] Reviewed by human