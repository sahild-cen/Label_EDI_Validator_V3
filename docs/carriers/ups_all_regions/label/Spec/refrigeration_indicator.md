# Field: refrigeration_indicator

## Display Name
Refrigeration Indicator (RFG)

## Field Description
An indicator that appears on the label to denote that the package requires refrigeration handling, often used in conjunction with UPS Premier service.

## Format & Validation Rules
- **Data Type:** string
- **Length:** 3 characters
- **Pattern/Regex:** `^RFG$`
- **Allowed Values:** "RFG"
- **Required:** conditional — required when refrigeration service is selected

## Examples from Spec
"RFG" shown on the UPS Premier Platinum US Domestic Label with COD, Refrigeration and Adult Signature Required.

## Position on Label
Appears in the Package Information Block area, alongside the Premier level indicator (e.g., "PLT RFG").

## Edge Cases & Notes
- Shown paired with the UPS Premier Platinum indicator in the example label.
- May appear alongside other service indicators like COD and Adult Signature Required.

## Claude Confidence
MEDIUM — shown clearly on example label but limited textual specification of exact rules.

## Review Status
- [ ] Reviewed by human