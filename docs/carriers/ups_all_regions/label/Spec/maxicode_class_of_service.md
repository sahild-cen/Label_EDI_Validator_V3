# Field: maxicode_class_of_service

## Display Name
MaxiCode Class of Service

## Field Description
A numeric code used within the MaxiCode barcode to identify the specific UPS service and options for the shipment. This code is encoded in the MaxiCode symbology on the label.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 3 characters
- **Pattern/Regex:** `[0-9]{3}`
- **Allowed Values:** 417-426 (Express Freight), 439-448 (Express Freight Midday), 459 (Economy DDP), 460 (Economy DDU), 866-872 (Proactive Response US/Intl), 969, 975 (Proactive Response Saturday), 744 (Express 12:00), 435-437 (Premium Care Returns)
- **Required:** yes

## Examples from Spec
- `417` — UPS Express Freight
- `439` — UPS Express Freight Midday
- `459` — UPS Economy DDP
- `460` — UPS Economy DDU
- `866` — UPS Next Day Air Early (Proactive Response)
- `867` — UPS Next Day Air (Proactive Response)
- `868` — UPS Express (Proactive Response)
- `744` — UPS Express 12:00

## Position on Label
Encoded within the MaxiCode barcode on the label.

## Edge Cases & Notes
Each combination of base service plus options (Saturday Delivery, Delivery Confirmation, Import Control, etc.) has its own unique class of service code. UPS Express 12:00 (744) is only offered in Germany (DE to DE).

## Claude Confidence
HIGH — Comprehensive tables with explicit numeric codes provided.

## Review Status
- [ ] Reviewed by human