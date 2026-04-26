# Field: ship_to_address

## Display Name
Ship-To Address

## Group Description
The destination address block containing the consignee name, phone number, UPS Access Point name (if applicable), and full address of the delivery location. Prefixed with "SHIP TO:" on the label.

## Sub-Fields

### consignee_name
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Name of the person to whom the package is being shipped. For UPS Access Point, this is the person who will pick up the package.
- **Detect By:** spatial:ship_to, text_prefix:SHIP TO:, first line after SHIP TO label
- **Position on Label:** center-left area of label, ship-to section
- **ZPL Font:** 10 pt. (standard labels)
- **Field Prefix:** "SHIP TO:" label appears to the left
- **ZPL Command:** ^FD (text field)

### consignee_phone_number
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Phone number of the consignee/recipient
- **Detect By:** spatial:ship_to, line below consignee name
- **Position on Label:** center-left area, within ship-to block
- **ZPL Font:** 10 pt.
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### uap_name
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Name of the UPS Access Point location
- **Detect By:** spatial:ship_to, labeled as "UPS ACCESS POINT (UAP) NAME"
- **Position on Label:** center-left area, within ship-to block
- **ZPL Font:** 10 pt.
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### uap_extended_address
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — only if additional address line exists for UAP
- **Description:** Extended address line for the UPS Access Point location
- **Detect By:** spatial:ship_to
- **Position on Label:** center-left area, within ship-to block
- **ZPL Font:** 10 pt.
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### uap_street_address
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Street address of the UPS Access Point location
- **Detect By:** spatial:ship_to
- **Position on Label:** center-left area, within ship-to block
- **ZPL Font:** 10 pt.
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### company_name
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — when shipping to a company
- **Description:** Company name at the destination
- **Detect By:** spatial:ship_to
- **Position on Label:** center-left area, within ship-to block
- **ZPL Font:** 10 pt.
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### extended_address
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** no
- **Description:** Extended address line(s) for destination
- **Detect By:** spatial:ship_to
- **Position on Label:** center-left area, within ship-to block
- **ZPL Font:** 10 pt.
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### street_address
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Street address of the destination
- **Detect By:** spatial:ship_to
- **Position on Label:** center-left area, within ship-to block
- **ZPL Font:** 10 pt.
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### city_postal_code
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** City, state (if applicable), and postal code of the destination. Printed in 12 pt. bold for UPS Access Point labels.
- **Detect By:** spatial:ship_to
- **Position on Label:** center-left area, within ship-to block
- **ZPL Font:** 12 pt. bold (postal line)
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### country
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Country name of the destination. Printed in 12 pt. bold for UPS Access Point labels.
- **Detect By:** spatial:ship_to
- **Position on Label:** center-left area, within ship-to block
- **ZPL Font:** 12 pt. bold
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Examples from Spec
```
SHIP TO:
CONSIGNEE NAME
CONSIGNEE PHONE NUMBER
UPS ACCESS POINT (UAP) NAME
UAP EXTENDED ADDRESS
UAP STREET ADDRESS
WINDSOR ON  N8N2M1
CANADA
```
Also:
```
SHIP TO:
CONSIGNEE NAME
CONSIGNEE PHONE NUMBER
COMPANY NAME
EXTENDED ADDRESS
STREET ADDRESS
41460  NEUSS
GERMANY
```

## Edge Cases & Notes
- For UPS Access Point shipments, the ship-to section contains the UAP address (where the package physically goes), while the consignee address block at the bottom shows where the recipient lives.
- Postal code line and country are printed in 12 pt. bold, larger than other ship-to lines (10 pt.).
- Consignee name is the person picking up, who may need to produce ID verification.

## Claude Confidence
HIGH — Spec clearly defines ship-to section requirements with multiple examples.

## Review Status
- [x] Reviewed by human