# Field: shipment_information

## Display Name
Shipment Information (SHP#, Weight, Date, Dimensional Weight)

## Group Description
The shipment-level metadata block including shipper number, shipment weight, dimensional weight, and ship date, appearing in the upper portion of the label adjacent to the ship-from address.

## Sub-Fields

## Examples from Spec
```
SHP#: 1X2X 3X33 3VP
SHP WT: 50.5 KG
DATE: 11 JAN 2020
SHP DWT: 50.5 KG
```
```
SHP#: 1X2X 3X33 3TT
SHP WT: 8 KG
DATE: 11 JAN 2020
SHP DWT: 8 KG
```
```
SHP WT: 1542 LBS
```

## Edge Cases & Notes
- Weight unit can be KG or LBS depending on origin country.
- SHP DWT (dimensional weight) may not appear on all labels, only when dimensional weight is applicable.

## Claude Confidence
HIGH — spec examples clearly show these fields with consistent prefixes across multiple label examples.

## Review Status
- [x] Reviewed by human