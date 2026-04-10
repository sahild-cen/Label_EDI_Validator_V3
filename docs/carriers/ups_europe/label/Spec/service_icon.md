# Field: service_icon

## Display Name
Service Icon

## Field Description
A graphical icon indicating the class and speed of UPS service. It consists of three fixed positions representing class of service, time of day, and day of delivery.

## Format & Validation Rules
- **Data Type:** alphanumeric (graphical rendering)
- **Length:** 3 positions
- **Pattern/Regex:** Position 1 = class of service (1, 2, or 3); Position 2 = time of day (+, A, P, or Space); Position 3 = day of delivery (S or Space)
- **Allowed Values:** 
  - Position 1: 1, 2, 3
  - Position 2: +, A, P, [Space]
  - Position 3: S, [Space]
  - Exceptions: Black 0.35 inch square for UPS GROUND (U.S.) and UPS® STANDARD (INTERNATIONAL); Open circle for Economy (Canada); Blank for UPS Today™ (Poland)
- **Required:** yes

## Examples from Spec
"1" (UPS EXPRESS), "1+" (UPS EXPRESS PLUS), "1P" (UPS SAVER), "1 S" (Saturday Delivery), "1PS" (Saturday with Saver), "2" (UPS EXPEDITED), "3" (UPS 3 DAY SELECT), "Black Square" (UPS STANDARD)

## Position on Label
Beneath the MaxiCode™ Symbology and Postal Barcode Blocks. Must print to the right of the Service Title and Human-Readable Interpretation. Right-justified with the right edge of the Tracking Number Block.

## ZPL Rendering
- **Typical Position:** Middle-right area, right of service title, right-justified with tracking number block
- **Font / Size:** Font Size = 30 pt. (for text-based icons)
- **Field Prefix:** None — graphic or large text
- **ZPL Command:** ^GFA (for graphic icons like black square) or ^FD (text field) for numeric/letter icons

## Edge Cases & Notes
The three positions remain fixed. Special exceptions exist for UPS GROUND (black 0.35 inch square), Economy Canada (open circle), and UPS Today Poland (blank). Saturday delivery adds "S" in position 3.

## Claude Confidence
HIGH — spec clearly defines the three positions with allowed values and exceptions

## Review Status
- [ ] Reviewed by human