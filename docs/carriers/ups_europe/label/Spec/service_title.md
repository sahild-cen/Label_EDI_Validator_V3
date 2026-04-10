# Field: service_title

## Display Name
UPS Service Title

## Field Description
The name of the UPS service being used for the shipment, displayed prominently on the label.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Enumerated list including: UPS EXPRESS, UPS EXPEDITED, UPS ACCESS POINT ECONOMY, UPS Domestic Express, UPS Domestic Express Plus, UPS Worldwide Express, UPS Worldwide Express Plus, UPS Worldwide Expedited, UPS Worldwide Express Saver, UPS Worldwide Standard, UPS Transborder Standard, UPS Transborder Express, UPS Express NA1, UPS Express 12:00, and many packaging variants
- **Required:** yes

## Examples from Spec
- `UPS EXPRESS`
- `UPS EXPEDITED`
- `UPS ACCESS POINT ECONOMY`

## Position on Label
Prominently displayed, typically in the middle section of the label near the routing information.

## ZPL Rendering
- **Typical Position:** Middle section, typically right-justified or centered
- **Font / Size:** 12 pt. bold (reduced for Access Point labels)
- **Field Prefix:** None (standalone text)
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
For Access Point labels, the service title font size is reduced to 12 pt. bold. The shipment summary in the manifest document lists all possible service titles with packaging variants (Letters/Envelopes, 10 KG Box, 25 KG Box, Express Box, Tube, PAK, GNIFC).

## Claude Confidence
HIGH — Spec lists comprehensive service titles and specifies font size

## Review Status
- [ ] Reviewed by human