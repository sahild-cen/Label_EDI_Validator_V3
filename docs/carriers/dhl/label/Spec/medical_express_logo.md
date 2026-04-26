# Field: medical_express_logo

## Display Name
Medical EXPRESS Logo

## Field Description
A heart shape with a pulse line logo that identifies Medical Express shipments containing life-saving commodities (vaccines, medicines) and/or temperature-sensitive items. Placed adjacent to (above) the scannable Piece Identifier barcodes to ensure visibility to operations teams. This logo is unique to Medical Express shipments to serve as a distinct priority signal.

## Format & Validation Rules
- **Data Type:** graphic/image
- **Length:** N/A
- **Pattern/Regex:** N/A
- **Allowed Values:** DHL-approved graphical file (heart shape with pulse line); must comply with Corporate Branding guidelines
- **Required:** conditional — required for Medical Express shipments only

## Examples from Spec
No textual examples; logo is a heart with pulse line graphic.

## ZPL Rendering
- **Typical Position:** adjacent to (above) the Piece Identifier barcodes
- **Font / Size:** Minimum area 15x15 mm²; original proportions must be maintained
- **Field Prefix:** None — graphic element
- **ZPL Command:** ^GFA (graphic field) or ^IM (image recall)

## Edge Cases & Notes
- Must not impact or overlap necessary quiet zones of adjacent barcodes.
- The logo is available as an approved graphical file for operational use.
- Minimum 15x15mm² must be complied with.

## Claude Confidence
HIGH — clearly specified with size requirements and positioning rules

## Review Status
- [ ] Reviewed by human