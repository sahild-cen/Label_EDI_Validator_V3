# Field: maxicode_class_of_service

## Display Name
MaxiCode Class of Service

## Field Description
A three-digit numeric code used within the MaxiCode barcode to identify the UPS service level. This value is encoded in the MaxiCode data but may not be visually displayed as text.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 3 characters
- **Pattern/Regex:** `\d{3}`
- **Allowed Values:** Enumerated list including: 054, 481, 485, 034, 484, 488, 346, 495, 489, 347, 496, 490, 066, 387, 388, 069, 390, 391, 004, 393, 394, 067, 399, 400, 068, 402, 403, 477, 478, 479, 752, 748, 749, 073, 482, 486, 483, 487, 075, 358, 359, 076, 361, 362, 077, 368, 369, 079, 374, 376, 497, 498, 499, 740, 746, 747, 840, 841, 847, 848, 853, 854, 858, 860
- **Required:** yes — required for MaxiCode encoding

## Examples from Spec
- `054` (UPS Express Plus)
- `066` (UPS Express)
- `004` (UPS Saver)
- `067` (UPS Expedited)
- `068` (UPS Standard)
- `346` (UPS Express NA1)
- `752` (UPS Express 12:00)
- `840` (UPS Today Standard)

## Position on Label
Encoded within the MaxiCode barcode data; not displayed as separate text.

## ZPL Rendering
- **Typical Position:** Encoded within MaxiCode barcode
- **Font / Size:** Not applicable — encoded in barcode
- **Field Prefix:** None — barcode data
- **ZPL Command:** ^BD (MaxiCode) — part of the MaxiCode data content

## Edge Cases & Notes
Different class of service codes exist for COD lead packages vs. non-COD/child packages. For example, UPS Express non-COD = 066 but UPS Express COD lead = 075. The class of service value must match the service indicator and service icon.

## Claude Confidence
HIGH — comprehensively enumerated in multiple tables in the spec

## Review Status
- [ ] Reviewed by human