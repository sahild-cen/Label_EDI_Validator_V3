# Field: TCC

## Display Name
Charge/Rate Calculations

## Segment ID
TCC

## Required
yes

## Description
Specifies charge and rate/tariff calculation details. This segment is only for internal use in DSV.

## Subfields

### freight_and_other_charges_description_identifier
- **Element Position:** 1.1
- **Pattern/Regex:** .{1,17}
- **Required:** no
- **Description:** Freight and other charges description identifier. Code values to be provided by local CargoLink country.

### code_list_identification_code_1
- **Element Position:** 1.2
- **Pattern/Regex:** N/A
- **Required:** no
- **Description:** Code list identification code (not used)

### code_list_responsible_agency_code_1
- **Element Position:** 1.3
- **Pattern/Regex:** N/A
- **Required:** no
- **Description:** Code list responsible agency code (not used)

### freight_and_other_charges_description
- **Element Position:** 1.4
- **Pattern/Regex:** .{1,26}
- **Required:** no
- **Description:** Freight and other charges description (future use)

### payment_arrangement_code
- **Element Position:** 1.5
- **Pattern/Regex:** (ZCN|ZCZ|ZDP|ZPW)
- **Required:** no
- **Description:** Payment arrangement code indicating which party pays. ZCN=Consignee, ZCZ=Consignor, ZDP=Delivery party, ZPW=Pickup party. Not used for Air or Courier.

### item_identifier
- **Element Position:** 1.6
- **Pattern/Regex:** N/A
- **Required:** no
- **Description:** Item identifier (not used)

### rate_or_tariff_class_description_code
- **Element Position:** 2.1
- **Pattern/Regex:** ZAC
- **Required:** no
- **Description:** Rate or tariff class description code. ZAC=Agreement Code

### code_list_identification_code_2
- **Element Position:** 2.2
- **Pattern/Regex:** N/A
- **Required:** no
- **Description:** Code list identification code for rate/tariff (not used)

### code_list_responsible_agency_code_2
- **Element Position:** 2.3
- **Pattern/Regex:** N/A
- **Required:** no
- **Description:** Code list responsible agency code for rate/tariff (not used)

### rate_or_tariff_class_description
- **Element Position:** 2.4
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Rate or tariff class description text

### commodity_rate_detail
- **Element Position:** 3
- **Pattern/Regex:** N/A
- **Required:** no
- **Description:** Commodity/rate detail composite (not used)

### rate_tariff_class_detail
- **Element Position:** 4
- **Pattern/Regex:** N/A
- **Required:** no
- **Description:** Rate/tariff class detail composite (not used)

## Edge Cases & Notes
TCC is mandatory within SG7 but SG7 is conditional. This segment is only for internal use in DSV. Example: TCC+100000:::Description:ZCN+ZAC:::Spotqb'

## Claude Confidence
MEDIUM — complex composite structure with many not-used elements; internal DSV use only

## Review Status
- [ ] Reviewed by human