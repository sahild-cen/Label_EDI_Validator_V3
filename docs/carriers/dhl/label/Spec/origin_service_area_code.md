# Field: origin_service_area_code

## Display Name
Origin Service Area Code

## Field Description
A DHL-specific code identifying the origin service area or facility. This code is used for routing and operational sorting within the DHL network. It typically corresponds to the origin station or gateway.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 3 characters
- **Pattern/Regex:** ^[A-Z]{3}$
- **Allowed Values:** DHL-defined service area codes (e.g., station/gateway codes)
- **Required:** yes

## Examples from Spec
No examples in extracted spec text.

## ZPL Rendering
- **Typical Position:** routing code area, often near destination service area code
- **Font / Size:** Not specified
- **Field Prefix:** May appear as part of a routing code string
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
This code is assigned by DHL's routing system and is not user-specified. It may appear as part of a larger routing string on the label.

## Claude Confidence
LOW — known DHL field but no detail in extracted spec

## Review Status
- [ ] Reviewed by human