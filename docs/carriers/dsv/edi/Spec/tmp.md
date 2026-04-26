# Field: TMP

## Display Name
Temperature

## Segment ID
TMP

## Required
no

## Description
Specifies temperature requirements for transport equipment (e.g., reefer containers).

## Subfields

### temperature_type_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** \d{1,3}
- **Required:** yes
- **Description:** Temperature type code qualifier

### temperature_degree
- **Element Position:** 2.1
- **Pattern/Regex:** -?\d{1,15}
- **Required:** no
- **Description:** Temperature degree (composite C239, first sub-component). The temperature setting value.

### measurement_unit_code
- **Element Position:** 2.2
- **Pattern/Regex:** CEL
- **Required:** no
- **Description:** Measurement unit code (composite C239, second sub-component). CEL = degree Celsius

## Edge Cases & Notes
TMP is conditional, max 1 occurrence within SG38. This TMP at equipment level differs from TMP at goods item level. Example: TMP+1+9:10'. Note the example shows temperature_degree as "9" and measurement_unit_code as "10" which may indicate a non-standard usage pattern — verify with DSV. The spec lists CEL as the valid code for measurement unit.

## Claude Confidence
MEDIUM — example TMP+1+9:10 does not clearly match the CEL unit code specification; may need clarification

## Review Status
- [ ] Reviewed by human