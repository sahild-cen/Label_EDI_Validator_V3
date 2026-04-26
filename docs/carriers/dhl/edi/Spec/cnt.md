# Field: CNT

## Display Name
Control Totals

## Segment ID
CNT

## Required
yes

## Description
To provide control totals. Used at message header level (gross weight, total packages, volume) and at SG25 shipment level (transport units for LBBX).

## Subfields

### control_total_type_code_qualifier
- **Element Position:** 1.1
- **Pattern/Regex:** (7|11|15|56)
- **Required:** yes
- **Description:** Control total type code qualifier. '7' = Gross Weight (max 1 decimal), '11' = Total number of Packages (max 3 decimals, cannot exceed 999), '15' = Cube/Volume, '56' = Total number of transport units (LBBX purposes, SG25 level only).

### control_total_value
- **Element Position:** 1.2
- **Pattern/Regex:** \d{1,18}
- **Required:** yes
- **Description:** Control total value. Max 18 digits. Decimal sign may be point or comma per UNA segment.

### measurement_unit_code
- **Element Position:** 1.3
- **Pattern/Regex:** (KGM|LBR|MTQ|CMQ|INQ)?
- **Required:** no
- **Description:** Measurement unit code. With '7': 'KGM' or 'LBR'. With '15': 'MTQ', 'CMQ', or 'INQ'. Not used with '11' or '56'. Confirm with DHL Express which units are supported in origin country.

## Edge Cases & Notes
At message header level, total volume ('15') is required for shipments with destination outside shipper country. It can be provided here or dimensions per item can be provided in GID segment. Maximum pieces cannot exceed 999. At SG25 level, qualifier '56' is used for LBBX customer controlled solution.

## Claude Confidence
HIGH — spec clearly defines all qualifier values and units

## Review Status
- [ ] Reviewed by human