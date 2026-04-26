# Field: handling_feature_codes

## Display Name
Handling Feature Codes (HFCs)

## Field Description
Codes representing handling-relevant product features that impact sorting and/or delivery processes. These are translated from commercial Product and Service Codes and printed in reverse video format (white text on black background), left-aligned in the handling feature segment. Only handling-relevant features appear on the label.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable — typically 3 characters per code
- **Pattern/Regex:** Not specified in spec — codes derived from DHL reference data
- **Allowed Values:** Defined by DHL's reference data translation from Product/Service Codes (e.g., "DTP" from service code "DD")
- **Required:** conditional — mandatory when defined through Service Codes

## Examples from Spec
- "DTP" — handling feature code translated from service code "DD"

## ZPL Rendering
- **Typical Position:** handling feature segment, printed left-aligned
- **Font / Size:** Reverse video format (white text on black background)
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field) with ^FR (field reverse) or ^GB (graphic box) background

## Edge Cases & Notes
- Must be printed per Global Standard when defined through Service Codes.
- Product features that are not handling-relevant appear only on accompanying documentation (EDI, pickup/delivery lists), not on the label.
- The translation from commercial products/services to handling codes is based on DHL's reference data.
- Multiple HFCs can appear simultaneously.
- In the routing barcode, handling feature codes are encoded as a 3-digit numeric sum of feature values with leading zeroes.

## Claude Confidence
HIGH — clearly defined with rendering requirements (reverse video) and examples

## Review Status
- [ ] Reviewed by human