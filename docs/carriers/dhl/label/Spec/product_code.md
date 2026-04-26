# Field: product_code

## Display Name
Product Code

## Field Description
A 2-digit numeric code identifying the DHL Express transport product for the shipment. This is part of the routing barcode's product/feature block and drives service selection during automated sorting and processing.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 2 digits (fixed length)
- **Pattern/Regex:** `\d{2}`
- **Allowed Values:** Defined product codes including: 05 (DOM EUROPACK), 11 (EUROPACK), 48 (EXPRESS WORLDWIDE), 57 (ECONOMY SELECT), among others
- **Required:** yes — mandatory in routing barcode

## Examples from Spec
- `05` — DOM EUROPACK
- `11` — EUROPACK
- `48` — EXPRESS WORLDWIDE
- `57` — ECONOMY SELECT

## ZPL Rendering
- **Typical Position:** Encoded within routing barcode; also part of human-readable routing code
- **Font / Size:** Not specified
- **Field Prefix:** None — positional within routing string after "+" separator
- **ZPL Command:** Encoded within routing barcode (^BC)

## Edge Cases & Notes
- Product/feature block always consists of 8 digits total (product code 2 + delivery date 2 + delivery time 1 + handling feature code 3).
- Part of the mandatory routing barcode structure.

## Claude Confidence
HIGH — explicitly defined with examples in routing barcode structure

## Review Status
- [ ] Reviewed by human