# Field: inbound_sort_code

## Display Name
Inbound Sort Code

## Field Description
A sort code used at the inbound/destination facility to support manual sorting. It depends on destination country, postcode, and product, and can serve as either a consolidator (various facilities sharing the same code) or a separator (sub-dividing a facility based on postal code and/or product).

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 1-4 characters
- **Pattern/Regex:** [A-Z0-9]{1,4}
- **Allowed Values:** Values from DHL's Global Reference databases; "." if lookup returned no value; blank if no attempt was made
- **Required:** conditional — mandatory when defined for the inbound facility; not all inbound facilities have sort codes defined

## Examples from Spec
"The Inbound Sort Code consists of up to 4 alphanumeric chars (numerals or capital letters)." When not defined: populated with ".". When no attempt was made: left blank.

## ZPL Rendering
- **Typical Position:** manual sorting section, rightmost element (element 12)
- **Font / Size:** Not specified in extracted text
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
A "." indicates an effective attempt to look up a sort code returned no value. A blank field indicates no attempt was made, signaling to DHL that the label needs to be reprinted. Can serve dual purposes: consolidator (grouping multiple facilities) or separator (sub-dividing a single facility).

## Claude Confidence
HIGH — clearly specified in section 5.9.3

## Review Status
- [ ] Reviewed by human