# Field: GID

## Display Name
Goods Item Details

## Segment ID
GID

## Required
yes

## Description
Identifies a goods item within the shipment with package count and type. At least one GID group is mandatory.

## Subfields

### goods_item_number
- **Element Position:** 1
- **Pattern/Regex:** \d{1,6}
- **Required:** yes
- **Description:** Goods item number — sequential line item number

### package_quantity
- **Element Position:** 2.1
- **Pattern/Regex:** \d{1,8}
- **Required:** no
- **Description:** Package quantity (composite C213 first occurrence, sub-element 7224). Number of packages at shipment level (CNT+11) or for each line item is required for Road.

### package_type_description_code
- **Element Position:** 2.2
- **Pattern/Regex:** .{1,17}
- **Required:** yes
- **Description:** Package type description code (composite C213 first occurrence, sub-element 7065). Required for Road. E.g., PLL=Pallet.

### packaging_related_description_code_5th_c213
- **Element Position:** 6.6
- **Pattern/Regex:** (INR)?
- **Required:** no
- **Description:** Packaging related description code on the 5th C213 composite (sub-element 7233). INR=InnerGoodsItems. Used for Air/Sea to indicate SG19 is nested for inner goods items.

## Edge Cases & Notes
At least one GID group is mandatory. The segment supports up to 5 C213 composites but only the first and fifth are used in implementation. Example: GID+1+1:PLL' or GID+1+9:PLL++++:::::INR'

## Claude Confidence
MEDIUM — structure is complex with multiple C213 repetitions; key used elements are clear but the 5th composite positioning is unusual

## Review Status
- [ ] Reviewed by human