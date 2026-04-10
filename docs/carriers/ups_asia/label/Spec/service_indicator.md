# Field: service_indicator

## Display Name
Service Indicator

## Field Description
A two-character code embedded in the tracking number that identifies the UPS service level. This code appears as the 9th and 10th characters of the 1Z tracking number.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 2 characters
- **Pattern/Regex:** `[A-Z0-9]{2}`
- **Allowed Values:** Per service table: "54" (Express Plus), "66" (Express), "67" (Expedited), "86" (Saver), "04" (Saver EDI-DOC), "85" (Return Service), "E1" (Express Freight), "E5" (Express Freight Import Control/RS), "EA" (Express Freight with Signature), "EQ" (Express Freight Midday), "EV" (Express Freight Midday Import Control/RS), "E3" (Express Freight DC Signature Required), "E4" (Express Freight DC Adult Signature), "E9" (Express Freight Import Control 1-Pickup), "ES" (Express Freight Midday DC Signature), "ET" (Express Freight Midday DC Adult Signature), "EZ" (Express Freight Midday Import Control 1-Pickup), "NT" (Next Day Air)
- **Required:** yes

## Examples from Spec
From service table: E1, E3, E4, E5, E9, EQ, ES, ET, EV, EZ. From tracking numbers: 66, 67, 86, 85, 54, 04, E1, E5, EA, EV, NT

## Position on Label
Embedded within the tracking number (positions 9-10 of the 1Z number). Not displayed as a standalone field.

## Edge Cases & Notes
The service indicator is part of the tracking number structure and is used to identify the class of service. The service table on page 33 maps service indicators to service titles, icons, and class of service codes.

## Claude Confidence
HIGH — explicitly defined in the service table and visible in tracking number examples

## Review Status
- [ ] Reviewed by human