# Field: consignee_final_address

## Display Name
Final Consignee Address (Access Point D2R/D2A)

## Group Description
For UPS Access Point shipments, the final consignee/recipient address is printed separately from the ship-to (Access Point location) address. This block is marked with "D2R" (Direct to Retail) or "D2R/D2A" indicator and shows where the package is ultimately intended for.

## Sub-Fields

### consignee_name
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — required for Access Point shipments
- **Description:** Final consignee name for the package
- **Detect By:** spatial:lower_label, appears in Access Point label lower section
- **Position on Label:** lower-center, below billing/desc section
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### extended_address
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — present when additional address detail is needed
- **Description:** Extended address lines for the final consignee
- **Detect By:** spatial:lower_label
- **Position on Label:** lower-center, below consignee name
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### d2r_d2a_indicator
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** `^D2R(/D2A)?$`
- **Allowed Values:** "D2R", "D2R/D2A"
- **Required:** conditional — required for Access Point shipments
- **Description:** Indicator showing Direct to Retail (D2R) or Direct to Retail/Direct to Address (D2R/D2A) delivery mode
- **Detect By:** text_match:D2R
- **Position on Label:** lower-center, inline with or near extended address
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### street_address
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — required for Access Point shipments
- **Description:** Street address of the final consignee
- **Detect By:** spatial:lower_label
- **Position on Label:** lower-center
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### city_postal_code
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — required for Access Point shipments
- **Description:** City and postal code of the final consignee
- **Detect By:** spatial:lower_label
- **Position on Label:** lower-center
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### country_name
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — required for Access Point shipments
- **Description:** Country name of the final consignee
- **Detect By:** spatial:lower_label
- **Position on Label:** lower-center, last line of final consignee block
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

### uap_barcode_id
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** `^U\d{2}\s\d{3}\s\d{3}$`
- **Allowed Values:** Not restricted
- **Required:** conditional — appears on some Access Point Economy labels
- **Description:** UPS Access Point identifier code (e.g., "U90 123 456") shown in the final consignee block
- **Detect By:** text_match:U90, spatial:lower_label
- **Position on Label:** lower-center, within consignee address block
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Examples from Spec
- "CONSIGNEE NAME / EXTENDED ADDRESS D2R / EXTENDED ADDRESS / STREET ADDRESS / CITY POSTAL CODE / COUNTRY NAME"
- "CONSIGNEE NAME / EXTENDED ADDRESS D2R/D2A / EXTENDED ADDRESS / STREET ADDRESS / CITY POSTAL CODE / COUNTRY NAME"
- With UAP code: "CONSIGNEE NAME / EXTENDED ADDRESS D2R / EXTENDED ADDRESS / STREET ADDRESS / U90 123 456 / CITY POSTAL CODE / COUNTRY NAME"

## Edge Cases & Notes
- This block only appears on UPS Access Point labels (Direct to Retail, Direct to Address variants).
- The "D2R" or "D2R/D2A" indicator appears inline with the extended address line.
- Some Access Point Economy labels include a UAP identifier code (U90 format).

## Claude Confidence
MEDIUM — Examples are clear but the spec doesn't provide explicit field-by-field definitions; inferred from label examples.

## Review Status
- [x] Reviewed by human