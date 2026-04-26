# Field: FTX (Proper Shipping Name)

## Display Name
Free Text - Proper Shipping Name

## Segment ID
FTX

## Required
no

## Description
Free text segment within DGS group (SG33) for Proper Shipping Name of dangerous goods.

## Subfields

### text_subject_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** AAD
- **Required:** yes
- **Description:** Text subject code qualifier — AAD = Proper Shipping Name

### free_text_function_code
- **Element Position:** 2
- **Pattern/Regex:** .{1,3}
- **Required:** no
- **Description:** Free text function code

### text_literal_1
- **Element Position:** 4.1
- **Pattern/Regex:** .{1,512}
- **Required:** yes
- **Description:** Free text line 1 — Proper Shipping Name (first sub-component of C108)

### text_literal_2
- **Element Position:** 4.2
- **Pattern/Regex:** .{1,512}
- **Required:** no
- **Description:** Free text line 2

### text_literal_3
- **Element Position:** 4.3
- **Pattern/Regex:** .{1,512}
- **Required:** no
- **Description:** Free text line 3

### text_literal_4
- **Element Position:** 4.4
- **Pattern/Regex:** .{1,512}
- **Required:** no
- **Description:** Free text line 4

### text_literal_5
- **Element Position:** 4.5
- **Pattern/Regex:** .{1,512}
- **Required:** no
- **Description:** Free text line 5

## Edge Cases & Notes
Example: FTX+AAD+++Environmentally hazardous substance, liquid, n.o.s.:BISPHENOL A EPOXY RESIN'

## Claude Confidence
HIGH — spec clearly defines all elements

## Review Status
- [ ] Reviewed by human