# Field: ship_from_address

## Display Name
Ship-From Address

## Group Description
The shipper/sender address block, left-justified at the top of the shipping label. Contains the origin address information for the package.

## Sub-Fields

### contact_name
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Contact name of the shipper/sender
- **Detect By:** spatial:ship_from, first line of ship-from address block
- **Position on Label:** top-left of label
- **ZPL Font:** 8pt (approximately ^A0N,20,20)
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### phone_number
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Phone number of the shipper/sender
- **Detect By:** spatial:ship_from, second line of ship-from address block
- **Position on Label:** top-left of label, below contact name
- **ZPL Font:** 8pt
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### company_name
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Company name of the shipper/sender
- **Detect By:** spatial:ship_from
- **Position on Label:** top-left of label, below phone number
- **ZPL Font:** 8pt
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### extended_address
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — when applicable
- **Description:** Extended address line (suite, floor, etc.) of the shipper
- **Detect By:** spatial:ship_from
- **Position on Label:** top-left of label, below company name
- **ZPL Font:** 8pt
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### street_address
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Street address of the shipper; must print directly above the postal code line
- **Detect By:** spatial:ship_from
- **Position on Label:** top-left of label, below extended address
- **ZPL Font:** 8pt
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### postal_code_line
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec — see Appendix F for country-specific postal code line configurations
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Postal code line containing city, state/province/county and postal code on the same line. ZIP+4 codes must be used if available.
- **Detect By:** spatial:ship_from
- **Position on Label:** top-left of label, below street address
- **ZPL Font:** 8pt
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### country
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Country name of the shipper
- **Detect By:** spatial:ship_from
- **Position on Label:** top-left of label, below postal code line
- **ZPL Font:** 8pt
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Examples from Spec
```
CONTACT NAME
PHONE NUMBER
COMPANY NAME
EXTENDED ADDRESS
STREET ADDRESS
POSTAL CODE LINE
COUNTRY
```

## Edge Cases & Notes
- All uppercase characters required
- Punctuation is not recommended; if punctuation must be used, validate with destination postal authority
- Standard abbreviations should be employed (including 2-letter state or province abbreviations)
- Left-justified at the top of the shipping label
- Phone number is optional when shipping to/from the European Union (EU)
- Country, contact name, and phone number are required except when origin and destination country are the same

## Claude Confidence
HIGH — spec clearly defines address block requirements, font sizes, and positioning rules

## Review Status
- [x] Reviewed by human