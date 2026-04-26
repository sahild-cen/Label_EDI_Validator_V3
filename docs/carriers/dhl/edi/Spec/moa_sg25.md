# Field: MOA (SG25 Invoice Level)

## Display Name
Monetary Amount (Invoice Level)

## Segment ID
MOA

## Required
yes

## Description
A segment to indicate a monetary value for an Invoice. Part of Segment Group 25 at Invoice Level. Up to 99 occurrences.

## Subfields

### monetary_amount_type_code_qualifier
- **Element Position:** 1.1
- **Pattern/Regex:** (43|64|55|161|79)
- **Required:** yes
- **Description:** Monetary amount type code qualifier (element 5025 within C516 composite). Use '43' = Declared total customs value, '64' = Freight Charge (Override Charge), '55' = Import Duty Value, '161' = Import Tax Value, '79' = Invoice Line Items Total Value. For DDP shipments, '55' and '161' must be provided.

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
Example: MOA+43:150090:EUR'. DHL will only accept 5 monetary amount types other than '43' and '79'. For DDP shipments (see SG31 TOD), Import Duty ('55') and Import Tax ('161') must be provided; sum of '55' + '161' + '43' = Import Total Value is calculated by DHL.

## Claude Confidence
HIGH — spec provides detailed rules for amounts and currencies

## Review Status
- [ ] Reviewed by human