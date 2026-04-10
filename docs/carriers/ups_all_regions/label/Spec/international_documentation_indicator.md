# Field: international_documentation_indicator

## Display Name
International Documentation Indicator

## Field Description
A text indicator printed on the label to alert UPS Operations about the documentation status of an international shipment, particularly whether it is a paperless shipment, has additional customs documents, or uses image upload services.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable (3-10 characters)
- **Pattern/Regex:** `^(EDI|EDI-PULL|EDI-IDIS|EDI-CCP|EDI-IDIS-RS|EDI-RS|EDI-RS1|EDI-RS3)$`
- **Allowed Values:**
  - "EDI" — invoice is the only customs document required
  - "EDI-PULL" — additional customs documents included with the shipment
  - "EDI-IDIS" — additional customs documents uploaded to International Document Imaging System
  - "EDI-CCP" — paperless shipment is UPS World Ease™
  - "EDI-IDIS-RS" — paperless returns/Import Control with additional documents uploaded to IDIS
  - "EDI-RS" — UPS Paperless Returns and Import Control Shipment
  - "EDI-RS1" — UPS Paperless Returns and Import Control Shipment
  - "EDI-RS3" — UPS Paperless Returns and Import Control Shipment
- **Required:** conditional — required when using UPS Paperless Invoice, international image uploads, or paperless returns

## Examples from Spec
- "EDI" (shown on UPS Express Plus 4x6 label)
- "EDI-IDIS" (shown on UPS Saver paperless label, International Forms Image Upload labels)
- "EDI-PULL" (shown on Paperless Shipment with Additional Customs Documents label)

## Position on Label
Prints on the label in the area below the tracking number / service type area. Visible in the Additional Routing Instructions area.

## Edge Cases & Notes
- Font Size = 16 pt. bold for all indicators.
- EDI-IDIS is used both for UPS Paperless Invoice with additional IDIS documents AND for International Forms Image Upload.
- Multiple label examples show this indicator in different contexts (paperless invoice, image upload, returns).

## Claude Confidence
HIGH — spec provides explicit enumeration of all allowed values with descriptions.

## Review Status
- [ ] Reviewed by human