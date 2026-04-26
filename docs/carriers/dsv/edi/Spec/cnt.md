# Field: CNT

## Display Name
Control Total

## Segment ID
CNT

## Required
no

## Description
Specifies control totals for the shipment including gross weight, package quantity, volume, loading metres, and pallet spaces.

## Subfields

### control_total_type_code_qualifier
- **Element Position:** 1.1
- **Pattern/Regex:** (7|11|15|19|57)
- **Required:** yes
- **Description:** Control total type code qualifier (C270/6069). Valid codes: 7=Total gross weight, 11=Consignment package quantity, 15=Total consignment cube (volume), 19=Total reported quantity in supplementary units (pallet spaces), 57=Total loading metres.

### control_total_quantity
- **Element Position:** 1.2
- **Pattern/Regex:** n..18
- **Required:** yes
- **Description:** Control total quantity value (C270/6066). The numeric value for weight, package count, volume, loading metres, or pallet spaces.

### measurement_unit_code
- **Element Position:** 1.3
- **Pattern/Regex:** .{1,8}
- **Required:** no
- **Description:** Measurement unit code (C270/6411). For qualifier 7 use KGM (kilogram); for qualifier 11 use package type codes (EUR, PL, EU, BA, BG, BO, CA, CS, CL, CN, CP, CR, CT, DR, GI, HP, IB, IP, JC, LD, PD, PX, QP, RL, SB, UP, PCE, plus legacy codes); for qualifier 15 use MTQ (cubic metre); for qualifier 19 use PLL, HLP, or KPL; for qualifier 57 use MTR (metre).

## Edge Cases & Notes
CNT can occur up to 9 times. Not used for Air or Sea. For Road: Gross Weight at shipment level (CNT+7) or per line item (SG21 MEA) is required. Number of packages at shipment level (CNT+11) or per line item (SG19 GID) is required. At least one of volume (CNT+15), loading metres (CNT+57), per-item volume, per-item loading metres, or per-item dimensions is required. Qualifier 19 is only used with special agreement for pallet transport. PCE is valid with CNT+11 when multiple package types are used in GID. Examples: CNT+7:259.0:KGM', CNT+11:1:PCE', CNT+15:0.002:MTQ', CNT+57:9:MTR', CNT+19:1:PLL'.

## Claude Confidence
HIGH — spec provides detailed information across multiple CNT occurrences

## Review Status
- [ ] Reviewed by human