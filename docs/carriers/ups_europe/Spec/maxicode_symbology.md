# Field: maxicode_symbology

## Display Name
MaxiCode™ Symbology

## Field Description
A 2D barcode symbology that contains shipment detail information. It is one of the five key data elements on a UPS Smart Label and is used for routing and tracking purposes.

## Format & Validation Rules
- **Data Type:** barcode (2D MaxiCode)
- **Length:** variable
- **Pattern/Regex:** Not specified in spec (see Appendix A for full specifications)
- **Allowed Values:** Mode 2 for U.S. destinations, Mode 3 for non-U.S. destinations
- **Required:** yes

## Examples from Spec
No detailed data content examples in extracted spec text. Spec references Appendix A for full MaxiCode specifications.

## Position on Label
Carrier segment. The Postal Barcode prints to the right of the MaxiCode™ Symbology, implying MaxiCode is on the left side of the middle area of the carrier segment.

## Edge Cases & Notes
- MaxiCode data string should not contain any punctuation.
- Ensure that both the MaxiCode™ data string and the Postal Barcode have identical postal codes.
- Some label creation software providers and printer manufacturers have interpreted Mode 2 for U.S. destinations and Mode 3 for non-U.S. destinations exclusively.

## Claude Confidence
HIGH — spec clearly identifies MaxiCode as one of five key elements and references detailed specs in Appendix A

## Review Status
- [x] Reviewed by human