# Field: service_indicator

## Display Name
Service Indicator

## Field Description
A two-character alphanumeric code embedded within the tracking number that identifies the specific UPS service and any associated service options (e.g., Saturday delivery, delivery confirmation, import control).

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 2 characters
- **Pattern/Regex:** `[A-Z0-9]{2}`
- **Allowed Values:** E1, E2, E3, E4, E5, E6, E7, E8, E9, EA (Express Freight); EQ, ER, ES, ET, EV, EW, EX, EY, EZ, F0 (Express Freight Midday); FC (Economy DDP), FD (Economy DDU); V2, V3, V4, V5, V6, V8 (Proactive Response); Q8 (Express 12:00); Y9, YG (Proactive Response Saturday); EM, EL, EN (Premium Care Returns); and others per tables
- **Required:** yes

## Examples from Spec
- `E1` — UPS Express Freight
- `EQ` — UPS Express Freight Midday
- `FC` — UPS Economy DDP
- `FD` — UPS Economy DDU
- `V2` — UPS Next Day Air Early (Proactive Response)
- `V3` — UPS Next Day Air (Proactive Response)
- `V4` — UPS Express (Proactive Response)
- `V5` — UPS Express Plus (Proactive Response)
- `V6` — UPS Saver (Proactive Response)
- `V8` — UPS Express NA1 (Proactive Response)
- `Q8` — UPS Express 12:00

## Position on Label
Encoded within the tracking number (positions 8-9 of the 1Z number) and used in MaxiCode encoding.

## Edge Cases & Notes
Service indicators vary based on combinations of base service and options like Saturday Delivery, Delivery Confirmation Signature Required, Delivery Confirmation Adult Signature Required, Import Control/Return Service, and 1 Pickup Attempt. Saturday Delivery is only valid in US and Canada.

## Claude Confidence
HIGH — Comprehensive tables provided in the spec with clear mappings.

## Review Status
- [ ] Reviewed by human