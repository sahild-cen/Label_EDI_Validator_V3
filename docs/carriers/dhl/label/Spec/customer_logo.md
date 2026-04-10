# Field: customer_logo

## Display Name
Customer Logo

## Field Description
An optional logo image that may be placed in the space to the right of the sender address segment. Alternatively, a DHL Initiative Logo (e.g., GoGreen) may be placed here if the customer agrees or requests it.

## Format & Validation Rules
- **Data Type:** image
- **Length:** N/A
- **Pattern/Regex:** Not applicable
- **Allowed Values:** Customer's logo or DHL Initiative Logo (e.g., GoGreen)
- **Required:** no — optional

## Examples from Spec
"GoGreen" mentioned as an example DHL Initiative Logo.

## Position on Label
To the right of the sender address segment (Ship From section). Also referenced near the Ship To section (element 8).

## Edge Cases & Notes
- Alternatively, a DHL Initiative Logo (e.g., GoGreen) can be placed if customer agrees or asks for it
- The relative small font of the sender address creates space for this element

## Claude Confidence
HIGH — spec clearly states optional status and placement

## Review Status
- [ ] Reviewed by human