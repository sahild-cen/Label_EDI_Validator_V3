# Field: service_indicator

## Display Name
Service Indicator

## Field Description
A two-character alphanumeric code that identifies the specific UPS service type. This is the Service Level Indicator portion of the 1Z tracking number and is used to derive the MaxiCode Class of Service.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 2 characters
- **Pattern/Regex:** `[A-Z0-9]{2}`
- **Allowed Values:** Specific codes per service, examples: YZ (Access Point Economy), Z0 (Delivery Confirmation), Z3 (Signature Required), Z4 (Adult Sig Required), Z6 (COD), Z1, Z2, Z5, Z7 (Returns), EA (example), 67 (Expedited example)
- **Required:** yes

## Examples from Spec
From Access Point Economy tables:
- YZ = UPS Access Point Economy
- Z0 = Delivery Confirmation
- Z3 = Delivery Confirmation with Signature Required
- Z4 = Delivery Confirmation Adult Signature Required
- Z6 = UPS Access Point Economy (Electronic COD)
- Z1 = Delivery Confirmation (Electronic COD)
- Z2 = Delivery Confirmation with Signature Required (Electronic COD)
- Z5 = Delivery Confirmation Adult Signature Required (Electronic COD)
- Z7 = Print Return Label, Print and Mail, Electronic Return Label

## Position on Label
Encoded within the 1Z tracking number (positions 9-10). Not displayed separately as human-readable text.

## Edge Cases & Notes
- The service indicator is embedded in the tracking number and used to calculate the MaxiCode Class of Service value.
- Different indicators exist for the same base service depending on whether COD or Returns options are selected.

## Claude Confidence
HIGH — Comprehensive tables provided for Access Point Economy service indicators.

## Review Status
- [x] Reviewed by human