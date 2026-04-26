# Field: incoterms

## Display Name
Incoterms / Terms of Trade

## Field Description
Indicates the international commercial terms (Incoterms) that define duties and taxes payment responsibility. Determines whether the shipper or receiver pays customs duties/taxes.

## Format & Validation Rules
- **Data Type:** string
- **Length:** 3 characters
- **Pattern/Regex:** ^(DAP|DDP|DDU|EXW|FCA|CPT|CIF|FOB)$
- **Allowed Values:** Standard Incoterms codes; most commonly DAP (Delivered at Place) and DDP (Delivered Duty Paid) for DHL Express
- **Required:** conditional — required for international shipments

## Examples from Spec
No examples in extracted spec text.

## ZPL Rendering
- **Typical Position:** customs area or billing information section
- **Font / Size:** Not specified
- **Field Prefix:** "Terms:" or displayed as part of billing/duty information
- **ZPL Command:** ^FD (text field)

## Edge Cases & Notes
DAP (formerly DDU) means receiver pays duties/taxes at delivery. DDP means shipper/third party has prepaid all duties/taxes. This field directly affects how DHL handles customs clearance and billing.

## Claude Confidence
LOW — known international shipping field but no detail in extracted spec

## Review Status
- [ ] Reviewed by human