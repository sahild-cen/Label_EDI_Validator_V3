# Field: product_content_code

## Display Name
Product Content Code

## Field Description
DHL's internal code for the product under which a certain transport order will be processed. It identifies the DHL product type and determines how the shipment is handled through the network.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 3 characters (exact)
- **Pattern/Regex:** [A-Z]{3}
- **Allowed Values:** DHL product codes (e.g., WPX, EPL) — maintained in DHL Global Reference Databases
- **Required:** yes

## Examples from Spec
"WPX" and "EPL" mentioned as examples. Always consists of 3 upper-case characters. Different products may have the same Product Content Code.

## ZPL Rendering
- **Typical Position:** top-left area of label, adjacent to or near Product Name (section 1)
- **Font / Size:** Not specified; for declarable shipments must be printed in reverse video format (white text on black background)
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field); ^GB (graphic box) + ^FR (field reverse) for reverse video rendering on declarable shipments

## Edge Cases & Notes
For declarable shipments, the Product Content Code MUST be printed in reverse video format (white characters on black background). Product Name and Product Content Code can be determined based on (i) Service level (e.g. pre-9:00) and (ii) DOC or NON-DOC shipment.

## Claude Confidence
HIGH — clearly specified as mandatory with formatting rules

## Review Status
- [ ] Reviewed by human