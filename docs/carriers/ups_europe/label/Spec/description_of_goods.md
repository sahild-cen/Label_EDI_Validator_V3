# Field: description_of_goods

## Display Name
Description of Goods (DESC)

## Field Description
A text description of the contents/commodities being shipped in the package.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — appears on international shipment labels

## Examples from Spec
- `DESC: COMPUTER EQUIPMENT`
- `DESC: LASER PRINTER`
- `DESC: CALCULATORS`

## Position on Label
Located in the lower portion of the Carrier Segment, below the billing indicator.

## ZPL Rendering
- **Typical Position:** Bottom area of carrier segment
- **Font / Size:** 10pt
- **Field Prefix:** "DESC:"
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
- Appears on labels shown for international shipments.
- Content should accurately describe the package contents.

## Claude Confidence
MEDIUM — spec shows examples in label samples but does not provide detailed format rules

## Review Status
- [ ] Reviewed by human