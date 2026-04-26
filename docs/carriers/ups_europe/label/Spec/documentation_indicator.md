# Field: documentation_indicator

## Display Name
Documentation Indicator

## Group Description
Documentation indicators combined with the RS indicator must be used for UPS Returns as noted.

## Sub-Fields

### service_title
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** KEY-RS EDI EDI PULL INV-RS
- **Required:** yes
- **Description:** Documentation indicators combined with the RS indicator must be used for UPS Returns as noted.
- **Detect By:** below the highlight bar of the Tracking Number Barcode Block
- **Position on Label:**  right-justified in the Additional Routing Instructions Block immediately below the highlight bar of the Tracking Number Barcode Block.
- **ZPL Font:** 16 pt. bold
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Examples from Spec
```
 KEY-RS
```
```
 EDI
```
```
 EDI PULL
```

## Edge Cases & Notes

## Claude Confidence
HIGH — spec explicitly defines font size, positioning, and formatting requirements.

## Review Status
- [x] Reviewed by human