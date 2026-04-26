# Field: service_type

## Display Name
UPS Service Title

## Group Description
The UPS service level name displayed prominently on the label, indicating the type of shipping service used.

## Sub-Fields

### service_title
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** "UPS EXPRESS", "UPS EXPEDITED", "UPS ACCESS POINT ECONOMY", "UPS Domestic Standard", "UPS Domestic Express", "UPS Domestic Express Plus", "UPS Domestic Express Saver", "UPS Worldwide Express", "UPS Worldwide Express Plus", "UPS Worldwide Expedited", "UPS Worldwide Express Saver", "UPS Worldwide Standard", "UPS Transborder Standard", "UPS Transborder Express", "UPS Transborder Express Plus", "UPS Transborder Express Saver", "UPS Express NA1", "UPS Express 12:00", "UPS Worldwide Express Freight", and variants with package type suffixes (Letters/Envelopes, 10 KG Box, 25 KG Box, Express Box, Tube, PAK, GNIFC)
- **Required:** yes
- **Description:** The UPS service name. Font size is reduced to 12 pt. bold for UPS Access Point labels.
- **Detect By:** spatial:service_section, prominent text in service area of label
- **Position on Label:** center-right area, near the tracking barcode section
- **ZPL Font:** 12 pt. bold (UPS Access Point labels; standard size not specified for other labels)
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Examples from Spec
```
UPS EXPRESS
UPS EXPEDITED
UPS ACCESS POINT ECONOMY
```

## Edge Cases & Notes
- Font size is explicitly reduced to 12 pt. bold for UPS Access Point labels.
- Service titles can include package type suffixes (e.g., "Letters/Envelopes", "10 KG Box").
- The full list of service titles is defined in the Shipment Summary section of the manifest spec.

## Claude Confidence
HIGH — Spec explicitly lists service titles and font size requirements.

## Review Status
- [x] Reviewed by human