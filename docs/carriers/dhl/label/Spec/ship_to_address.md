# Field: ship_to_address

## Display Name
Ship To Address (Consignee Address)

## Field Description
The agreed delivery point address. Each piece requires a Ship To address, which is the destination where the shipment will be delivered.

## Format & Validation Rules
- **Data Type:** string (multi-line)
- **Length:** Maximum 7 lines; minimum 5 lines must be offered by customer automation applications. Highly-Compact version allows 5 lines.
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted — follows same address structure as Ship From
- **Required:** yes — mandatory

## Examples from Spec
Highly-Compact structure:
1. Address line 1: Receiver Company / Name
2. Address line 2: Building Name or equivalent
3. Address line 3: Street Name, Street Number
4. Address line 4: City Name, Postcode or equivalent for other Postal Location Formats (e.g., Suburb, County, State)
5. Country Code / Country Name

## Position on Label
Prominent section on the label, emphasized with hooks (thicker corners, recommended 4x4mm, line thickness >0.5mm).

## Edge Cases & Notes
- The word "To" may be in local language, but for export shipments English "To" must appear; alternatively both languages separated by "/"
- Ship To address should be emphasized by adding hooks (thicker corners)
- Delivery Country and applicable Postal Location Format Elements (e.g., City and Postal Code) must be printed in bigger font
- If space is lacking, the Delivery Country and Postal Location lines can be joined to one line
- Any customer automation application must offer a minimum of 5 lines for the Consignee address
- Maximum 7 lines for consistency with DHL's data structure
- Follows same address element structure as the Ship From address per DHL Corporate Data Model

## Claude Confidence
HIGH — spec provides detailed mandatory status, structure, and formatting requirements

## Review Status
- [ ] Reviewed by human