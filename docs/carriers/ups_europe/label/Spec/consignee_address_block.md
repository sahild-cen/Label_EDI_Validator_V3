# Field: consignee_address_block

## Display Name
Consignee Address Block (UPS Access Point)

## Group Description
A separate address block at the very bottom of UPS Access Point labels showing the actual consignee's (recipient's) home/delivery address, distinct from the UPS Access Point ship-to address. This block is bounded by horizontal lines.

## Sub-Fields

### consignee_name
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** Yes
- **Description:** Name of the consignee/recipient (the person the package is intended for)
- **Detect By:** spatial:bottom_of_label, within horizontal line boundaries
- **Position on Label:** very bottom of label, below routing code area
- **ZPL Font:** 10 pt. bold
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### extended_address
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** no
- **Description:** Extended address line for the consignee
- **Detect By:** spatial:bottom_of_label
- **Position on Label:** very bottom of label, within consignee address block
- **ZPL Font:** 10 pt.
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### street_address
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Street address of the consignee
- **Detect By:** spatial:bottom_of_label
- **Position on Label:** very bottom of label, within consignee address block
- **ZPL Font:** 10 pt.
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### city_postal_code
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** City and postal code of the consignee
- **Detect By:** spatial:bottom_of_label
- **Position on Label:** very bottom of label, within consignee address block
- **ZPL Font:** 10 pt.
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### country
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Country name of the consignee
- **Detect By:** spatial:bottom_of_label
- **Position on Label:** very bottom of label, last line of consignee address block
- **ZPL Font:** 10 pt.
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Examples from Spec
```
CONSIGNEE NAME
EXTENDED ADDRESS
EXTENDED ADDRESS
STREET ADDRESS
CITY POSTAL CODE
COUNTRY NAME
```
And from 4x4.25 second label:
```
HOLD AT UPS ACCESS POINT FOR:
CONSIGNEE NAME
EXTENDED ADDRESS
EXTENDED ADDRESS
STREET ADDRESS
CITY POSTAL CODE
COUNTRY NAME
```

## Edge Cases & Notes
- This block is specific to UPS Access Point labels. It is bounded by horizontal lines (minimum 0.03 inches) placed above the consignee name and below the country.
- The consignee name is 10 pt. bold; all other lines are 10 pt. regular.
- On 4x4.25 second labels, this block is preceded by "HOLD AT UPS ACCESS POINT FOR:" in 10 pt. bold.
- The consignee may be required to produce verification of name/address for pickup.

## Claude Confidence
HIGH — Spec explicitly describes this block with font sizes and formatting rules.

## Review Status
- [x] Reviewed by human