# Field: ups_service_title

## Display Name
UPS Service Title

## Field Description
The complete service name printed in uppercase letters, identifying the UPS service used for the shipment.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Complete service titles such as "UPS EXPRESS", "UPS EXPRESS PLUS", "UPS SAVER", "UPS EXPEDITED", "UPS STANDARD", "UPS EXPRESS FREIGHT", "UPS EXPRESS 12:00", "UPS EXPRESS FREIGHT MIDDAY"
- **Required:** yes

## Examples from Spec
"UPS EXPRESS", "UPS SAVER", "UPS EXPRESS FREIGHT", "UPS EXPRESS 12:00"

## Position on Label
Left-justified, beneath the top highlight bar of the tracking number barcode block.

## ZPL Rendering
- **Typical Position:** Middle area, below top highlight bar, left-justified
- **Font / Size:** Font Size = 12 pt. bold
- **Field Prefix:** None — plain text data
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Must be printed in uppercase letters using the complete service title.

## Claude Confidence
HIGH — spec clearly defines font size, position, and content requirements

## Review Status
- [ ] Reviewed by human