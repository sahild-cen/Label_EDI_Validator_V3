# Field: maxicode_service_class

## Display Name
MaxiCode Service Class Code

## Field Description
A numeric code within the MaxiCode data string that indicates the UPS service class for the shipment. Referenced as "96" in the MaxiCode data string examples.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 3 (implied from examples showing "96" prefix)
- **Pattern/Regex:** Not fully specified in spec
- **Allowed Values:** "96" shown in examples; other values not listed in this extract
- **Required:** yes

## Examples from Spec
- `<GS>96841706672<GS>` — the "96" appears as service class before the postal code
- `<GS>9628501<GS>` — the "96" appears as service class before the postal code

## Position on Label
Encoded within the MaxiCode 2D barcode data string, preceding the postal code.

## Edge Cases & Notes
- The "96" prefix in the MaxiCode data string appears to represent a service class or message header identifier.
- Full list of service class codes not provided in this extract.

## Claude Confidence
LOW — Only example value "96" is shown; the full specification of this field is likely in another section of the guide.

## Review Status
- [x] Reviewed by human