# Field: service_type

## Display Name
Service Type / Service Name

## Field Description
The UPS service level selected for the shipment, displayed as a text banner on the label indicating the speed and type of delivery service.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Enumerated list includes:
  - UPS EXPRESS
  - UPS EXPEDITED
  - UPS SAVER
  - UPS EXPRESS PLUS
  - UPS STANDARD
  - UPS GROUND
  - UPS NEXT DAY AIR
  - UPS NEXT DAY AIR EARLY
  - UPS NEXT DAY AIR SAVER
  - UPS 2ND DAY AIR
  - UPS 2ND DAY AIR AM
  - UPS 3 DAY SELECT
  - UPS EXPRESS 1200
  - UPS SUREPOST
  - UPS EXPRESS FREIGHT
  - UPS AIR FREIGHT DIRECT
  - UPS Access Point Economy
  - UPS Today Standard
  - UPS Today Dedicated Courier
  - UPS Today Express
  - UPS Today Express Saver
  - UPS Worldwide Express Freight
  - UPS Worldwide Express Freight Midday
- **Required:** yes

## Examples from Spec
- `UPS EXPRESS`
- `UPS EXPEDITED`
- `UPS SAVER`
- `UPS EXPRESS PLUS`
- `UPS STANDARD`
- `UPS GROUND`
- `UPS NEXT DAY AIR`
- `UPS NEXT DAY AIR EARLY`
- `UPS SUREPOST`
- `UPS EXPRESS FREIGHT`
- `UPS AIR FREIGHT DIRECT`

## Position on Label
Displayed prominently as a banner/bar in the middle section of the label, typically above the tracking number.

## Edge Cases & Notes
Service codes are also defined for internal use: 1DA, EAM, 1DS, 2DA, 2DM, 3DS, EXM, GND, LCO, TDT, TDC, TDE, TDS (domestic); EXD, EXP, EXS, EAM, WFP, WFM (international). The display name on the label differs from the internal code.

## Claude Confidence
HIGH — Service types and codes are clearly enumerated in the spec tables on page 45.

## Review Status
- [ ] Reviewed by human