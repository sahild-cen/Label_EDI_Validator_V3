# Field: MEA

## Display Name
Measurements

## Segment ID
MEA

## Required
yes

## Description
Specifies measurements related to goods items, including weights, volumes, counts, and dangerous goods measurements. Used in multiple contexts within SG21 (goods item level) and SG35 (dangerous goods level).

## Subfields

### measurement_purpose_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** (WT|CT|VOL|LMT)
- **Required:** yes
- **Description:** Measurement purpose code qualifier. Valid codes: WT = Weights, CT = Counts, VOL = Volume, LMT = Limits

### measured_attribute_code
- **Element Position:** 2.1
- **Pattern/Regex:** (AAF|AFN|AAB|ADZ|SQ|ZOT)?
- **Required:** no
- **Description:** Measured attribute code (composite C502, first sub-component). Valid codes: AAF = Net net weight, AFN = Net explosive weight, AAB = Goods item gross weight, ADZ = Adjusted gross weight, SQ = Sequence, ZOT = Other count. May be empty (e.g., for CT counts or VOL).

### measurement_significance_code
- **Element Position:** 2.2
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Measurement significance code — Not used

### non_discrete_measurement_name_code
- **Element Position:** 2.3
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Non-discrete measurement name code — Not used

### non_discrete_measurement_name
- **Element Position:** 2.4
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Non-discrete measurement name — Not used

### measurement_unit_code
- **Element Position:** 3.1
- **Pattern/Regex:** (KGM|LTR|MTQ|MTR|PLL|NMP|BAG|BOB|BOX|CP|DRM|IBC|JCN|LGM|PD|SB|CMT)
- **Required:** yes
- **Description:** Measurement unit code (composite C174, first sub-component). Valid codes include: KGM = kilogram, LTR = litre, MTQ = cubic metre, MTR = metre, PLL = pallet, NMP = number of packs, and DGS package types (BAG, BOB, BOX, CP, DRM, IBC, JCN, LGM, PD, SB)

### measure
- **Element Position:** 3.2
- **Pattern/Regex:** .{1,18}
- **Required:** yes
- **Description:** The measured value (composite C174, second sub-component)

### range_minimum_quantity
- **Element Position:** 3.3
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Range minimum quantity — Not used

### range_maximum_quantity
- **Element Position:** 3.4
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Range maximum quantity — Not used

### significant_digits_quantity
- **Element Position:** 3.5
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Significant digits quantity — Not used

### surface_or_layer_code
- **Element Position:** 4
- **Pattern/Regex:** .{0}
- **Required:** no
- **Description:** Surface or layer code — Not used

## Edge Cases & Notes
MEA appears in multiple segment groups with different purpose codes:
- SG21 (goods item level): MEA+WT+AAB (gross weight), MEA+VOL (volume), MEA+LMT (limits/length), MEA+WT+ADZ (adjusted weight), MEA+CT+SQ (sequence count), MEA+CT+ZOT (other count)
- SG35 (DGS level, max 9 occurrences): MEA+WT+AAF (net net weight), MEA+WT+AFN (net explosive weight), MEA+CT (DGS package count), MEA+VOL (DGS volume), MEA+WT+AAB (DGS gross weight)
When measured_attribute_code is empty, element position 2 may be omitted entirely (e.g., MEA+CT++BAG:1 or MEA+VOL++LTR:1).

## Claude Confidence
HIGH — spec clearly defines all variants with examples

## Review Status
- [ ] Reviewed by human