# Field: service_icon

## Display Name
Service Icon

## Group Description
A graphical icon representing the UPS service class, positioned to the right of the UPS Service Title and human-readable interpretation. The icon consists of three fixed positions indicating class of service, time of day, and day of delivery.

## Sub-Fields

### service_icon
- **Data Type:** string
- **Length:** 3 positions (fixed)
- **Pattern/Regex:** `^[123][+AP\s][S\s]$`
- **Allowed Values:** Position 1: 1, 2, or 3 (class of service); Position 2: +, A, P, or space (time of day); Position 3: S or space (day of delivery — S for Saturday)
- **Required:** yes
- **Description:** Three-position service icon indicating class of service, time of day, and delivery day. Exceptions: black 0.35 inch square for UPS GROUND (U.S.) and UPS STANDARD (International); open circle for Economy (Canada); blank for UPS Today (Poland).
- **Detect By:** spatial:right of service title, fixed icon area
- **Position on Label:** Right of the Service Title and Human-Readable Interpretation, right-justified with the right edge of the Tracking Number Block
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^GFA (graphic) or ^FD (text field)

## Examples from Spec
Service icon values from spec tables:
- `1+` — UPS EXPRESS PLUS
- `1` — UPS EXPRESS, UPS EXPRESS 12:00
- `1S` — UPS EXPRESS with Saturday Delivery
- `1P` — UPS SAVER, UPS EXPRESS FREIGHT
- `2` — UPS EXPEDITED
- `3` — UPS 3 DAY SELECT
- Black Square — UPS STANDARD

## Edge Cases & Notes
- UPS GROUND (U.S.) and UPS STANDARD (International) use a black 0.35 inch square instead of text.
- Economy (Canada) uses an open circle.
- UPS Today (Poland) has a blank icon.
- Each of the three positions remains fixed in the layout.

## Claude Confidence
HIGH — spec explicitly defines the three-position icon structure with allowed values and exceptions.

## Review Status
- [x] Reviewed by human