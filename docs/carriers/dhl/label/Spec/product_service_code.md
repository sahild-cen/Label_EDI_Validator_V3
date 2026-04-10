# Field: product_service_code

## Display Name
Product Service Code

## Field Description
A short code identifying a specific value-added service associated with the shipment, as displayed on the waybill/label.

## Format & Validation Rules
- **Data Type:** string
- **Length:** 1 character (based on example)
- **Pattern/Regex:** Not fully specified in spec
- **Allowed Values:** Example: "S" for Delivery Signature
- **Required:** conditional — only when value-added services are selected

## Examples from Spec
- "Delivery Signature" — Product Service Code: "S", Value: "1 000.00", Currency: "EUR"

## Position on Label
Appears in the services section of the transport label or waybill.

## Edge Cases & Notes
- Only one example service is shown in the extracted text; the complete list of service codes is not provided.
- Associated with a declared value and currency code.

## Claude Confidence
LOW — Only one example is provided; the full list of product service codes is not in the extracted text.

## Review Status
- [ ] Reviewed by human