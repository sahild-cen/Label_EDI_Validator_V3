# Field: ship_to_address

## Display Name
Ship To Address

## Field Description
The consignee/destination address block containing the recipient's contact name, phone number, company name, extended address, street address, city, state/province, postal code, and country.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable per line
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes

## Examples from Spec
- "CONTACT NAME / PHONE NUMBER / COMPANY NAME / EXTENDED ADDRESS / STREET ADDRESS / FRIEDBURG 61169 / GERMANY"
- "CONTACT NAME / PHONE NUMBER / COMPANY NAME / EXTENDED ADDRESS / STREET ADDRESS / 28033 MADRID / SPAIN"
- "COMPANY NAME / EXTENDED ADDRESS / STREET ADDRESS / KALAMAZOO MI 49009"

## Position on Label
In the "SHIP TO:" block of the label. For World Ease single labels: "SHIP TO" text = 10 pt. bold, Address Lines = 10 pt., Postal Code Line = 12 pt. bold, Country Line = 12 pt. bold.

## Edge Cases & Notes
For World Ease single labels, font sizes are variable to prevent overwriting the World Ease Routing Code Import Site Box. The postal code and country lines are emphasized in bold.

## Claude Confidence
HIGH — spec provides multiple label examples showing address block structure

## Review Status
- [ ] Reviewed by human