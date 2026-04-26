# Field: ship_from_address

## Display Name
Ship From Address (Consignor's Address)

## Field Description
The "Ship From" section refers to the Consignor's Address. It supports identification by the carrier (e.g., for Pickup) as well as the Consignee. It does not necessarily reflect the return address in case of failed delivery. If approved by DHL, a deviating address may be printed here.

## Required
yes — though noted as part of the standard label, the spec describes it as a core section

## ZPL Rendering
- **Typical Position:** upper-left area of label, with the word "From" in upper left corner of this section
- **Font / Size:** Relative small font, allowing space to the right for optional Customer Logo

## Subfields

### name
- **Pattern/Regex:** .{1,47}
- **Required:** yes
- **Detect By:** spatial:ship_from, preceded by "From" label
- **Description:** Shipper company or person name (Address line 1: Receiver Company / Name in compact version)

### address_line_1
- **Pattern/Regex:** .{1,47}
- **Required:** yes
- **Description:** First line of street address. Each line contains a pre-defined maximum of up to 47 characters.

### address_line_2
- **Pattern/Regex:** .{1,47}
- **Required:** no
- **Description:** Additional address line (e.g., building name, floor number, county). Overall number of lines must not exceed 7.

### city
- **Pattern/Regex:** .{1,47}
- **Required:** yes
- **Description:** City name

### state
- **Pattern/Regex:** .{1,47}
- **Required:** conditional — depends on country postal format
- **Description:** State, province, suburb, or equivalent postal location format element

### postal_code
- **Pattern/Regex:** .{1,47}
- **Required:** conditional — depends on country postal format
- **Description:** Postal code or equivalent postal location format identifier

### country_code
- **Pattern/Regex:** [A-Z]{2}
- **Required:** conditional — must be used whenever available; follows ISO 3166 two-character standard
- **Description:** ISO 3166 two-character country code, used as a quick reference for DHL services

### country_name
- **Pattern/Regex:** .{1,47}
- **Required:** conditional — optional for domestic shipments; mandatory for cross-border shipments if ISO 3166 code is missing
- **Description:** Country name written in its own line. For domestic pieces may be in local language; for cross-border must be in English (may be followed by local translation).

## Edge Cases & Notes
Maximum of 7 address lines for consistency with DHL's data structure. Each line maximum 47 characters (highest value). For international shipments, the Country Name shall be written in its own line. The word "From" must appear in the upper left corner; for international shipments, the English word "From" must appear (may include local language separated by "/"). For Highly-Compact labels, the number of Sender Address lines can be limited to 5 (from 7) upon formal DHL approval. If approved by DHL, a deviating address may be printed instead of the actual consignor's address.

## Claude Confidence
HIGH — well-documented in sections 5.4 and 5.4.1

## Review Status
- [ ] Reviewed by human