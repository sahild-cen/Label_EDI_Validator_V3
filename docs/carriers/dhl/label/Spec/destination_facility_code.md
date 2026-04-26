# Field: destination_facility_code

## Display Name
Destination Facility Code

## Field Description
The complete DHL Facility Code of the DHL facility that will manage the delivery. It is the central element of the Manual Sorting Section, composed of Country Code, Service Area Code, and Facility Code.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable (format: XX-XXX-XXX, up to 11 characters with hyphens)
- **Pattern/Regex:** [A-Z]{2}-[A-Z0-9]{3}(-[A-Z0-9]{3})?
- **Allowed Values:** Values from DHL's Global Reference databases; depends on destination country, postal location type, and product
- **Required:** yes — though the facility code portion may be omitted if not available

## Examples from Spec
"SG-SIN" for Service Area Singapore (when only Country Code and Service Area Code are available, without Facility Code). Full format: Country Code (2 letters) - Service Area Code (3 chars) - Facility Code (3 chars).

## ZPL Rendering
- **Typical Position:** manual sorting section, center element (element 11)
- **Font / Size:** Not specified in extracted text
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
Consists of three parts separated by hyphens: Country Code (ISO 3166, 2 capital letters), Service Area Code (3 capital letters or numerals), and Facility Code (3 capital letters or numerals). If a Facility Code has not been specified or an address cannot be matched with Geo Location Coordinates in GREF, only Country Code and Service Area Code are printed (e.g., "SG-SIN").

## Claude Confidence
HIGH — well-documented with format and examples in section 5.9.2

## Review Status
- [ ] Reviewed by human