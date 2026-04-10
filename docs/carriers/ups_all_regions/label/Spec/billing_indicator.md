# Field: billing_indicator

## Display Name
Billing Indicator

## Field Description
Indicates the billing method for the shipment, identifying who pays for shipping charges.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** `BILLING: [A-Z/]+`
- **Allowed Values:** `P/P` (Prepaid), `F/D` (Free Domicile), `F/C` (Freight Collect)
- **Required:** yes

## Examples from Spec
- `BILLING: P/P`

## Position on Label
Printed in the label area below the tracking number/service icon section.

## Edge Cases & Notes
For UPS Economy DDP: valid billing options are P/P, F/D, and F/C (via Shipper or Third Party Payor). For UPS Economy DDU: valid billing options are P/P and F/C (via Shipper or Third Party Payor). F/D is not valid for DDU shipments.

## Claude Confidence
HIGH — Shown on multiple label samples with specific allowed values per service type.

## Review Status
- [ ] Reviewed by human