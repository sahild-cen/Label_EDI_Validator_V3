# Field: product_code

## Display Name
Product Code

## Field Description
A 2-digit numeric code representing the DHL transport product type, encoded within the routing barcode.

## Format & Validation Rules
- **Data Type:** numeric
- **Length:** 2 digits (fixed length)
- **Pattern/Regex:** `\d{2}`
- **Allowed Values:** Specific product codes per DHL product catalog (examples: 05 = DOM EUROPACK, 11 = EUROPACK, 48 = EXPRESS WORLDWIDE, 57 = ECONOMY SELECT)
- **Required:** yes (mandatory in routing barcode)

## Examples from Spec
- `11` — EUROPACK
- `05` — DOM EUROPACK
- `57` — ECONOMY SELECT
- `48` — EXPRESS WORLDWIDE

## Position on Label
Within the routing barcode, immediately after the "+" field separator.

## Edge Cases & Notes
- A product/feature block always consists of 8 digits total (product code 2 + delivery date 2 + delivery time 1 + handling feature codes 3).
- The full list of product codes is not provided in the extracted text.

## Claude Confidence
HIGH — Spec provides clear format definition and multiple examples with product names.

## Review Status
- [ ] Reviewed by human