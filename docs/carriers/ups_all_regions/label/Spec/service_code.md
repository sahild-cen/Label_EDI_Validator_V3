# Field: service_code

## Display Name
Service Code

## Field Description
A short alphanumeric code representing the UPS service level, used internally for routing and processing. Appears as a numeric or alphanumeric indicator on the label near the service name.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 1-3 characters
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:**
  - Domestic: 1DA, EAM, 1DS, 2DA, 2DM, 3DS, EXM, GND, LCO, TDT, TDC, TDE, TDS
  - International: EXD, EXP, EXS, EAM, WFP, WFM
  - Numeric codes visible on labels: 1, 1P, 1+, 1+S, 2
- **Required:** yes

## Examples from Spec
- `1` (UPS Express, UPS Next Day Air)
- `1P` (UPS Saver, UPS Express Freight)
- `1+` (UPS Express Plus)
- `1+S` (UPS Next Day Air Early with additional service)
- `2` (UPS Expedited)

## Position on Label
Displayed as a large numeral/code near the service type banner area, typically to the right side of the routing code section.

## Edge Cases & Notes
The numeric service indicator (1, 1P, 1+, 2, etc.) appears to be a visual routing aid distinct from the three-letter service codes listed in the table. The "P" suffix may indicate a premium/priority variant, and "+" may indicate an express plus variant. "S" suffix appears related to Saturday delivery or special handling.

## Claude Confidence
MEDIUM — The numeric codes on labels are visible but the spec does not explicitly map each numeric code to its meaning in the extracted text.

## Review Status
- [ ] Reviewed by human