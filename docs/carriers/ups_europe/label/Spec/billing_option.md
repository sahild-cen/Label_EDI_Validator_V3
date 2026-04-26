# Field: billing_option

## Display Name
Billing Option (BILLING:)

## Field Description
A text description of the contents/commodities being shipped in the package.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- `BILLING: P/P*`
- `BILLING: FOB`
- `BILLING: F/C BILL RECEIVER`
- `BILLING: C/F`
- `BILLING: SDV`
- `BILLING: F/D`
- `BILLING: T/P`

## Position on Label
The billing option must print directly below the highlight bar, at the top of Description of Goods section.

## ZPL Rendering
- **Typical Position:** Bottom area of carrier segment
- **Font / Size:** 10pt
- **Field Prefix:** "BILLING:"
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
- Appears on labels shown for international shipments.

## Claude Confidence
MEDIUM — spec shows examples in label samples but does not provide detailed format rules

## Review Status
- [x] Reviewed by human