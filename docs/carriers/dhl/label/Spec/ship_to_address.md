# Field: ship_to_address

## Display Name
Ship To Address (Consignee's Address)

## Field Description
The agreed Delivery Point address for the shipment. Each piece requires a Ship To address. This is a mandatory section and should be emphasized by adding hooks (thicker corners) around the address block.

## Required
yes

## ZPL Rendering
- **Typical Position:** prominent middle area of label, emphasized with hooks (4x4mm corner marks, line thickness > 0.5mm)
- **Font / Size:** Delivery Country and applicable Postal Location Format Elements (e.g., City and Postal Code) must be printed in bigger font

## Subfields

### name
- **Pattern/Regex:** .{1,47}
- **Required:** yes
- **Detect By:** spatial:ship_to, preceded by "To" label
- **Description:** Consignee company or person name

### address_line_1
- **Pattern/Regex:** .{1,47}
- **Required:** yes
- **Description:** First line of street address (e.g., Street Name, Street Number)

### address_line_2
- **Pattern/Regex:** .{1,47}
- **Required:** no
- **Description:** Additional address line (e.g., building name, floor number). Overall lines must not exceed 7.

### city
- **Pattern/Regex:** .{1,47}
- **Required:** yes
- **Description:** City name — must be printed in bigger font

### state
- **Pattern/Regex:** .{1,47}
- **Required:** conditional — depends on country postal format (e.g., Suburb, County, State)
- **Description:** State, province, suburb, or equivalent postal location format element

### postal_code
- **Pattern/Regex:** .{1,47}
- **Required:** conditional — depends on country postal format
- **Description:** Postal code — must be printed in bigger font along with city

### country_code
- **Pattern/Regex:** [A-Z]{2}
- **Required:** conditional — must be used whenever available
- **Description:** ISO 3166 two-character country code

### country_name
- **Pattern/Regex:** .{1,47}
- **Required:** conditional — mandatory for cross-border; must be printed in bigger font
- **Description:** Delivery country name — must be printed in bigger font. For cross-border must be in English.

## Edge Cases & Notes
The word "To" must appear; for export shipments the English word "To" must appear (may include local language separated by "/"). The Ship To address should be emphasized by adding hooks (thicker corners, recommended 4x4mm, line thickness > 0.5mm). Minimum of 5 lines must be offered; maximum 7 lines for consistency with DHL data structure. Delivery Country and Postal Location Format Elements (City, Postal Code) must be in bigger font. If space is lacking, city/postal code and country can be joined to one line each. For Highly-Compact version, can be reduced to 5 lines upon formal approval.

## Claude Confidence
HIGH — extensively documented in section 5.8

## Review Status
- [ ] Reviewed by human