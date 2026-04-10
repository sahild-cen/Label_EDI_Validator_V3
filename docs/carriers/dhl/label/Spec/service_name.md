# Field: service_name

## Display Name
Global Service Name

## Field Description
The human-readable name of the DHL Express service/product being used for the shipment.

## Format & Validation Rules
- **Data Type:** string
- **Length:** Variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** DHL product names such as "EUROPACK", "DOM EUROPACK", "ECONOMY SELECT", "EXPRESS WORLDWIDE", "Medical EXPRESS", etc.
- **Required:** yes

## Examples from Spec
- "EUROPACK"
- "DOM EUROPACK"
- "ECONOMY SELECT"
- "EXPRESS WORLDWIDE"

## Position on Label
Appears as human-readable text on the transport label in the handling/product information area.

## Edge Cases & Notes
- The service name corresponds to the 2-digit product code in the routing barcode.
- The Medical EXPRESS product has a specific logo specification (section 5.10.4).

## Claude Confidence
MEDIUM — Service names are referenced throughout examples but the complete enumeration and exact display rules are not fully detailed in the extracted text.

## Review Status
- [ ] Reviewed by human