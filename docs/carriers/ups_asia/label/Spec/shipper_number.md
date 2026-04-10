# Field: shipper_number

## Display Name
Shipper Number (SHP#)

## Field Description
The UPS shipper identification number printed in the Package Information Block.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
`SHP#: 1X2X 3X33 3VP`, `SHP#: 1X2X 3X33 3TT`, `SHP #: 12 3XX 3WB`

## Position on Label
Package Information Block, typically to the right of the Ship From address.

## Edge Cases & Notes
- The prefix may appear as either `SHP#:` or `SHP #:` based on examples in the spec.

## Claude Confidence
HIGH — multiple examples shown across label diagrams

## Review Status
- [ ] Reviewed by human