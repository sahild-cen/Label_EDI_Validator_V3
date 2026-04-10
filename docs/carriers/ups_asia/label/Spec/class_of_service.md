# Field: class_of_service

## Display Name
Class of Service

## Field Description
A numeric code identifying the UPS class of service, as defined in the service table.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 3 characters
- **Pattern/Regex:** `\d{3}`
- **Allowed Values:** Per service table: 417 (Express Freight), 419 (Express Freight DC Sig Required), 420 (Express Freight DC Adult Sig), 421 (Express Freight Import Control/RS), 425 (Express Freight Import Control 1-Pickup), 439 (Express Freight Midday), 441 (Midday DC Sig Required), 442 (Midday DC Adult Sig), 443 (Midday Import Control/RS), 447 (Midday Import Control 1-Pickup)
- **Required:** conditional — used internally for service identification

## Examples from Spec
417, 419, 420, 421, 425, 439, 441, 442, 443, 447

## Position on Label
Not specified in spec — may be encoded in barcodes rather than printed as human-readable text.

## Edge Cases & Notes
These values are from the Express Freight service table on page 33. Additional class of service codes likely exist for non-freight services but are not shown in the extracted spec text.

## Claude Confidence
MEDIUM — defined in the service table but not clearly visible as printed on labels

## Review Status
- [ ] Reviewed by human