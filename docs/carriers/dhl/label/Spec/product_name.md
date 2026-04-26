# Field: product_name

## Display Name
Product Name

## Field Description
The Global Product Name officially specifies the product under which the underlying transport service has been sold to the customer. It is printed as the "Product Short Name" (e.g., EXPRESS WORLDWIDE).

## Format & Validation Rules
- **Data Type:** string
- **Length:** up to 20 characters
- **Pattern/Regex:** [A-Za-z0-9 :]{1,20}
- **Allowed Values:** DHL Express global product portfolio names (e.g., EXPRESS WORLDWIDE)
- **Required:** conditional — mandatory for standard labels; may be omitted on Highly-Compact labels with formal DHL Express approval

## Examples from Spec
"EXPRESS WORLDWIDE" mentioned as example. Text string in upper-case letters, up to 20 chars long. May contain the full set of 7-bit standard chars including white space, upper/lower case chars and symbols such as a colon (":").

## ZPL Rendering
- **Typical Position:** top-left area of label (section 1)
- **Font / Size:** Not specified in extracted text
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
On Highly-Compact labels, the Product Name may be omitted upon special approval by DHL Express. This is to maximize compactness when customers require extra info or elements (e.g., additional barcodes) in the customer-owned segment.

## Claude Confidence
HIGH — clearly defined in spec sections 5.2 and 5.2.1

## Review Status
- [ ] Reviewed by human