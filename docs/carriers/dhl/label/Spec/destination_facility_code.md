# Field: destination_facility_code

## Display Name
Destination Facility Code

## Field Description
The complete DHL Facility Code of the DHL Facility that will manage the delivery, consisting of Country Code, Service Area Code, and Facility Code.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable (format: CC-SSS-FFF where CC=2 chars, SSS=3 chars, FFF=3 chars, total up to 11 with hyphens)
- **Pattern/Regex:** `[A-Z]{2}-[A-Z0-9]{3}-[A-Z0-9]{3}` (full format) or `[A-Z]{2}-[A-Z0-9]{3}` (partial when facility code unavailable)
- **Allowed Values:** Values from DHL's Global Reference Databases
- **Required:** yes — mandatory (but may be partial if facility code not available)

## Examples from Spec
"SG-SIN" given as an example for Service Area Singapore when no DHL Facility Code has been specified.

## Position on Label
Center portion of the Manual Sorting Section (element 11).

## Edge Cases & Notes
- Composed of: Country Code (2-digit capital letters per ISO 3166) + hyphen + DHL Service Area Code (3-digit capital letters or numerals) + hyphen + DHL Facility Code (3-digit capital letters or numerals)
- Depends on destination country, postal location type (e.g., post code), and product
- When a DHL Facility Code has not been specified or an address cannot be matched with Geo Location Coordinates in GREF, only Country Code and Service Area Code are printed (separated by hyphen)

## Claude Confidence
HIGH — spec provides clear structure, example, and fallback rules

## Review Status
- [ ] Reviewed by human