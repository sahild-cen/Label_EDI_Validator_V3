# Field: service_indicator

## Display Name
Service Indicator

## Group Description
A two-character alphanumeric code embedded in the tracking number (positions 9-10 of the 1Z number) that identifies the specific UPS service and options selected.

## Sub-Fields

### service_indicator_code
- **Data Type:** alphanumeric
- **Length:** 2
- **Pattern/Regex:** ^[A-Z0-9]{2}$
- **Allowed Values:** YZ (AP Economy), Z0 (AP Economy Delivery Confirmation), Z3 (AP Economy DC Signature Required), Z4 (AP Economy DC Adult Signature Required), Z6 (AP Economy COD), Z1 (AP Economy COD DC), Z2 (AP Economy COD DC Signature Required), Z5 (AP Economy COD DC Adult Signature Required), Z7 (AP Economy Returns), EA (example from conversion table = 426), 66, C7, 67, and others per service tables
- **Required:** yes
- **Description:** Two-character code identifying the UPS service level, embedded in the tracking number and used to derive the MaxiCode Class of Service value
- **Detect By:** Extracted from tracking number positions 9-10 (after "1Z" + 6-char account)
- **Position on Label:** embedded within tracking number
- **ZPL Font:** Not applicable (part of tracking number)
- **Field Prefix:** None
- **ZPL Command:** Not applicable (embedded in tracking number data)

## Examples from Spec
Service indicators from Access Point Economy tables:
- YZ = UPS Access Point Economy (Class of Service 991)
- Z0 = Delivery Confirmation (993)
- Z3 = DC Signature Required (995)
- Z4 = DC Adult Signature Required (996)
- Z6 = COD (998)
- Z7 = Returns (999)

## Edge Cases & Notes
- The service indicator can be converted to/from a 3-digit MaxiCode Class of Service code using the character value lookup table provided in Appendix A.
- Conversion formula: First character value (from table) + Second character value = Class of Service decimal.

## Claude Confidence
MEDIUM — Spec provides detailed tables for Access Point Economy but only partial coverage of all service indicators.

## Review Status
- [x] Reviewed by human