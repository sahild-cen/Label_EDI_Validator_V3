# Field: eei_indicator

## Display Name
Electronic Export Information (EEI) Indicator

## Field Description
An indicator required when asking UPS to complete an AES filing for a State Department License shipment, formerly known as SED (Shipper Export Declaration).

## Format & Validation Rules
- **Data Type:** string
- **Length:** 3 characters
- **Pattern/Regex:** `EEI`
- **Allowed Values:** "EEI"
- **Required:** conditional — required when UPS is completing AES filing for SDL shipments

## Examples from Spec
- `SDL/EEI/POA`

## Position on Label
In the additional routing instructions area, combined with other indicators separated by forward slashes.

## Edge Cases & Notes
Formerly known as SED (Shipper Export Declaration). When combined with SDL, POA, and/or CO, must be separated by forward slashes.

## Claude Confidence
HIGH — Clearly defined in the spec with format requirements.

## Review Status
- [ ] Reviewed by human