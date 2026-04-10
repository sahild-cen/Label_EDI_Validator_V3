# Field: service_icon

## Display Name
Service Icon

## Field Description
A visual icon or text code printed on the label that represents the service level, used by UPS Operations for quick visual identification of the service type.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable (1-4 characters or black square symbol)
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** "1+" (Express Plus), "1" (Express), "1 S" (Express Saturday), "1P" (Saver), "2" (Expedited), "2A" (2nd Day Air A.M.), "2 S" (2nd Day Saturday), "3" (3 Day Select), "Black Square" (Ground/Standard), "+S" (with additional indicators)
- **Required:** yes

## Examples from Spec
- "1+" (UPS Express Plus)
- "1" (UPS Express)
- "1 S" (UPS Express Saturday Delivery)
- "1P" (UPS Saver)
- "2" (UPS Expedited / 2nd Day Air)
- "2A" (2nd Day Air A.M.)
- "3" (3 Day Select)
- "Black Square" (UPS Ground / UPS Standard)
- "+S" (shown on Premier Platinum label with COD)

## Position on Label
Displayed prominently on the label, typically in the service/routing area.

## Edge Cases & Notes
- UPS Ground and UPS Standard use a "Black Square" rather than text.
- Saturday delivery variants append " S" to the base icon.
- The icon visually corresponds to the service level for rapid sortation.

## Claude Confidence
HIGH — spec provides comprehensive tables mapping service icons to services.

## Review Status
- [ ] Reviewed by human