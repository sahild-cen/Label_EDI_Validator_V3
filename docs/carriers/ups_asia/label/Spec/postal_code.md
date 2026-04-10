# Field: postal_code

## Display Name
Postal Code

## Field Description
The postal/ZIP code for the destination address. Format, length, and position within the address line vary by destination country as defined in the Postal Code Line Format Matrix (Appendix F).

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable — depends on destination country (e.g., 5 for Croatia/Turkey, 6 for Nigeria/Turkmenistan, 4 for Mozambique/Norfolk Island, 5 for Wallis and Futuna/Indonesia)
- **Pattern/Regex:** Country-dependent
- **Allowed Values:** Country-dependent format
- **Required:** conditional — required for countries that have postal code systems; some countries have no postal codes (indicated by "-" in the matrix)

## Examples from Spec
- Croatia: 10000 (5 digits)
- Indonesia: 40115 (5 digits)
- Mozambique: 1100 (4 digits)
- Nigeria: 930283 (6 digits)
- Norfolk Island: 2899 (4 digits)
- Turkey: 01960 (5 digits)
- Turkmenistan: 744000 (6 digits)
- Wallis and Futuna: 98600 (5 digits)
- Kosovo: 5 digits

## Position on Label
Within the destination address block. Address Format 1 = Postal Code, City, State/Province/County. Address Format 2 = City, State/Province/County, Postal Code.

## Edge Cases & Notes
- Address Format 1 places postal code BEFORE city; Address Format 2 places it AFTER city and state.
- Some countries have no postal codes (marked with "-" for length).
- For MaxiCode encoding: postal codes must not contain spaces or special characters; truncate to 6 characters for non-U.S. MaxiCode Mode 3; remove embedded spaces (e.g., "W1T 1JY" → "W1T1JY").
- U.S. ZIP codes can be 5 or 9 digits (ZIP+4 without hyphen in MaxiCode).

## Claude Confidence
HIGH — Multiple examples and format rules provided across Appendix F and MaxiCode definitions.

## Review Status
- [ ] Reviewed by human