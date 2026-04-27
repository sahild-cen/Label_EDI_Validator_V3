# Field: service_name

## Display Name
Service Name / Service Title

## Field Description
The UPS service level name displayed on the label, identifying the shipping service used.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** "UPS EXPRESS", "UPS EXPRESS PLUS", "UPS EXPRESS 12:00", "UPS SAVER", "UPS EXPEDITED", "UPS STANDARD", "UPS NEXT DAY AIR", "UPS EXPRESS FREIGHT", "UPS EXPRESS FREIGHT MIDDAY", "UPS EXPRESS (NA1)", "UPS ACCESS POINT ECONOMY"
- **Required:** yes

## Examples from Spec
"UPS EXPRESS", "UPS EXPRESS PLUS", "UPS EXPRESS 12:00", "UPS SAVER", "UPS EXPEDITED", "UPS STANDARD", "UPS NEXT DAY AIR", "UPS EXPRESS FREIGHT", "UPS EXPRESS FREIGHT MIDDAY", "UPS EXPRESS (NA1)", "UPS ACCESS POINT ECONOMY"

## Position on Label
Center section of the label, below the routing code, displayed in large bold text.

## Edge Cases & Notes
The service name is a critical visual identifier. It must match the service indicator code used in the tracking number. Some service names include time-definite elements (e.g., "12:00", "PLUS").

## Claude Confidence
HIGH — clearly defined across all label examples and in the service table on page 32

## Review Status
- [x] Reviewed by human