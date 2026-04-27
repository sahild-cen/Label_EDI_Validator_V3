# Field: urc_version_number

## Display Name
URC Version Number

## Field Description
The version number of the UPS Routing Code data file used to generate the routing code. Indicates which version of the routing data table was used.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- `18.5A 01/2020`

## Position on Label
Bottom of the label, below the description of goods area in the Carrier segment. Font size = 6 pt.

## Edge Cases & Notes
- The URC data file must be updated monthly. This version number helps identify the currency of routing data.

## Claude Confidence
MEDIUM — shown on label samples with font size specified but format details are limited in extracted text

## Review Status
- [x] Reviewed by human