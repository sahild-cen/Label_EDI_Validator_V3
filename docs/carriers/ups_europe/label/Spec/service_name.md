# Field: service_name

## Display Name
Service Name / Service Title

## Field Description
The human-readable UPS service name indicating the level of service for the shipment.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** "UPS EXPRESS", "UPS EXPRESS PLUS", "UPS EXPRESS 12:00", "UPS SAVER", "UPS EXPEDITED", "UPS STANDARD", "UPS NEXT DAY AIR", "UPS EXPRESS FREIGHT", "UPS EXPRESS FREIGHT MIDDAY", "UPS EXPRESS (NA1)", "UPS ACCESS POINT ECONOMY" and others
- **Required:** yes

## Examples from Spec
"UPS EXPRESS", "UPS EXPRESS PLUS", "UPS EXPRESS 12:00", "UPS SAVER", "UPS EXPEDITED", "UPS STANDARD", "UPS NEXT DAY AIR", "UPS EXPRESS FREIGHT", "UPS EXPRESS FREIGHT MIDDAY", "UPS EXPRESS (NA1)", "UPS ACCESS POINT ECONOMY"

## Position on Label
Below the routing code / MaxiCode section, prominently displayed in a large font.

## ZPL Rendering
- **Typical Position:** Middle section, below routing code area
- **Font / Size:** 16 pt Bold per spec
- **Field Prefix:** None — standalone service name
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
The service title from the spec's service table (page 32) corresponds to service indicators. Express Freight labels use "UPS EXPRESS FREIGHT™" branding.

## Claude Confidence
HIGH — clearly shown on all label examples with consistent positioning

## Review Status
- [ ] Reviewed by human