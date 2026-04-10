# Field: service_icon

## Display Name
Service Icon

## Field Description
A graphical or textual icon indicating the class of service, time of day, and day of delivery. Consists of three fixed positions displayed as a visual indicator.

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 3 positions (fixed)
- **Pattern/Regex:** Position 1 = `[123]`, Position 2 = `[+AP\s]`, Position 3 = `[S\s]`
- **Allowed Values:** Position 1: Class of service (1, 2, or 3). Position 2: Time of day (+, A, P, or Space). Position 3: Day of delivery (S or Space). Exceptions: black 0.35 inch square for UPS GROUND (U.S.) and UPS STANDARD (INTERNATIONAL); open circle for Economy (Canada); blank for UPS Today (Poland).
- **Required:** yes

## Examples from Spec
`1+`, `1`, `1 S`, `1P`, `2`, `3`, Black Square

## Position on Label
To the right of the Service Title and Human-Readable Interpretation, right-justified with the right edge of the Tracking Number Block. Font Size = 30 pt.

## Edge Cases & Notes
- Each icon position remains fixed.
- Special exceptions exist for specific services (black square, open circle, blank).
- The icon values correspond to service type as defined in the Return Service and Import Control indicator tables.

## Claude Confidence
HIGH — spec clearly defines the three positions with allowed values and exceptions

## Review Status
- [ ] Reviewed by human