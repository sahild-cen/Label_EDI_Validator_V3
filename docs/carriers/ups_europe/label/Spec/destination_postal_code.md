# Field: destination_postal_code

## Display Name
Destination Postal Code

## Field Description
The postal code for the destination/consignee address. Format and length vary by destination country as defined in Appendix F. This field is used in both the human-readable address block and encoded in the MaxiCode barcode.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** Variable by country (e.g., 5 for Croatia/Turkey, 6 for Nigeria/Turkmenistan, 10 for Iran, 4 for Mozambique/Norfolk Island, or no postal code for some countries)
- **Pattern/Regex:** Country-dependent; see Appendix F matrix
- **Allowed Values:** Valid postal codes for the destination country
- **Required:** conditional — required for countries that use postal codes; some countries have no postal code system (indicated by "-" in length field)

## Examples from Spec
- Croatia: 10000 (5 digits)
- Cuba: 20305 (5 digits)
- Indonesia: 40115 (5 digits)
- Iran: 1193653471 (10 digits)
- Mozambique: 1100 (4 digits)
- Nigeria: 930283 (6 digits)
- Norfolk Island: 2899 (4 digits)
- Turkey: 01960 (5 digits)
- Turkmenistan: 744000 (6 digits)
- Wallis and Futuna: 98600 (5 digits)
- Kosovo: 5 digits (noted separately)

## Position on Label
Within the consignee/destination address block. Also encoded in MaxiCode barcode (truncated to 6 characters max for non-U.S. destinations in Mode 3).

## ZPL Rendering
- **Typical Position:** Consignee address block area; address format depends on country (Format 1: Postal Code, City, State/Province; Format 2: City, State/Province, Postal Code)
- **Font / Size:** Not specified in extracted text
- **Field Prefix:** None — part of address line
- **ZPL Command:** ^FD (text field) in address block

## Edge Cases & Notes
- Address Format 1 = Postal Code precedes City, State/Province/County
- Address Format 2 = City, State/Province/County precedes Postal Code
- Some countries marked with bullet (•) for "Origin Country" and/or "Destination Country" columns — indicating UPS Europe serves these as origin and/or destination.
- Countries with "-" for postal code length have no postal code system (e.g., Myanmar, Nauru, Ivory Coast, Zimbabwe).
- For MaxiCode encoding: non-U.S. postal codes exceeding 6 characters must be truncated; spaces must be removed.
- Kosovo uses address format 1 with postal code length of 5.

## Claude Confidence
HIGH — Appendix F provides detailed country-by-country postal code formats with examples and address format rules.

## Review Status
- [ ] Reviewed by human