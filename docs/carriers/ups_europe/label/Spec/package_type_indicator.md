# Field: package_type_indicator

## Display Name
Package Type Indicator

## Field Description
An indicator for the package type such as letter (LTR) or envelope (ENV), displayed adjacent to the weight when the package is not a standard package.

## Format & Validation Rules
- **Data Type:** string
- **Length:** 3 characters typical
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** "LTR", "ENV" and potentially others
- **Required:** conditional — only when package is a non-standard type (letter, envelope)

## Examples from Spec
"LTR" (page 30, 31 — "0.6 LBS LTR"), "ENV" (page 50 — "2.3 KG ENV")

## Position on Label
Top-right area, between the weight and the piece count.

## ZPL Rendering
- **Typical Position:** Top-right, between weight value and piece count
- **Font / Size:** Not specified — appears same size as weight
- **Field Prefix:** None — appears as standalone abbreviation
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Only appears for non-standard package types. Not shown on most labels with standard packages.

## Claude Confidence
MEDIUM — shown in a few examples; limited detail on all possible values

## Review Status
- [ ] Reviewed by human