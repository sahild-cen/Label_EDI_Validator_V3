# Field: inbound_sort_code

## Display Name
Inbound Sort Code

## Field Description
A sort code used at destination/inbound facilities to support manual sorting. It can serve as either a consolidator (various facilities sharing the same code) or separator (facility sub-divided by postal code and/or product).

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** Up to 4 characters
- **Pattern/Regex:** `[A-Z0-9]{1,4}`
- **Allowed Values:** Values from DHL reference databases; "." if lookup returned no value; blank if no attempt was made
- **Required:** conditional — mandatory when defined for the inbound facility

## Examples from Spec
No specific code examples given. "." used when effective lookup returned no value.

## Position on Label
Right portion of the Manual Sorting Section (element 12).

## Edge Cases & Notes
- Consists of numerals or capital letters, up to 4 characters
- Depends on destination country, postcode, and product
- Can serve as Consolidator (various facilities with same code) or Separator (facility sub-divided by postal code/product)
- "." means an effective lookup attempt returned no value
- Blank/empty means no attempt was made, indicating to DHL the label needs reprinting
- DHL may not require for all destinations

## Claude Confidence
HIGH — spec clearly defines format, conditional logic, and population rules

## Review Status
- [ ] Reviewed by human