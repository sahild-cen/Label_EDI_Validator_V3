# Field: maxicode_class_of_service

## Display Name
MaxiCode™ Class of Service

## Field Description
A three-digit numeric value encoded in the MaxiCode data string that identifies the specific UPS service level for the shipment. Derived from the 1Z Service Level Indicator.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 3 digits
- **Pattern/Regex:** `[0-9]{3}`
- **Allowed Values:** Specific values per service, including: 991, 992, 993, 994, 995, 996, 997, 998, 999 (for Access Point Economy variants), 426 (example for service level EA), and many others derivable from the conversion table
- **Required:** yes (within MaxiCode data string)

## Examples from Spec
- Service indicator EA → Class of Service 426 (E=416 + A=10)
- UPS Access Point Economy: 991
- UPS Access Point Economy with Delivery Confirmation: 992
- UPS Access Point Economy with Signature Required: 995
- UPS Access Point Economy with Adult Signature Required: 996
- UPS Access Point Economy COD: 998
- UPS Access Point Economy Returns: 999

## Position on Label
Encoded within the MaxiCode barcode; not displayed as human-readable text on its own.

## Edge Cases & Notes
- Calculated from the two-character 1Z Service Level Indicator by looking up each character's decimal value and summing them.
- First character value = position × 32 (e.g., E=416, Z=992). Second character value is simply 0-31.
- If the Class of Service value is less than 100, no conversion takes place (backward compatibility).
- Separate class of service codes exist for standard, COD, and returns variants of Access Point Economy.

## Claude Confidence
HIGH — Detailed conversion tables and examples provided in Appendix A and Access Point Economy section.

## Review Status
- [x] Reviewed by human