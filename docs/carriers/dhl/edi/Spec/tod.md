# Field: TOD

## Display Name
Terms of Delivery

## Segment ID
TOD

## Required
yes

## Description
To specify terms of delivery or transport. Mandatory within SG31 to indicate freight costs payment and Incoterms. Also supports product features and account-based charge allocation.

## Subfields

### delivery_or_transport_form_function_code
- **Element Position:** 1
- **Pattern/Regex:** 6
- **Required:** yes
- **Description:** Delivery or transport form function code — Use '6' for Delivery conditions.

### transport_charges_payment_method_code
- **Element Position:** 2
- **Pattern/Regex:** A?
- **Required:** no
- **Description:** Transport charges payment method code. Use 'A' to indicate charges are to be charged to an account. Only used when extra charge codes have related account numbers.

### delivery_or_transport_terms_description_code
- **Element Position:** 3.1
- **Pattern/Regex:** (DDU|DDP|CPT|[A-Z]{3})
- **Required:** yes
- **Description:** Incoterms code. Default is 'DDU'. For complete list, contact Sales representative. 'DDP' used for Loose Bulk services.

### code_list_identification_code
- **Element Position:** 3.2
- **Pattern/Regex:** .*
- **Required:** no
- **Description:** Code list identification code — Not used.

### code_list_responsible_agency_code
- **Element Position:** 3.3
- **Pattern/Regex:** .*
- **Required:** no
- **Description:** Code list responsible agency code — Not used.

### product_features
- **Element Position:** 3.4
- **Pattern/Regex:** (\d{3}){0,23}
- **Required:** no
- **Description:** Product features/Extra Charge Codes. Each code is 3 digits with leading zero. Multiple codes concatenated without separator. Max 23 codes (AN..70). Extra Charge Codes with related Account Numbers should be placed first. E.g., '050051' = Saturday delivery + Named signature. '230' = Loose Bulk Mother, '231' = Loose Bulk Baby, '300' = Direct injection.

### account_numbers
- **Element Position:** 3.5
- **Pattern/Regex:** (.{9}){0,7}
- **Required:** no
- **Description:** Account Numbers for extra charges. Each is 9 characters, concatenated without separator. Must be in same order as related Extra Charge Codes in element 3.4. Max 7 account numbers (AN..70).

## Edge Cases & Notes
When using account-based charges, element 2 must be 'A'. Extra Charge Codes with related Account Numbers must be placed first in element 3.4, followed by codes without related accounts. Example: TOD+6+A+DDU:::101103151152202203204207208:ACC123456BCC123456CCC123456DCC123456ECC123456FCC123456GCC123456

## Claude Confidence
HIGH — spec provides extensive detail with multiple examples

## Review Status
- [ ] Reviewed by human