# Field: ship_to_label_indicator

## Display Name
Ship To Label Indicator

## Field Description
The text "SHIP TO:" printed to the left of the destination address block to clearly identify the consignee address.

## Format & Validation Rules
- **Data Type:** string
- **Length:** 8 characters ("SHIP TO:")
- **Pattern/Regex:** `^SHIP\s*TO:?$`
- **Allowed Values:** "SHIP TO:" (may be displayed on two lines as "SHIP" and "TO:")
- **Required:** yes

## Examples from Spec
- `SHIP TO:`

## Position on Label
To the left of the Ship To address block.

## Edge Cases & Notes
- Font Size = 10 pt. bold
- In label samples, appears split across two lines: "SHIP" on top and "TO:" below

## Claude Confidence
HIGH — clearly called out as a requirement in the address block section

## Review Status
- [ ] Reviewed by human