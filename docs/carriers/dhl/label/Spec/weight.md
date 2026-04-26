# Field: weight

## Display Name
Piece / Shipment Weight

## Field Description
The weight information printed on the transport label, which may include the individual piece weight, the total shipment weight (sum of all piece weights), or both. Always shows dead weight, never calculated volumetric weight. The lack of shipment weight may lead to customs processing issues and is therefore mandatory for at least one package of each dutiable shipment.

## Required
conditional — mandatory for at least the last piece of each dutiable shipment; piece weight mandatory for remote pickup shipments

## ZPL Rendering
- **Typical Position:** shipment information segment
- **Font / Size:** Not specified explicitly; header text in specified segment font

## Subfields

### value
- **Pattern/Regex:** `\d+(\.\d)?` — valid number with no more than one decimal digit; "." if weight not available
- **Required:** conditional — at minimum, last piece label must contain both piece and shipment weight
- **Description:** Numeric weight value. For combined piece/shipment: format is "piece_weight / shipment_weight" (e.g., "5.5 / 33.8"). For single-piece shipments, weight printed only once. A "." indicates weight not yet known.

### unit
- **Pattern/Regex:** `(kg|lb)`
- **Required:** yes — must be printed following the weight value
- **Description:** Unit of measurement, either "kg" or "lb". In combined piece/shipment weight, unit is printed only after the shipment weight. Both weights must use the same unit.

## Edge Cases & Notes
- Header text options: "Piece Weight", "Shipment Weight", or contracted "Piece/Shipment Weight" (abbreviations like "Shpt", "Pce" allowed).
- For domestic shipments, English terms may be translated to local language.
- Example formats: "5.5 / 33.8 kg" (both), "33.8 kg" (shipment only), "8.0 lb" (piece only), "2.7 kg" (single piece), "7/." (piece known, total unknown), "." (no weight available).
- Must always show dead weight, NOT volumetric weight.
- Shipper-declared weight printed if label is printed before DHL reweigh; DHL actual weight printed if after reweigh.
- Customs recommends full shipment weight on each package where available.
- For Germany deliveries, weight symbols (icons) are triggered by piece weight thresholds.

## Claude Confidence
HIGH — extensively detailed with multiple examples and rules

## Review Status
- [ ] Reviewed by human