# Field: service_indicator

## Display Name
Service Indicator

## Field Description
A two-character code embedded in the tracking number that identifies the specific UPS service level and any accessorial options (such as signature required, adult signature, Saturday delivery, or COD).

## Format & Validation Rules
- **Data Type:** alphanumeric
- **Length:** 2 characters
- **Pattern/Regex:** `[A-Z0-9]{2}`
- **Allowed Values:** Enumerated list including: 54, G1, G5, 34, G4, G8, AT, GG, G9, AV, GH, GA, 66, D3, D4, 69, D6, D7, 04, D9, DA, 67, DG, DH, 68, DK, DL, FX, FY, FZ, QH, QD, QE, 73, G2, G6, G3, G7, 75, C6, C7, 76, C9, CA, 77, CH, CJ, 79, CP, CR, GJ, GK, GL, Q4, QA, QC, T8, T9, TG, TH, TN, TP, TT, TW
- **Required:** yes

## Examples from Spec
- `54` (UPS Express Plus)
- `66` (UPS Express)
- `AT` (UPS Express NA1)
- `04` (UPS Saver)
- `67` (UPS Expedited)
- `68` (UPS Standard)
- `75` (UPS Express COD Lead)
- `FX` (UPS Standard Saturday Delivery)
- `G9` (UPS Express NA1 Adult Signature Required)
- `QH` (UPS Express 12:00)

## Position on Label
Embedded within the tracking number (positions 8-9 of the 1Z tracking number). Not displayed as a standalone visible field.

## ZPL Rendering
- **Typical Position:** Embedded within the tracking number barcode data
- **Font / Size:** Not specified — not a separately printed text element
- **Field Prefix:** None — embedded in tracking number
- **ZPL Command:** Part of tracking number barcode data

## Edge Cases & Notes
Different service indicators are used for COD lead packages vs. COD child packages. The service indicator determines the service icon and MaxiCode class of service. Signature Required and Adult Signature Required have their own distinct indicators per service.

## Claude Confidence
HIGH — comprehensively enumerated in the spec with multiple tables

## Review Status
- [ ] Reviewed by human