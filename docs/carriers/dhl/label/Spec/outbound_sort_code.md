# Field: outbound_sort_code

## Display Name
Outbound Sort Code

## Field Description
A sort code defined by each DHL Service Area per Destination Facility Code, used to support manual sorting at outbound facilities. This is part of the Manual Sorting Section on the label.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 1-4 characters
- **Pattern/Regex:** [A-Z0-9]{1,4}
- **Allowed Values:** Values from DHL's Global Reference Database (GREF); "." if lookup returned no value; blank if no attempt was made
- **Required:** conditional — mandatory when defined in GREF for the outbound facility; not all outbound facilities have sort codes defined

## Examples from Spec
"Sort Codes consist of up to four alphanumeric chars (numerals or capital letters)." When not defined: populated with ".". When no attempt was made: left blank.

## ZPL Rendering
- **Typical Position:** manual sorting section, leftmost element (element 10)
- **Font / Size:** Not specified in extracted text
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
A "." indicates that an effective attempt to look up a sort code returned no value. A blank field indicates no attempt was made to determine the Outbound Sort Code, which will also indicate to DHL that the label needs to be reprinted. The information is available in DHL's Global Reference Database (GREF).

## Claude Confidence
HIGH — clearly specified in section 5.9.1

## Review Status
- [ ] Reviewed by human