# Field: product_features

## Display Name
Product Features

## Field Description
Product features indicated via TOD (Terms of Delivery) segment at SG31 level. Appendix B contains the full list of product features.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** See Appendix B – Product Features (not fully extracted)
- **Required:** conditional — at SG31 level

## Examples from Spec
No examples in spec (Appendix B referenced but not fully extracted).

## Position on Label
Not specified in spec.

## Edge Cases & Notes
Per change report v0.5, Appendix B for Product Features was added for Advance Shipments. Per v0.8, additional product features were added. TOD segment includes samples for LBBX Baby or Mother service codes per v0.8 update. Per v1.1, TOD 4052:2 (Account Number) was added.

## Claude Confidence
MEDIUM — TOD segment described but product feature values are in Appendix B which is not fully extracted.

## Review Status
- [ ] Reviewed by human