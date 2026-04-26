# Field: shipment_number

## Display Name
Shipment Number

## Group Description
An 11-digit alphanumeric shipment identifier calculated using the Base 26 method from the lead package tracking number. Used for shipment-level identification.

## Sub-Fields

### shipment_number
- **Data Type:** alphanumeric
- **Length:** 11
- **Pattern/Regex:** `^[A-Z0-9]{6}[3-9A-Z]{5}$` (6-char shipper number + 5-char Base 26 converted value)
- **Allowed Values:** The first 6 characters are the shipper/account number; last 5 characters are Base 26 converted values using conversion table (digits 3,4,7,8,9 and letters B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,V,W,X,Y,Z)
- **Required:** yes
- **Description:** Calculated from the lead package tracking number using Base 26 calculation. Exclude "1Z" and account number, exclude service level indicator and check digit, convert remaining 7-digit package ID through Base 26 division, then convert using the Base 26 conversion table. Prepend the 6-character shipper number.
- **Detect By:** text pattern matching 11-char alphanumeric with Base 26 character set
- **Position on Label:** This number must appear 
directly beneath the package weight and count.
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Examples from Spec
- Tracking number `1Z123X5666207548 64` → Shipment Number: `123X569M7CH`
- Tracking number `1Z123X56Y644000050` → Shipment Number: `123X56GPFWZ`

## Edge Cases & Notes
- Base 26 conversion table maps values 0-25 to: 3,4,7,8,9,B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,V,W,X,Y,Z
- Letters A,E,I,O,U and digits 0,1,2,5,6 are intentionally excluded from the conversion output (likely to avoid confusion with similar-looking characters).
- Calculation uses the 7-digit package identification portion of the tracking number (positions after service level indicator, excluding check digit).
- The integer value is kept at each division step; remainders are discarded.

## Claude Confidence
HIGH
Spec provides complete Base 26 calculation method with two worked examples and the conversion table.

## Review Status
- [x] Reviewed by human