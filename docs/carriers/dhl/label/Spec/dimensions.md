# Field: dimensions

## Display Name
Dimensions

## Field Description
The physical dimensions of the package. Used for volumetric weight calculation and operational handling within DHL's network.

## Required
conditional — required for non-document shipments and when volumetric weight applies

## ZPL Rendering
- **Typical Position:** near weight field, lower or mid-section of label
- **Font / Size:** Not specified

## Subfields

### length
- **Pattern/Regex:** ^\d+(\.\d{1})?$
- **Required:** yes
- **Description:** Length of the package (longest side)

### width
- **Pattern/Regex:** ^\d+(\.\d{1})?$
- **Required:** yes
- **Description:** Width of the package

### height
- **Pattern/Regex:** ^\d+(\.\d{1})?$
- **Required:** yes
- **Description:** Height of the package

### unit
- **Pattern/Regex:** ^(CM|IN|cm|in)$
- **Required:** yes
- **Description:** Dimension unit of measure — CM for metric, IN for imperial

## Edge Cases & Notes
DHL uses centimeters (CM) as the standard dimension unit globally. Volumetric weight is calculated as (L × W × H) / 5000 in cm for DHL Express. Dimensions may not always appear on the printed label but are required in the shipment data.

## Claude Confidence
LOW — standard field but may not always print on label

## Review Status
- [ ] Reviewed by human