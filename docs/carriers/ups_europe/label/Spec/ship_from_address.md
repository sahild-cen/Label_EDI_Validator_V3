# Field: ship_from_address

## Display Name
Ship From Address

## Field Description
The shipper/sender address block that appears at the top of the shipping label. Contains contact name, phone number, company name, extended address, street address, postal code line, and country.

## Format & Validation Rules
- **Data Type:** string (multi-line text block)
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
Label samples show:
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
Left-justified at the top of the shipping label, within the Carrier Segment.

## ZPL Rendering
- **Typical Position:** Top-left of label
- **Font / Size:** 8pt for address lines
- **Field Prefix:** None — the ship-from address block has no explicit text prefix
- **ZPL Command:** ^FD (text field) — multiple lines

## Edge Cases & Notes
- All uppercase characters required.
- Punctuation is not recommended; if used, validate with destination postal authority.
- Standard abbreviations should be employed (including 2-letter state or province abbreviations).
- Phone number, contact name, and country are required except when origin and destination country are the same.
- Phone number is optional when shipping to/from the European Union (EU).
- See Appendix F for appropriate Postal Code line configuration.
- City/State, Province or County must print on the same line with the Postal Code.
- ZIP+4™ codes must be used if available.

## Claude Confidence
HIGH — spec provides detailed formatting requirements, font sizes, and content rules

## Review Status
- [ ] Reviewed by human