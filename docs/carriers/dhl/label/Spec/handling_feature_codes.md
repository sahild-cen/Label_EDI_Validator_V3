# Field: handling_feature_codes

## Display Name
Handling Feature Codes (HFC)

## Field Description
Codes representing handling-relevant product features that impact sorting and/or delivery processes. These are translated from commercial Product and Service Codes and printed in reverse video format on the label.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 3 numeric digits in routing barcode (fixed length, with leading zeroes); variable display on label
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Sum of values of product features; "000" when no features are chosen. Examples include "DTP" displayed on label.
- **Required:** conditional — mandatory when defined through Service Codes

## Examples from Spec
- "DTP" displayed on label in reverse video
- "000" when no features chosen
- "001" for Customs Clearance
- "081" = sum of 1+16+64 (multiple features combined)
- "002" example in routing barcode

## Position on Label
Printed left-aligned in the handling feature segment, in reverse video format. Located in the product features area of the label.

## Edge Cases & Notes
- Only handling-relevant features appear on the label; non-handling features appear only on accompanying documentation (EDI, pickup/delivery lists)
- In the routing barcode, the feature code is always 3 digits with leading zeroes
- The feature code in the routing barcode is a sum of individual feature code values
- Translation from commercial products/services to handling codes is based on DHL's reference data

## Claude Confidence
HIGH — spec clearly defines these codes with examples and placement rules

## Review Status
- [ ] Reviewed by human