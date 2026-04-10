# Field: service_type

## Display Name
Service Type / Product Code

## Field Description
Identifies the DHL shipping service/product selected for the shipment, such as Express Worldwide, Express 9:00, Express 12:00, Economy Select, etc.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 1-3 characters (product code) or full text name
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** DHL product codes including but not limited to: "D" (Express Worldwide), "T" (Express 12:00), "K" (Express 9:00), "P" (Express Worldwide), "U" (Express Worldwide ECX), "Y" (Express 12:00), "N" (Domestic Express), "H" (Economy Select), "W" (Economy Select)
- **Required:** yes

## Examples from Spec
No examples in spec.

## Position on Label
Typically displayed near the top of the label, often with the DHL product name in text form.

## Edge Cases & Notes
The product/service code is also encoded in the barcode data. Different service types may require slightly different label layouts or additional fields (e.g., time-definite services require delivery commitment time).

## Claude Confidence
MEDIUM — Service types are well-known but exact code mappings may vary by region and are not in the extracted text.

## Review Status
- [ ] Reviewed by human