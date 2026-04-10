# Field: ship_to_address

## Display Name
Ship To Address (Consignee Address)

## Field Description
The destination/receiver address block containing contact name, phone number, company name, extended address, street address, postal code line, and country.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
```
SHIP
TO:    CONTACT NAME
       PHONE NUMBER
       COMPANY NAME
       EXTENDED ADDRESS
       STREET ADDRESS
       POSTAL CODE LINE
       COUNTRY
```

## Position on Label
Below the Ship From address, in the Carrier Segment. The text "SHIP TO" must be printed to the left of the destination address.

## Edge Cases & Notes
- "SHIP TO" text = 10 pt. bold
- Address Lines = 10 pt.
- Postal Code Line = 20 pt. bold
- Country Line = 12 pt. bold
- Phone number, contact name and country are required except when origin and destination country are the same
- See Appendix F for appropriate Postal Code line configuration

## Claude Confidence
HIGH — spec clearly defines placement, font sizes, and formatting

## Review Status
- [ ] Reviewed by human