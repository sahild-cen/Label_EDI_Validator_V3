# Field: maxicode

## Display Name
MaxiCode

## Field Description
The MaxiCode 2D symbology printed on World Ease over-labels containing encoded shipping information including postal code, country code, service class, tracking number, account number, pickup date, weight, and address details.

## Format & Validation Rules
- **Data Type:** barcode (MaxiCode symbology)
- **Length:** variable (structured data string)
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Structured per MaxiCode data fields (see description)
- **Required:** yes — on World Ease over-labels

## Examples from Spec
No examples in spec (data string content described by field).

## Position on Label
Must print directly above the pre-printed "UPS World Ease™" text on the over-label.

## Edge Cases & Notes
MaxiCode data string fields: Ship To Postal Code (an 5 — import site postal code; for non-US codes, fixed length 6, pad with trailing spaces or truncate from right), Ship To ISO Country Code (n 3), Class of Service (n 3), Tracking Number (an 10 — tracking number of the package the over-label will be used on), UPS SCAC = "UPSN", UPS Account Number (an 6), Julian Day of Pickup (n 3), Shipment ID Number (an 30 — leave blank for over-label), Package in Shipment (n 1-3/n 1-3 — always "1/1" for over-label), Package Weight (n 1-3, rounded up, minimum 1 LB/KG; for document box populate with 1), Address Validation (a 1 — always "N"), Ship To Address (an 35 — leave blank), Ship To City (an 20 — import site city), Ship To State/Province/County (a 2 — conditional, required for Canada, Ireland, and United States). Full specifications referenced in UPS GTL Appendix A.

## Claude Confidence
HIGH — spec provides detailed field-by-field breakdown of MaxiCode data string

## Review Status
- [ ] Reviewed by human