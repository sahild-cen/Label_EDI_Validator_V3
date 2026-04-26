# Field: handling_service_logos

## Display Name
Handling-relevant Service Logos

## Field Description
Visual logos/icons displayed on the label to indicate specific handling-relevant services, such as the Medical EXPRESS Logo. These support DHL internal operational procedures and visual identification of special handling requirements.

## Format & Validation Rules
- **Data Type:** graphic/image
- **Length:** N/A
- **Pattern/Regex:** N/A
- **Allowed Values:** DHL-defined service logos (e.g., Medical EXPRESS Logo)
- **Required:** conditional — displayed when applicable services are selected

## Examples from Spec
"Medical EXPRESS Logo" specifically mentioned in section 5.10.4.1.

## ZPL Rendering
- **Typical Position:** product features section
- **Font / Size:** N/A — graphic element
- **Field Prefix:** None
- **ZPL Command:** ^GFA (graphic field)

## Edge Cases & Notes
The Medical EXPRESS Logo is specifically called out as a service logo type. Other handling-relevant service logos may exist but are not enumerated in the extracted text.

## Claude Confidence
MEDIUM — section headers visible but detail limited in extracted text

## Review Status
- [ ] Reviewed by human