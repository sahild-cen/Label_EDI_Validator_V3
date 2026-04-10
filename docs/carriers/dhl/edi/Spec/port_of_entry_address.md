# Field: port_of_entry_address

## Display Name
Port of Entry Address

## Field Description
A new address qualifier (NAD+JD) added at SG43 level for identifying the Port of Entry location, specifically introduced for Loose BBX (LBBX) purposes.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** NAD qualifier "JD"
- **Required:** conditional — used for LBBX shipments

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
Added in version 0.8 of the document specifically for LBBX purposes. This is a DHL-specific NAD qualifier.

## Claude Confidence
MEDIUM — Documented in change report but detailed format not in extracted text.

## Review Status
- [ ] Reviewed by human