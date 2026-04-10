# Field: maxicode_symbology

## Display Name
MaxiCode™ Symbology

## Field Description
A 2D barcode symbology that contains the shipment detail. It is one of the five key data elements on the UPS Smart Label that enables efficient processing by technologies in the delivery network.

## Format & Validation Rules
- **Data Type:** barcode (2D - MaxiCode)
- **Length:** variable (per MaxiCode encoding rules)
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Mode 2 for U.S. destinations, Mode 3 for non-U.S. destinations (though some software providers interpret this exclusively)
- **Required:** yes

## Examples from Spec
No explicit data string examples provided. The spec notes: "Some label creation software providers and printer manufacturers have interpreted Mode 2 for U.S. destinations and Mode 3 for non-U.S. destinations exclusively."

## Position on Label
Located in the Carrier Segment, to the left of the UPS Routing Code and Postal Barcode. The Postal Barcode prints to the right of the MaxiCode™ Symbology.

## ZPL Rendering
- **Typical Position:** Middle area of carrier segment, left side
- **Font / Size:** Not specified (barcode element)
- **Field Prefix:** None — barcode
- **ZPL Command:** ^BD (MaxiCode)

## Edge Cases & Notes
- MaxiCode data string should not contain any punctuation.
- Ensure that both the MaxiCode™ data string and the Postal Barcode have identical postal codes.
- See Appendix A for full MaxiCode™ specifications.
- Mode 2 vs Mode 3 interpretation varies by software provider.

## Claude Confidence
HIGH — spec clearly identifies MaxiCode as a key data element with mode specifications and placement rules

## Review Status
- [ ] Reviewed by human