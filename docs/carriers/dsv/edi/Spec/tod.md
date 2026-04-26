# Field: TOD

## Display Name
Terms of Delivery or Transport

## Segment ID
TOD

## Required
no

## Description
Specifies the terms of delivery or transport, including Incoterms and Combiterms.

## Subfields

### delivery_or_transport_terms_function_code
- **Element Position:** 1
- **Pattern/Regex:** 6
- **Required:** no
- **Description:** Delivery or transport terms function code (4055). Valid code: 6=Delivery condition.

### transport_charges_payment_method_code
- **Element Position:** 2
- **Pattern/Regex:** an..3
- **Required:** no
- **Description:** Transport charges payment method code (4215). Not used.

### delivery_or_transport_terms_description_code
- **Element Position:** 3.1
- **Pattern/Regex:** (CFR|CIF|CIP|CPT|DAP|DDP|DPU|EXW|FAS|FCA|FOB|[0-9]{3})
- **Required:** no
- **Description:** Delivery or transport terms description code (C100/4053). Incoterm code. Valid codes: CFR, CIF, CIP, CPT, DAP, DDP, DPU, EXW, FAS, FCA, FOB. Numeric codes may be used for Combiterms.

### delivery_terms_code_list
- **Element Position:** 3.2
- **Pattern/Regex:** (ZCT)?
- **Required:** no
- **Description:** Code list identification code (C100/1131). Leave blank for Incoterms. Use ZCT for Combiterms.

### delivery_terms_agency
- **Element Position:** 3.3
- **Pattern/Regex:** an..3
- **Required:** no
- **Description:** Code list responsible agency code (C100/3055). Not used.

### delivery_terms_description_1
- **Element Position:** 3.4
- **Pattern/Regex:** an..70
- **Required:** no
- **Description:** Delivery or transport terms description (C100/4052). Not used.

### delivery_terms_description_2
- **Element Position:** 3.5
- **Pattern/Regex:** an..70
- **Required:** no
- **Description:** Delivery or transport terms description 2 (C100/4052). Not used.

## Edge Cases & Notes
TOD is the trigger segment for SG2, which can occur up to 2 times. For Road, at least one of Incoterm (SG2 TOD+6) or Freight Payer (SG12 NAD+FP) is required. Examples: TOD+6++EXW', TOD+6++022:ZCT' (Combiterm).

## Claude Confidence
HIGH — spec clearly defines structure and valid Incoterm codes

## Review Status
- [ ] Reviewed by human