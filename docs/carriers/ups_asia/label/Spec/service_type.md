# Field: service_type

## Display Name
Service Type / Service Title

## Field Description
The UPS service level name identifying the shipping service selected for the shipment.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** "UPS EXPRESS PLUS", "UPS EXPRESS", "UPS EXPRESS FREIGHT", "UPS EXPRESS FREIGHT MIDDAY", "UPS SAVER", "UPS EXPEDITED", "UPS NEXT DAY AIR" (and others per service table)
- **Required:** yes

## Examples from Spec
"UPS SAVER", "UPS EXPRESS", "UPS EXPEDITED", "UPS NEXT DAY AIR", "UPS EXPRESS PLUS", "UPS EXPRESS FREIGHT", "UPS EXPRESS FREIGHT MIDDAY"

## Position on Label
Middle-lower section of the label, prominently displayed above the tracking number.

## Edge Cases & Notes
The service table on page 33 lists service titles with corresponding service indicators, service icons, and class of service codes. The service title is the human-readable representation.

## Claude Confidence
HIGH — field appears consistently across all label examples with a defined service table

## Review Status
- [ ] Reviewed by human