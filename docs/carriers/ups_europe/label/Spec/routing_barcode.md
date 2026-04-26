# Field: routing_barcode

## Display Name
Routing Code Barcode

## Group Description
A barcode representation of the routing code, appearing in the center section of the UPS label. This barcode encodes the same routing data shown as human-readable text nearby.

## Sub-Fields

### routing_barcode
- **Data Type:** barcode
- **Length:** variable (matches routing code data)
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** Not restricted
- **Required:** yes
- **Description:** Barcode encoding the routing code for automated package sorting
- **Detect By:** spatial:center_label, barcode positioned between ship-to address and service type
- **Position on Label:** center of label
- **ZPL Font:** Not applicable
- **Field Prefix:** None
- **ZPL Command:** Not specified (likely ^BC or similar 1D barcode command)

## Examples from Spec
No explicit barcode format examples; routing code values appear as "DEU 063 9-39", "FRA 753 7-00", etc.

## Edge Cases & Notes
- The routing barcode appears to be a 1D barcode in the center zone of the label.
- The human-readable routing code appears both above/below this barcode.

## Claude Confidence
MEDIUM — Barcode presence is evident from label layouts but specific barcode symbology is not explicitly stated in extracted text.

## Review Status
- [x] Reviewed by human