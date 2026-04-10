# Field: consignee_communication_contact

## Display Name
Consignee Communication Contact

## Field Description
A segment (SG44 - COM) to indicate the type of communication contact to be used to inform the contact person at the consignee level.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Qualifiers include TEL (telephone), EML (email), FAX (fax), AL (mobile)
- **Required:** conditional — up to 9 occurrences

## Examples from Spec
No examples in spec.

## Position on Label
Not specified in spec.

## Edge Cases & Notes
Per document change report v0.8, qualifier "AL" was added for element 3155 to support mobile phone numbers (mapped to MOB). Email contact qualifier was also added per v0.3 update.

## Claude Confidence
HIGH — Communication qualifiers are explicitly documented in the change report.

## Review Status
- [ ] Reviewed by human