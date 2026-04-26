# Field: return_address

## Display Name
Return Address

## Field Description
The address to which the package should be returned if undeliverable. May be the same as the ship-from address or a designated return facility. Not always printed on every DHL label.

## Required
conditional — required when return service is selected or when different from shipper address

## ZPL Rendering
- **Typical Position:** upper-left area, may overlap or replace ship-from position
- **Font / Size:** Not specified in extracted spec

## Subfields

### name
- **Pattern/Regex:** .{1,45}
- **Required:** yes
- **Detect By:** spatial:return_address
- **Description:** Return-to company or person name

### address_line_1
- **Pattern/Regex:** .{1,45}
- **Required:** yes
- **Description:** First line of return street address

### address_line_2
- **Pattern/Regex:** .{1,45}
- **Required:** no
- **Description:** Second line of return street address

### city
- **Pattern/Regex:** .{1,35}
- **Required:** yes
- **Description:** Return city name

### state
- **Pattern/Regex:** [A-Za-z]{2,3}
- **Required:** conditional — required for US, CA, AU addresses
- **Description:** State or province code

### postal_code
- **Pattern/Regex:** .{1,12}
- **Required:** yes
- **Description:** Return ZIP or postal code

### country
- **Pattern/Regex:** [A-Z]{2}
- **Required:** conditional — required for international
- **Description:** ISO 2-letter country code

## Edge Cases & Notes
For DHL Express return labels, this field becomes the primary destination. Some DHL services do not require a separate return address if it matches the shipper address.

## Claude Confidence
LOW — standard field but no specific detail in extracted spec

## Review Status
- [ ] Reviewed by human