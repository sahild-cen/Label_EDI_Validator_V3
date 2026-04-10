# Field: piece_weight_symbols

## Display Name
Piece Weight Symbols

## Field Description
Graphical weight warning icons/symbols displayed on transport labels for shipments delivered in Germany, indicating when piece weight exceeds specific thresholds (10 kg or 20 kg) per German federal law effective July 1, 2024.

## Format & Validation Rules
- **Data Type:** graphic/icon
- **Length:** N/A
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** No icon (< 10 kg), "10+ kg" symbol (≥ 10 kg and < 20 kg), "20+ kg" symbol (≥ 20 kg)
- **Required:** conditional — mandatory for all shipments delivered in Germany (DE)

## Examples from Spec
Weight thresholds:
- Less than 10 kg (or 22 lb): No icon printed
- 10.000 to 19.999 kg (or 22.000 to 43.999 lb): "10+ kg" symbol
- 20.000 kg and above (or 44.000 lb and above): "20+ kg" symbol

## Position on Label
Located in the segment containing Piece and Shipment Weights, on their left side. For ECOM26_711_001 template (limited space), printed to the right of Pce/Shpt Weight segment.

## Edge Cases & Notes
- Only PIECE_WEIGHT (Customer-Declared Piece Weight) is used to determine symbol; SHIPMENT_WEIGHT is not considered
- Applied irrespective of original unit of measurement (kg or lb)
- Does not apply to shipments in transit via Germany, only final destination DE
- Applied across all Transport Label templates (ECOM, NETW, DUO)
- Fine adjustments to location are acceptable to avoid overlap
- Deviations from standard location require pre-approval from Global SOP or Global Competence Center

## Claude Confidence
HIGH — spec provides very detailed business rules, threshold tables, and placement guidance

## Review Status
- [ ] Reviewed by human