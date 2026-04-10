# Field: ups_premier_level_indicator

## Display Name
UPS Premier Service Level Indicator

## Field Description
A text code printed in the Package Information Block of the label indicating which UPS Premier service level (Silver, Gold, or Platinum) has been selected for the shipment.

## Format & Validation Rules
- **Data Type:** string
- **Length:** 3 characters
- **Pattern/Regex:** `^(SLV|GLD|PLT)$`
- **Allowed Values:** "SLV" (Silver), "GLD" (Gold), "PLT" (Platinum)
- **Required:** conditional — required for all UPS Premier shipments, for all origins and destinations

## Examples from Spec
- "SLV" (shown on UPS Premier Silver International Label)
- "PLT" (shown on UPS Premier Platinum US Domestic Label)

## Position on Label
Prints in the Package Information Block of the label.

## Edge Cases & Notes
- Font Size = 16 pt. bold for all three levels.
- UPS Premier is a contractual service for complex, sensitive packages (e.g., healthcare and pharmaceutical items).
- UPS Premier Silver uses RFID labels; Gold and Platinum use Mesh Identifiers.

## Claude Confidence
HIGH — spec explicitly defines the three allowed values and placement.

## Review Status
- [ ] Reviewed by human