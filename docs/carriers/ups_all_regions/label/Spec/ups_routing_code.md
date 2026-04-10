# Field: ups_routing_code

## Display Name
UPS Routing Code

## Field Description
The UPS routing code for the import site, used on World Ease labels. For over-labels, it prints alongside the postal barcode. For single labels, it appears in the import site box.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Values from URC (UPS Routing Code) file
- **Required:** yes — on World Ease labels

## Examples from Spec
- "ESP 285 4-40" (from label example context)
- "DEU 510 9-00" (from label example context)

## Position on Label
Must print to the right of the MaxiCode symbology (on over-labels). On single labels, appears in the Import Site Box below "UPS WORLD EASE" text. Font Size = 16 pt. bold.

## Edge Cases & Notes
Must reflect the UPS import site information. The routing code can be found in the URC file. For single labels, the import site box has two rows: top = "UPS WORLD EASE", bottom = UPS Routing Code for the import site.

## Claude Confidence
HIGH — spec describes placement and source; examples visible in label diagrams

## Review Status
- [ ] Reviewed by human