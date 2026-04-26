# Field: import_point_of_entry_address

## Display Name
Import Point of Entry Address

## Field Description
The address of DHL's Import Clearance Gateway, printed on Loose BBX Transport Labels with the caption "IMPORT AT:". This address follows the same specifications as the shipper and receiver address segments.

## Required
conditional — mandatory for Loose BBX Transport Labels

## ZPL Rendering
- **Typical Position:** Customs routing address segment (segments 25-27 on Loose BBX labels)
- **Font / Size:** Same specifications as other address segments

## Subfields

### name
- **Pattern/Regex:** .{1,35}
- **Required:** yes
- **Detect By:** caption "IMPORT AT:"
- **Description:** DHL Import Clearance Gateway name

### address_line_1
- **Pattern/Regex:** .{1,35}
- **Required:** yes
- **Description:** First line of gateway address

### address_line_2
- **Pattern/Regex:** .{1,35}
- **Required:** no
- **Description:** Second line of gateway address

### city
- **Pattern/Regex:** .{1,30}
- **Required:** yes
- **Description:** City name

### state
- **Pattern/Regex:** .{1,10}
- **Required:** conditional
- **Description:** State or province code

### postal_code
- **Pattern/Regex:** .{1,12}
- **Required:** conditional — where postcode system exists
- **Description:** Postal code

### country
- **Pattern/Regex:** [A-Z]{2}
- **Required:** yes
- **Description:** ISO 2-letter country code

## Edge Cases & Notes
Only applicable to Loose BBX Transport Labels. Not present on standard transport labels.

## Claude Confidence
MEDIUM — described in the Loose BBX section but with less detail than main address blocks

## Review Status
- [ ] Reviewed by human