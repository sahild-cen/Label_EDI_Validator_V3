# Field: MOA (SG50 Invoice Line Item)

## Display Name
Monetary Amount (Invoice Line Item)

## Segment ID
MOA

## Required
yes

## Description
A segment to specify a monetary amount associated with a line item, such as Line Item Total Customs Value, Article Customs Value, etc. Part of Segment Group 50. Up to 9 occurrences.

## Subfields

### monetary_amount_type_code_qualifier
- **Element Position:** 1.1
- **Pattern/Regex:** (38|39|146|[A-Z0-9]{1,3})
- **Required:** yes
- **Description:** Monetary amount type code qualifier (element 5025 within C516 composite). Use '38' or '39' = Line Item Value, '146' = Single Item (Article) Customs Value. Full list available from DHL Express.

### monetary_amount
- **Element Position:** 1.2
- **Pattern/Regex:** \d{1,15}\.\d{3}
- **Required:** yes
- **Description:** Monetary amount (element 5004). Max 18 digits including 3 mandatory decimals. Decimal sign depends on UNA segment. COD value must be in destination country currency.

### currency_identification_code
- **Element Position:** 1.3
- **Pattern/Regex:** [A-Z]{3}
- **Required:** yes
- **Description:** Currency identification code (element 6345). ISO 4217 currency codes. Must be currency of shipper country except for qualifier '22' (COD) where destination currency is used.

## Edge Cases & Notes
Example: MOA+38:130000000000000.101:EUR'. All amounts must have 3 decimals regardless of currency.

## Claude Confidence
HIGH — spec provides detailed rules consistent with invoice level MOA

## Review Status
- [ ] Reviewed by human