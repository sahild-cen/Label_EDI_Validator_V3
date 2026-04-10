# Field: content_description

## Display Name
Content Description

## Field Description
Mandatory field describing the contents of the shipment. Located primarily in segment 17a of the label, supporting up to 150 characters, with overflow capability into segment 17b (300 characters).

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** Up to 150 chars in segment 17a; up to 300 chars in segment 17b; combined support for at least 300 chars
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Free text content description; or "CTD – see data" for approved neutral content descriptions
- **Required:** yes — mandatory

## Examples from Spec
- "CTD – see data" for neutral content descriptions (bold font, min 3mm character height)
- "Belgian chocolate" or "Li-metal batteries with equipment" (from special information context)

## Position on Label
- Primarily in segment 17a (right of Waybill barcode), starting in Line 1 ("Special_Info1")
- If content extends beyond segment 17a capacity and no regulatory information uses 17b, can overflow into segment 17b

## Edge Cases & Notes
- For approved customers meeting Neutral Content Label criteria, content descriptions can be replaced with "CTD – see data" (bold, min 3mm height)
- Dangerous Goods Declarations must be located in segment 17a
- General Regulatory Information goes in segment 17b, starting in Line 2 ("Special_InfoA1")
- Regulatory information takes primacy over special information in segment 17b

## Claude Confidence
HIGH — spec provides clear mandatory status, location rules, and neutral content alternative

## Review Status
- [ ] Reviewed by human