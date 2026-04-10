# Field: shipper_address

## Display Name
Shipper Address (From Address)

## Field Description
The full street address of the shipment origin/sender, including street, city, state/province, postal code, and country.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable, multiple lines (typically up to 3 address lines of 35-45 characters each)
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
No examples in spec.

## Position on Label
In the shipper/origin address block, typically in the upper-left or left portion of the label.

## Edge Cases & Notes
International shipments require country name to be spelled out. The address format follows the conventions of the origin country.

## Claude Confidence
HIGH — Standard required element on all DHL labels.

## Review Status
- [ ] Reviewed by human