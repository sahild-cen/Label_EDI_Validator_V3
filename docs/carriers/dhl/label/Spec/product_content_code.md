# Field: product_content_code

## Display Name
Product Content Code

## Field Description
DHL's internal code for the product under which a certain transport order will be processed. Different products may share the same Product Content Code.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** exactly 3 characters
- **Pattern/Regex:** `[A-Z]{3}`
- **Allowed Values:** DHL product codes (e.g., "WPX", "EPL")
- **Required:** yes — mandatory

## Examples from Spec
"WPX" and "EPL" are given as examples.

## Position on Label
Section 1 of the transport label, alongside the Product Name.

## Edge Cases & Notes
- Must always consist of 3 upper-case characters
- For declarable shipments, the Product Content Code must be printed in reverse video format (white characters on black background)
- Product Name and Product Content Code can be determined based on (i) Service level (e.g., pre-9:00) and (ii) DOC or NON-DOC shipment

## Claude Confidence
HIGH — spec clearly defines format, examples, and mandatory status

## Review Status
- [ ] Reviewed by human