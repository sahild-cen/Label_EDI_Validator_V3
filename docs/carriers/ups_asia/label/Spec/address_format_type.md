# Field: address_format_type

## Display Name
Address Format Type

## Field Description
Determines the ordering of postal code, city, and state/province/county within the address line on the label. Format varies by destination country.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 1 character
- **Pattern/Regex:** `^[12]$`
- **Allowed Values:** 1 = "Postal Code, City, State/Province/County"; 2 = "City, State/Province/County, Postal Code"
- **Required:** yes — determined by destination country

## Examples from Spec
- Format 1 countries: Croatia (10000, City, State), Turkey, Ivory Coast, Mozambique, Namibia, Zimbabwe, Turkmenistan, Wallis and Futuna
- Format 2 countries: Indonesia (City, State, 40115), Nigeria (City, State, 930283), Norfolk Island (City, State, 2899)

## Position on Label
Determines layout of the postal code line within the consignee/destination address block.

## Edge Cases & Notes
- This is a formatting rule, not a printed field. It dictates how the address line is constructed.
- The full matrix in Appendix F covers all destination countries (only partial data extracted here).

## Claude Confidence
HIGH — Clearly defined with legend and multiple country examples.

## Review Status
- [ ] Reviewed by human