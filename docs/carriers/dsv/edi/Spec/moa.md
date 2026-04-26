# Field: MOA

## Display Name
Monetary Amount

## Segment ID
MOA

## Required
no

## Description
Specifies monetary amounts related to the shipment, including cash on delivery, insurance, invoice amounts, and freight rates.

## Subfields

### monetary_amount_type_code_qualifier
- **Element Position:** 1.1
- **Pattern/Regex:** (22|67|77|ZFR)
- **Required:** yes
- **Description:** Monetary amount type code qualifier (C516/5025). Valid codes: 22=Consignment cash on delivery amount, 67=Insurance amount, 77=Invoice line item amount, ZFR=DSV specific value for FreightRate (use as agreed).

### monetary_amount
- **Element Position:** 1.2
- **Pattern/Regex:** n..35
- **Required:** no
- **Description:** Monetary amount value (C516/5004).

### currency_identification_code
- **Element Position:** 1.3
- **Pattern/Regex:** [A-Z]{3}
- **Required:** no
- **Description:** Currency identification code (C516/6345). ISO 4217 3 alpha code to be used (e.g., SEK, DKK, EUR).

### currency_type_code_qualifier
- **Element Position:** 1.4
- **Pattern/Regex:** an..3
- **Required:** no
- **Description:** Currency type code qualifier (C516/6343). Not used.

### status_description_code
- **Element Position:** 1.5
- **Pattern/Regex:** an..3
- **Required:** no
- **Description:** Status description code (C516/4405). Not used.

## Edge Cases & Notes
MOA can occur up to 99 times. If TSR element 7273 has value 29 for insurance service, a MOA with qualifier 67 must be provided with the insurance amount. Not used for Air, Sea, or Courier. Examples: MOA+22:3400:SEK' (Cash on delivery), MOA+67:1546:DKK' (Insurance), MOA+77:1546:DKK' (Invoice amount).

## Claude Confidence
HIGH — spec clearly defines the composite element and valid codes

## Review Status
- [ ] Reviewed by human