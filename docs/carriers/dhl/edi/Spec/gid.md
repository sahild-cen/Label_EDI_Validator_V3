# Field: GID

## Display Name
Goods Item Details

## Segment ID
GID

## Required
yes

## Description
Identifies a goods item (piece/package) within a consignment, including package type and quantity.

## Subfields

### goods_item_number
- **Element Position:** 1
- **Pattern/Regex:** \d{1,5}
- **Required:** no
- **Description:** Sequential goods item number within the consignment. May be empty for piece-level entries, or contain a sequence number (e.g. 1, 2, 0010, 0020) for invoice line items.

### number_and_type_of_packages
- **Element Position:** 2
- **Pattern/Regex:** \d{1,8}:[A-Z]{2}
- **Required:** yes
- **Description:** Number of packages and package type code composite — quantity:type (e.g. 1:CT for 1 carton, 1:PK for 1 package)

## Edge Cases & Notes
GID appears at piece level within consignment. For standard shipments, element 1 is a sequence number. For invoice line items (under CNI+9999), the sequence aligns with line item numbers (e.g. 0010, 0020). Package type codes: CT = Carton, PK = Package. When element 1 is empty (GID++1:CT), the piece is identified by its associated GIN barcode.

## Claude Confidence
HIGH — consistent pattern across all examples

## Review Status
- [ ] Reviewed by human