# Field: service_type

## Display Name
Service Type

## Field Description
Identifies the DHL service level or product used for the shipment. This determines transit time, handling priority, and routing within the DHL network. Typically displayed prominently on the label.

## Format & Validation Rules
- **Data Type:** string
- **Length:** variable
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** DHL Express services include: "EXPRESS WORLDWIDE" (WPX), "EXPRESS 9:00" (E9), "EXPRESS 10:30" (E10), "EXPRESS 12:00" (E12), "EXPRESS ENVELOPE" (XPD), "ECONOMY SELECT" (ESU), "EXPRESS EASY" (EAZ), "DOMESTIC EXPRESS" (DOM), among others
- **Required:** yes

## Examples from Spec
No examples in extracted spec text.

## ZPL Rendering
- **Typical Position:** top area of label, often in a highlighted/boxed region
- **Font / Size:** Large bold font; may appear in a shaded or bordered box
- **Field Prefix:** None — service name printed directly
- **ZPL Command:** ^FD (text field); may use ^GB for background box

## Edge Cases & Notes
The service type determines many other label characteristics including routing codes and sort codes. DHL uses both full service names and abbreviated product codes. The DHL logo color/branding may vary by service type. Time-definite services (9:00, 10:30, 12:00) require special prominent display.

## Claude Confidence
MEDIUM — standard DHL field but no specific format detail in extracted spec

## Review Status
- [ ] Reviewed by human