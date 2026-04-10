# Field: ship_to_company_name

## Display Name
Ship To Company Name

## Field Description
The name of the company or business at the delivery destination.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — required when shipping to a business

## Examples from Spec
- `COMPANY NAME` (placeholder used throughout spec)
- `UPS CUSTOMS CLEARANCE` (for World Ease customs clearance shipments)

## Position on Label
Middle section of the label in the ship-to address block.

## Edge Cases & Notes
For UPS World Ease shipments with customs clearance routing, the company name may be "UPS CUSTOMS CLEARANCE" to indicate the package routes through UPS customs first.

## Claude Confidence
HIGH — Consistently present in all label examples.

## Review Status
- [ ] Reviewed by human