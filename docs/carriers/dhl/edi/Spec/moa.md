# Field: MOA

## Display Name
Monetary Amount

## Segment ID
MOA

## Required
no

## Description
To specify monetary amounts. Used at message header level (conditional) and at shipment level SG25 (optional, up to 99 occurrences).

## Subfields

### monetary_amount_type_code_qualifier
- **Element Position:** 1.1
- **Pattern/Regex:** (22|43|157|64|39|124)
- **Required:** yes
- **Description:** Monetary amount type code qualifier. '22' = Cash on delivery, '43' = Declared total customs value, '157' = Insurance value, '64' = Freight Charge (Override Charge), '39' = Invoice Total Amount, '124' = Tax Amount.

### monetary_amount
- **Element Position:** 1.2
- **Pattern/Regex:** \d{1,16}[.,]\d{2}
- **Required:** yes
- **Description:** Monetary amount value. Max 18 digits including 2 decimals. All amounts must have 2 decimals. Decimal sign may be point or comma per UNA segment. COD value must be in destination country currency.

### currency_identification_code
- **Element Position:** 1.3
- **Pattern/Regex:** [A-Z]{3}
- **Required:** yes
- **Description:** Currency identification code per ISO 4217. Must be currency of shipper country except for COD (qualifier '22') where destination country currency is used.

## Edge Cases & Notes
At message header level, only qualifier '43' (Declared total customs value) is documented. At SG25 shipment level, additional qualifiers ('22', '157', '64', '39', '124') are available. COD value must use destination country currency. All amounts require exactly 2 decimal places regardless of currency.

## Claude Confidence
HIGH — spec provides detailed rules for monetary values

## Review Status
- [ ] Reviewed by human