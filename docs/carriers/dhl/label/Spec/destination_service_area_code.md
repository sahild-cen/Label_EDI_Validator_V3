# Field: destination_service_area_code

## Display Name
Destination Service Area Code

## Field Description
A DHL-specific code identifying the destination service area or delivery facility. This is a critical routing element used for sorting and routing packages to the correct destination station within the DHL network. Often displayed prominently on the label.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 3 characters
- **Pattern/Regex:** ^[A-Z]{3}$
- **Allowed Values:** DHL-defined destination service area codes
- **Required:** yes

## Examples from Spec
No examples in extracted spec text.

## ZPL Rendering
- **Typical Position:** prominent routing area, often large font in upper-right or center-right
- **Font / Size:** Large bold font for sort/routing visibility
- **Field Prefix:** None — displayed as standalone routing identifier
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
This code is critical for DHL hub and station sorting operations. It is determined by DHL's routing tables based on the destination postal code and service type.

## Claude Confidence
MEDIUM — known DHL routing element

## Review Status
- [ ] Reviewed by human