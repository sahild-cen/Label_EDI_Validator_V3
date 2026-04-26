# Field: maxicode

## Display Name
MaxiCode

## Group Description
A 2D barcode symbology used on UPS labels that encodes shipping address elements, tracking information, and optionally customer data. Uses Mode 2 for US destinations (numeric postal codes up to 9 digits) and Mode 3 for non-US destinations (alphanumeric postal codes up to 6 characters).

## Sub-Fields

### ship_to_postal_code
- **Data Type:** alphanumeric
- **Length:** 1-9 (variable); 5 or 9 numeric for US (Mode 2), 6 alphanumeric for non-US (Mode 3)
- **Pattern/Regex:** Mode 2 (US): `^\d{5}(\d{4})?$`; Mode 3 (non-US): `^[A-Za-z0-9]{1,6}$` (padded with trailing spaces if shorter than 6)
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Destination postal code. Encode without spaces or special characters (e.g., no dashes). Must match the postal barcode value. If country has no postal code, leave empty. Pad with trailing spaces if below minimum length; truncate from right if exceeding max.
- **Detect By:** barcode_data: first field after format header "01<GS>96" in MaxiCode secondary message
- **Position on Label:** MaxiCode symbol area (typically upper-right of label)
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^BD (MaxiCode barcode)

### ship_to_iso_country_code
- **Data Type:** numeric
- **Length:** 3
- **Pattern/Regex:** `^\d{3}$`
- **Allowed Values:** ISO 3166 numeric country codes (e.g., 840 = US, 276 = Germany)
- **Required:** yes
- **Description:** Three-digit ISO 3166 numeric country code for the ship-to destination.
- **Detect By:** barcode_data: field after postal code in MaxiCode data string
- **Position on Label:** MaxiCode symbol area
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^BD (MaxiCode barcode)

### class_of_service
- **Data Type:** numeric
- **Length:** 3
- **Pattern/Regex:** `^\d{3}$`
- **Allowed Values:** UPS service codes (e.g., 001, 066)
- **Required:** yes
- **Description:** Three-digit UPS class of service code identifying the shipping service level.
- **Detect By:** barcode_data: field after country code in MaxiCode data string
- **Position on Label:** MaxiCode symbol area
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^BD (MaxiCode barcode)

### tracking_number
- **Data Type:** alphanumeric
- **Length:** 10
- **Pattern/Regex:** Not specified in spec (note: class of service and shipper number omitted from this field to avoid duplication with full 1Z number)
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** 10-character tracking number portion encoded in MaxiCode. The class of service and shipper number fields from the full 1Z number are omitted to avoid duplication.
- **Detect By:** barcode_data: field after class of service in MaxiCode data string
- **Position on Label:** MaxiCode symbol area
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^BD (MaxiCode barcode)

### ups_scac
- **Data Type:** string
- **Length:** 4
- **Pattern/Regex:** `^UPSN$`
- **Allowed Values:** "UPSN"
- **Required:** yes
- **Description:** Standard Carrier Alpha Code for UPS. Always "UPSN".
- **Detect By:** barcode_data: field after tracking number in MaxiCode data string
- **Position on Label:** MaxiCode symbol area
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^BD (MaxiCode barcode)

### ups_account_number
- **Data Type:** alphanumeric
- **Length:** 6
- **Pattern/Regex:** `^[A-Za-z0-9]{6}$`
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Six-character UPS shipper account number.
- **Detect By:** barcode_data: field after SCAC in MaxiCode data string
- **Position on Label:** MaxiCode symbol area
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^BD (MaxiCode barcode)

### julian_day_of_pickup
- **Data Type:** numeric
- **Length:** 3
- **Pattern/Regex:** `^\d{3}$`
- **Allowed Values:** 001-366
- **Required:** yes
- **Description:** Julian day (day of year) when the package is picked up.
- **Detect By:** barcode_data: field after account number in MaxiCode data string
- **Position on Label:** MaxiCode symbol area
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^BD (MaxiCode barcode)

### shipment_id_number
- **Data Type:** alphanumeric
- **Length:** 1-30 (variable)
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** no (optional)
- **Description:** Optional shipment identification number. If omitted, a <GS> placeholder must still be provided. This field can be cleared to reduce data length if MaxiCode exceeds maximum capacity.
- **Detect By:** barcode_data: field after julian day in MaxiCode data string
- **Position on Label:** MaxiCode symbol area
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^BD (MaxiCode barcode)

### package_n_of_x
- **Data Type:** alphanumeric
- **Length:** 3-7 (variable, format N/X where N and X are 1-3 digits each)
- **Pattern/Regex:** `^\d{1,3}/\d{1,3}$`
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Package number N of X total packages in the shipment. The "/" character must be encoded to separate N and X.
- **Detect By:** barcode_data: field after shipment ID in MaxiCode data string
- **Position on Label:** MaxiCode symbol area
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^BD (MaxiCode barcode)

### package_weight
- **Data Type:** numeric
- **Length:** 1-3
- **Pattern/Regex:** `^\d{1,3}$`
- **Allowed Values:** Minimum 1 (pound or kilogram); blank for Letters/Envelopes unless weight meets published threshold; blank if weight exceeds max characters (e.g., UPS Worldwide Express Freight)
- **Required:** yes (conditional — leave blank for Letters/Envelopes)
- **Description:** Package weight rounded up to the next whole pound or kilogram. Must be at least 1 unless package type is Letter or Envelope. Leave blank for Letters/Envelopes and for weights exceeding maximum character limit.
- **Detect By:** barcode_data: field after package N/X in MaxiCode data string
- **Position on Label:** MaxiCode symbol area
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^BD (MaxiCode barcode)

### address_validation
- **Data Type:** alphabetic
- **Length:** 1
- **Pattern/Regex:** `^[YN]$`
- **Allowed Values:** "Y" or "N"
- **Required:** yes
- **Description:** Set to "Y" when the delivery address has been compared to a USPS CASS-certified database. Set to "N" otherwise.
- **Detect By:** barcode_data: field after package weight in MaxiCode data string
- **Position on Label:** MaxiCode symbol area
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^BD (MaxiCode barcode)

### ship_to_address
- **Data Type:** alphanumeric
- **Length:** 1-35 (full street address) or 1-10<FS>1-8 (primary/secondary address format)
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Ship-to street address. Use format (an 1...35) for full street address line 1 (may be truncated at character limit). Use format (an 1...10<FS>an 1...8) for CASS-certified addresses with secondary address (e.g., suite number) — primary address number, <FS> separator, secondary address number. The secondary format requires Address Validation = "Y".
- **Detect By:** barcode_data: field after address validation in MaxiCode data string
- **Position on Label:** MaxiCode symbol area
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^BD (MaxiCode barcode)

### ship_to_city
- **Data Type:** alphanumeric
- **Length:** 1-20
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Ship-to city name.
- **Detect By:** barcode_data: field after ship-to address in MaxiCode data string
- **Position on Label:** MaxiCode symbol area
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^BD (MaxiCode barcode)

### ship_to_state_province
- **Data Type:** alphabetic
- **Length:** 2
- **Pattern/Regex:** `^[A-Za-z]{2}$`
- **Allowed Values:** US state abbreviations, Canadian province codes, or other applicable codes
- **Required:** conditional — required for US/applicable countries; some non-US destinations will not have a state or province (leave as placeholder)
- **Description:** Two-character state or province code for the ship-to destination. Some non-US destinations may not have a state/province value.
- **Detect By:** barcode_data: last field before <RS><EOT> in MaxiCode data string
- **Position on Label:** MaxiCode symbol area
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^BD (MaxiCode barcode)

### customer_data
- **Data Type:** alphanumeric
- **Length:** variable (limited by ~100 character MaxiCode capacity minus other fields)
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Data Identifier format (e.g., "10K" + invoice number) or Application Identifier format (e.g., "400" + PO number)
- **Required:** no (optional)
- **Description:** Additional customer data such as purchase order or invoice numbers, added after the main transportation data using Data Identifiers (format header "06<GS>") or Application Identifiers (format header "05<GS>"). Available space depends on how many optional fields are used.
- **Detect By:** barcode_data: additional format segment after main transportation data in MaxiCode
- **Position on Label:** MaxiCode symbol area
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^BD (MaxiCode barcode)

## Examples from Spec
**Example 1 (Validated Address):**
`[)><RS>01<GS>96303281483<GS>840<GS>001<GS>1Z12345675<GS>UPSN<GS>1X2X3X<GS>187<GS><GS>1/1<GS>37<GS>Y<GS>123<FS>567<GS>ATLANTA<GS>GA<RS><EOT>`

**Example 2 (Non-validated with customer data):**
`[)><RS>01<GS>96841706672<GS>840<GS>001<GS>1Z12345675<GS>UPSN<GS>1X2X3X<GS>187<GS><GS>1/1<GS>10<GS>N<GS>19 SOUTH ST<GS>SALT LAKE CITY<GS>UT<RS><EOT>`

Customer data using Data Identifiers: `06<GS>10K123456789<RS><EOT>`
Customer data using Application Identifiers: `05<GS>400123456789<RS><EOT>`

**Example 3 (International — Germany):**
`[)><RS>01<GS>9651147<GS>276<GS>066<GS>1Z12345679<GS>UPSN<GS>1X2X3X<GS>187<GS><GS>1/1<GS>10<GS>N<GS>5 WALDSTRASSE<GS>COLOGNE<GS><RS><EOT>`

**Example 4 (Letter/Envelope — weight blank):**
`[)><RS>01<GS>96841706672<GS>840<GS>001<GS>1Z12345675<GS>UPSN<GS>1X2X3X<GS>187<GS><GS>1/1<GS><GS>N<GS>1 MAIN ST<GS>SALT LAKE CITY<GS>UT<RS><EOT>`

## Edge Cases & Notes
- MaxiCode holds approximately 100 characters of data. If data exceeds maximum length: (1) clear the Shipment ID Number field first (saves ~11 characters), (2) if still too long, shorten the Ship-To Address field (delete only characters needed, not entire field).
- Non-printable characters: <GS> = decimal 29, <RS> = decimal 30, <FS> = decimal 28, <EOT> = decimal 4.
- Mode 2 is for US destinations (numeric postal codes); Mode 3 is for non-US destinations (alphanumeric postal codes). Some software interprets this as Mode 2 = US only, Mode 3 = non-US only.
- For all-numeric postal codes, use Mode 2 with up to 9 characters; truncate from right if longer.
- Printer manufacturers may rearrange the primary message (Postal Code, Country Code, Class of Service) order or separate primary/secondary messages differently.
- The primary message consists of Postal Code, Country Code, and Class of Service. The secondary message contains headers and all remaining 11 data fields.
- The <FS> separator for primary/secondary address numbers is only allowed for CASS-certified (uncompressed MaxiCode) addresses.

## Claude Confidence
HIGH
Spec provides detailed field-by-field data string format, multiple examples with encoded strings, and comprehensive notes on encoding rules.

## Review Status
- [x] Reviewed by human