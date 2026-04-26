# Field: service_title

## Display Name
UPS Service Title

## Group Description
The UPS service name printed on the label indicating the level of service selected, displayed in uppercase bold text beneath the top highlight bar.

## Sub-Fields

### service_title
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Complete UPS service titles including: UPS EXPRESS PLUS, UPS EXPRESS, UPS EXPRESS (NA1), UPS SAVER, UPS EXPEDITED, UPS STANDARD, UPS 3 DAY SELECT, UPS EXPRESS FREIGHT, UPS EXPRESS FREIGHT MIDDAY, UPS EXPRESS 12:00
- **Required:** yes
- **Description:** The complete UPS service title printed in uppercase bold letters
- **Detect By:** spatial:above tracking barcode, below top highlight bar
- **Position on Label:** Left-justified beneath the top highlight bar
- **ZPL Font:** 12 pt. bold
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Examples from Spec
```
UPS EXPRESS
```
```
UPS SAVER
```
```
UPS EXPRESS FREIGHT
```
```
UPS EXPRESS 12:00
```

## Edge Cases & Notes
- Must be printed in uppercase letters using the complete service title.
- Font size is 12 pt. bold.
- Left-justified beneath the top highlight bar of the tracking number barcode block.

## Claude Confidence
HIGH — spec explicitly defines font size, positioning, and formatting requirements.

## Review Status
- [x] Reviewed by human