# Field: routing_code

## Display Name
Routing Code

## Field Description
A composite code used by DHL's sortation systems to route the package through the network. It typically combines the destination service area code, destination facility code, and other sortation indicators.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** DHL system-generated
- **Required:** yes

## Examples from Spec
No examples in spec.

## Position on Label
Displayed prominently, typically in large bold text in the center or upper portion of the label for visual identification during sortation.

## Edge Cases & Notes
The routing code is one of the most visually prominent elements on the label. It is used by DHL handlers and automated sort systems. The format may include destination country code, service area code, and sort indicators separated by hyphens or spaces.

## Claude Confidence
HIGH — Essential sortation element on all DHL Express labels.

## Review Status
- [ ] Reviewed by human