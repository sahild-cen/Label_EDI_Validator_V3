# Field: regulatory_information

## Display Name
General Regulatory Information

## Field Description
Regulatory information that may be legally required on the label, such as country-specific declarations, export information, or dangerous goods declarations.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** Up to 300 chars in segment 17b
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Country-specific regulatory text; DG declarations; export declarations
- **Required:** conditional — depends on shipment type, origin/destination country, and commodity

## Examples from Spec
No specific text examples in this extract.

## Position on Label
- General Regulatory Information: Segment 17b, starting in Line 2 ("Special_InfoA1")
- Dangerous Goods Declarations: Segment 17a, starting in Line 1 ("SPECIAL_INFO1")

## Edge Cases & Notes
- Regulatory information has primacy over special/conditional information in segment 17b
- If regulatory info occupies 17b, special info can be moved to "Piece Content" line
- Two data elements in "Piece Content" line can be concatenated with "/" separator (e.g., "CNP-12345678 / IE-987654321")
- Dangerous goods information is mandatory in segment 17a

## Claude Confidence
MEDIUM — spec describes placement rules but specific content formats depend on country regulations

## Review Status
- [ ] Reviewed by human