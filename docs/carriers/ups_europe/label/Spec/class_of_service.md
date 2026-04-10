# Field: class_of_service

## Display Name
Class of Service

## Field Description
A 3-digit numeric code identifying the UPS service level for the shipment (e.g., ground, express, etc.). This is encoded in the MaxiCode primary message.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 3 digits
- **Pattern/Regex:** `^[0-9]{3}$`
- **Allowed Values:** UPS service level codes (e.g., 001, 066)
- **Required:** yes

## Examples from Spec
- `001` (appears in multiple MaxiCode examples)
- `066` (international example to Germany)

## Position on Label
Encoded within MaxiCode primary message. Also represented in the tracking number (service level indicator positions).

## ZPL Rendering
- **Typical Position:** Encoded within MaxiCode
- **Font / Size:** Not specified
- **Field Prefix:** None
- **ZPL Command:** Encoded within ^BD (MaxiCode)

## Edge Cases & Notes
- The class of service and shipper number fields in the 1Z number are omitted in the MaxiCode tracking number field to avoid duplication.
- The class of service is part of the MaxiCode primary message along with postal code and country code.

## Claude Confidence
HIGH — spec clearly defines the field with examples in multiple MaxiCode data strings

## Review Status
- [ ] Reviewed by human