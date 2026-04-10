# Field: product_name

## Display Name
Product Name

## Field Description
The Global Product Name officially specifies the product under which the underlying transport service has been sold to the customer, printed in the associated "Product Short Name" format.

## Format & Validation Rules
- **Data Type:** string
- **Length:** Up to 20 characters
- **Pattern/Regex:** `[A-Za-z0-9 :]{1,20}` (upper-case letters, may contain full 7-bit standard chars including whitespace, upper/lower case and symbols such as colon)
- **Allowed Values:** DHL Express global product portfolio names (e.g., "EXPRESS WORLDWIDE")
- **Required:** conditional — mandatory for standard labels; may be omitted on Highly-Compact Labels upon special DHL approval

## Examples from Spec
"EXPRESS WORLDWIDE" is given as an example product name.

## Position on Label
Section 1 of the transport label, upper area of the label.

## Edge Cases & Notes
- Text string must be in upper-case letters
- For Highly-Compact Labels, this field may be omitted upon formal DHL Express approval to free up space for customer-specific elements
- Reference data is maintained in DHL's Global Reference Databases

## Claude Confidence
HIGH — spec clearly describes format, length, and conditional requirements

## Review Status
- [ ] Reviewed by human