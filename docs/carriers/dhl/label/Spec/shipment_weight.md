# Field: shipment_weight

## Display Name
Shipment Weight

## Field Description
The sum of weights of all individual pieces building up a shipment. Mandatory for at least one package of each dutiable shipment.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** variable — valid number with no more than one decimal digit
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Dead weight value (not volumetric); "." if weight not available at time of printing
- **Required:** conditional — mandatory for at least the last piece of each dutiable shipment; must be on all labels if known prior to printing first label

## Examples from Spec
- "33.8 kg" (shipment weight only)
- "5.5 / 33.8 kg" (combined piece/shipment weight)
- "8/25" for last piece where 8=piece weight, 25=shipment weight
- "13.4 kg" for single-piece shipment (printed once)

## Position on Label
In the Shipment Information section, with header text "Shipment Weight" (or "Shpt" abbreviation allowed).

## Edge Cases & Notes
- Must always show dead weight, NOT calculated volumetric weight
- Lack of shipment weight may lead to customs processing issues
- As minimum, last piece label must contain both piece and shipment weight
- Measuring unit (kg or lb) must be same for both piece and shipment weight
- When no weight available at printing, "." shall be printed
- Customer applications must ensure at least the last package contains shipment weight
- Customs recommends full shipment weight on each package for easier processing

## Claude Confidence
HIGH — spec provides extensive rules, multiple examples, and clear requirements

## Review Status
- [ ] Reviewed by human