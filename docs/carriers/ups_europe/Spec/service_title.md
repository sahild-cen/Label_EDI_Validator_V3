# Field: service_title

## Display Name
UPS Service Title

## Field Description
The name of the UPS service level used for the shipment, displayed prominently on the label.

## Format & Validation Rules
- **Data Type:** string
- **Length:** Variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Valid UPS service names including: UPS EXPRESS, UPS EXPEDITED, UPS ACCESS POINT ECONOMY, UPS Domestic Express, UPS Domestic Express Plus, UPS Worldwide Express, UPS Worldwide Express Plus, UPS Worldwide Express Saver, UPS Worldwide Expedited, UPS Worldwide Standard, UPS Transborder Standard, UPS Transborder Express, UPS Express NA1, UPS Express 12:00, and variants with package types (Letters/Envelopes, 10 KG Box, 25 KG Box, Express Box, Tube, PAK, GNIFC)
- **Required:** yes

## Examples from Spec
- `UPS EXPRESS`
- `UPS EXPEDITED`
- `UPS ACCESS POINT ECONOMY`

## Position on Label
Displayed prominently, typically in the routing/service section of the label. For Access Point labels, font size is reduced to 12 pt. bold.

## Edge Cases & Notes
- For Access Point labels, the service title size is specifically reduced.
- The full list of service titles is provided in the Manifest Summary section, showing all domestic, transborder, and worldwide services along with package type variants.

## Claude Confidence
HIGH — Multiple examples and comprehensive service list provided.

## Review Status
- [x] Reviewed by human