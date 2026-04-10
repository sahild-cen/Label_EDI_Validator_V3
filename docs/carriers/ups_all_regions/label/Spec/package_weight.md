# Field: package_weight

## Display Name
Package Weight

## Field Description
The weight of the individual package, printed on the label. Weight display format varies by service type and origin country.

## Format & Validation Rules
- **Data Type:** alphanumeric (numeric value with unit)
- **Length:** variable
- **Pattern/Regex:** `[0-9]+(\.[0-9])?\s*(LBS|KG|KGS|OZ)`
- **Allowed Values:** Weight value followed by unit of measure (LBS, KG, KGS, OZ)
- **Required:** yes — must be printed on all applicable labels

## Examples from Spec
- `203 KG` (Express Freight)
- `10.2 OZ` (SurePost)
- `50 LBS` (ISC domestic)
- `8 KG` (Premium Care, Proactive Response international)
- `13 LBS` (domestic with COD)
- `15 LBS` (domestic return service)
- `5 LBS` (international return)
- `12 KG` (refrigeration international)
- `16.9 OZ` (Economy DDU)

## Position on Label
Printed in the upper portion of the label, typically in the package information block.

## Edge Cases & Notes
For UPS Worldwide Economy: DDP shipments from US/Canada must display in pounds; DDU from US/Canada must display in ounces to the tenth. Shipments from outside US/Canada must display in kilograms to the tenth. Rounding rules apply: any value other than zero in the hundredth position requires rounding up (e.g., 3.02 oz → 3.1 OZ, 1.091 kg → 1.1 KGS). For MaxiCode in Economy shipments, the weight field must contain "1".

## Claude Confidence
HIGH — Multiple examples and detailed format rules provided, especially for Worldwide Economy.

## Review Status
- [ ] Reviewed by human