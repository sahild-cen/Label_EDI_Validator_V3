# Field: description_of_goods

## Display Name
Description of Goods (DESC)

## Field Description
A general description of the contents of the shipment, required for customs and regulatory purposes.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** conditional — appears on shipments that are not documents-only

## Examples from Spec
- `DESC: TOOLS`
- `DESC: AUTO PARTS`
- `DESC: ART`
- `DESC: DOCUMENT`
- `DESC: FABRIC`

## Position on Label
Below the billing line and documentation indicator, in the lower portion of the label.

## Edge Cases & Notes
Prefixed with "DESC:". Even document-only shipments may include a description (e.g., "DESC: DOCUMENT"). The Movement Reference Number (MRN) prints beneath the description of goods when present.

## Claude Confidence
HIGH — shown on multiple label examples with various descriptions

## Review Status
- [x] Reviewed by human