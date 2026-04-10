# Field: piece_weight

## Display Name
Piece Weight

## Field Description
The weight of an individual piece/package in the shipment. Mandatory for Remote Pickup shipments and must be printed whenever available for multi-piece shipments.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** variable — valid number with no more than one decimal digit
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Dead weight value (not volumetric); "." if weight not available at time of printing
- **Required:** conditional — mandatory for Remote Pickup shipments; must be printed whenever available for multi-piece shipments

## Examples from Spec
- "8.0 lb" (piece weight only)
- "5.5" in "5.5 / 33.8 kg" (piece weight as part of combined display)
- "7/." where "." indicates total weight not yet known
- "2.7 kg" for single-piece shipment

## Position on Label
In the Shipment Information section, with header text "Piece Weight" (or "Pce" abbreviation allowed).

## Edge Cases & Notes
- Must always show dead weight, NOT volumetric weight
- Measuring unit (kg or lb) must be printed following the weight value
- For combined display, unit only required after shipment weight
- Piece weight may be legally required in some countries for health and security reasons
- When not available, "." shall be printed
- For single-piece shipments, weight needs to be printed only once

## Claude Confidence
HIGH — spec provides detailed rules, examples, and header text requirements

## Review Status
- [ ] Reviewed by human