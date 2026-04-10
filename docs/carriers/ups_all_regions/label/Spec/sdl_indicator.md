# Field: sdl_indicator

## Display Name
State Department License (SDL) Indicator

## Field Description
An indicator printed on the label to alert UPS Operations that the shipment contains export-controlled articles requiring a State Department License or license exemption.

## Format & Validation Rules
- **Data Type:** string
- **Length:** 3 characters
- **Pattern/Regex:** `SDL`
- **Allowed Values:** "SDL"
- **Required:** conditional — required for all State Department Licensed or Exempted shipments

## Examples from Spec
- `SDL` (standalone)
- `SDL/POA` (combined with Power of Attorney)
- `SDL/EEI/POA` (combined with EEI and POA)

## Position on Label
In the routing section of the label. For Air Freight, it prints in the routing section. When combined with other indicators (POA, EEI, CO), they are separated by forward slashes.

## Edge Cases & Notes
When SDL is combined with POA, EEI, and/or CO indicators, they must be separated by a forward slash (/). Must print on all labels in a shipment when applicable. Font size is 10 pt. bold.

## Claude Confidence
HIGH — Clearly defined with specific formatting rules and multiple examples.

## Review Status
- [ ] Reviewed by human