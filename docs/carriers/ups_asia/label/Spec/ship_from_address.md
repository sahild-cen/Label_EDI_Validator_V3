# Field: ship_from_address

## Display Name
Ship From Address

## Field Description
The origin/shipper address block containing contact name, phone number, company name, extended address, street address, postal code line, and country.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
```
CONTACT NAME
PHONE NUMBER
COMPANY NAME
EXTENDED ADDRESS
STREET ADDRESS
POSTAL CODE LINE
COUNTRY
```

## Position on Label
Left-justified at the top of the shipping label (Carrier Segment).

## Edge Cases & Notes
- All uppercase characters required
- Punctuation is not recommended; if necessary, limit to "-" or "/"; no punctuation allowed in MaxiCode data string
- Standard abbreviations should be employed (including 2-letter state or province abbreviations)
- Phone number, contact name, and country are required except when origin and destination country are the same
- Font Size = 8 pt.
- See Appendix F for appropriate Postal Code line configuration

## Claude Confidence
HIGH — spec clearly describes placement, content, and formatting requirements

## Review Status
- [ ] Reviewed by human