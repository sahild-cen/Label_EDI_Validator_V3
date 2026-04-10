# Field: data_matrix_customer_data

## Display Name
2D Data Matrix – Customer Data

## Field Description
A 2D Data Matrix barcode symbol containing customer-specific data, used on 2D-enabled transport labels.

## Format & Validation Rules
- **Data Type:** barcode (2D Data Matrix)
- **Length:** variable
- **Pattern/Regex:** Per ISO/IEC 16022 Data Matrix specification
- **Allowed Values:** Customer data as defined in DHL's 2D specifications
- **Required:** conditional — present on 2D-enabled labels

## Examples from Spec
No specific encoded data examples in extracted text. Referenced in "Standard 2D-enabled Label Sample" (section 5.1.2).

## Position on Label
Dedicated segment on the 2D-enabled transport label layout.

## Edge Cases & Notes
- Specific to the 2D-enabled label variant (ESS Label V3.0)
- Customer data content specifications are referenced in Global SOP Data Matrix 2D Specifications (R14)
- Data Matrix follows ISO/IEC 16022 international standard

## Claude Confidence
MEDIUM — spec references the 2D Data Matrix and customer data but detailed encoding specs are in a separate referenced document

## Review Status
- [ ] Reviewed by human