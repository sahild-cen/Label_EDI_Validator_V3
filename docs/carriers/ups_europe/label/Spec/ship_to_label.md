# Field: ship_to_label

## Display Name
Ship To Label

## Field Description
The "SHIP TO:" label text that introduces the consignee address block on the label.

## Format & Validation Rules
- **Data Type:** string
- **Length:** 8 characters
- **Pattern/Regex:** `SHIP\s+TO:`
- **Allowed Values:** "SHIP TO:"
- **Required:** yes

## Examples from Spec
"SHIP TO:"

## Position on Label
Middle section of the label, as a header for the ship-to address block.

## ZPL Rendering
- **Typical Position:** Middle-left area, header of ship-to block
- **Font / Size:** Not specified
- **Field Prefix:** None — this is itself the label text
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Consistently shown on all label examples.

## Claude Confidence
HIGH — consistently shown on all examples

## Review Status
- [ ] Reviewed by human