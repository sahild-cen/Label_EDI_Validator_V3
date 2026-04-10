# Field: outbound_sort_code

## Display Name
Outbound Sort Code

## Field Description
A sort code defined by each DHL Service Area per Destination Facility Code, used to support manual sorting operations at outbound facilities.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** Up to 4 characters
- **Pattern/Regex:** `[A-Z0-9]{1,4}`
- **Allowed Values:** Values from DHL's Global Reference Database (GREF); "." if lookup returned no value; blank if no attempt was made
- **Required:** conditional — mandatory when defined in GREF for the outbound facility

## Examples from Spec
No specific code examples given. "." is used when effective lookup returned no value. Blank indicates no lookup attempt was made.

## Position on Label
Left portion of the Manual Sorting Section (element 10).

## Edge Cases & Notes
- Consists of numerals or capital letters, up to 4 characters
- If no Outbound Sort Code is defined by DHL Express in the country of origin, field is populated with "."
- "." means an effective lookup attempt returned no value
- Blank/empty means no attempt was made to determine the code, which indicates to DHL the label needs reprinting
- Information available in GREF which must be referred to for latest valid values

## Claude Confidence
HIGH — spec clearly defines format, conditional logic, and population rules

## Review Status
- [ ] Reviewed by human