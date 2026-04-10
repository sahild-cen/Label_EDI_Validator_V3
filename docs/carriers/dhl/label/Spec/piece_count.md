# Field: piece_count

## Display Name
Relative and Total Number of Pieces in Shipment

## Field Description
Shows the relative position of this piece within the shipment and the total number of pieces to be transported and billed. Predominantly mandatory as it reduces risk of delays in customs processing.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** variable — format "X/Y" where X and Y are numeric, separated by "/"
- **Pattern/Regex:** `\d+/(\d+|\.)` (piece counter slash total or dot)
- **Allowed Values:** "X/Y" where X=current piece number, Y=total pieces; "." replaces unknown values
- **Required:** conditional — predominantly mandatory; suppression requires DHL's explicit approval

## Examples from Spec
- "1/1" for single-piece shipment
- "12/12" for last piece of 12-piece shipment
- "3/." for third piece where total is unknown
- "X/." syntax when total not known
- "X/Y" syntax when total is known
- "Y/Y" syntax for last piece label

## Position on Label
In the Shipment Information section.

## Edge Cases & Notes
- Criticality varies: "very high" for non-doc shipments, "moderate" for doc shipments
- Should be suppressed if correctness cannot be guaranteed
- DHL's explicit approval required for permanent suppression on account level
- Missing numbers replaced by "." (dot)
- At minimum, last piece label must contain both total and final single count

## Claude Confidence
HIGH — spec provides detailed rules with multiple examples and clear syntax

## Review Status
- [ ] Reviewed by human