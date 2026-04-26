# Field: DGS

## Display Name
Dangerous Goods

## Segment ID
DGS

## Required
no

## Description
Dangerous goods segment at line item level (SG33). Required for dangerous goods services. If dangerous goods present but no detailed information available, text "HAZARD" needs to be used.

## Subfields

### dangerous_goods_regulations_code
- **Element Position:** 1
- **Pattern/Regex:** (ADR|IMD)
- **Required:** no
- **Description:** Dangerous goods regulations code — ADR = European agreement for road, IMD = IMO IMDG code. Required for dangerous goods on Road.

### hazard_identification_code
- **Element Position:** 2.1
- **Pattern/Regex:** .{1,7}
- **Required:** no
- **Description:** Hazard identification code. Text "HAZARD" should be entered if structured information is not available. First sub-component of C205.

### additional_hazard_classification_identifier
- **Element Position:** 2.2
- **Pattern/Regex:** .{1,7}
- **Required:** no
- **Description:** Additional hazard classification identifier

### hazard_code_version_identifier
- **Element Position:** 2.3
- **Pattern/Regex:** .{1,10}
- **Required:** no
- **Description:** Hazard code version identifier. For Road, three Sub-Risk values separated by "+" using escape character (e.g. "3?+6.1?+4")

### undg_identifier
- **Element Position:** 3.1
- **Pattern/Regex:** \d{1,4}
- **Required:** no
- **Description:** United Nations Dangerous Goods (UNDG) identifier. First sub-component of C234.

### dangerous_goods_flashpoint_description
- **Element Position:** 3.2
- **Pattern/Regex:** .{1,8}
- **Required:** no
- **Description:** Dangerous goods flashpoint description. Road TMS only caters for 4 characters.

### shipment_flashpoint_degree
- **Element Position:** 4.1
- **Pattern/Regex:** .{1,10}
- **Required:** no
- **Description:** Shipment flashpoint degree. First sub-component of C223. Road TMS only caters for 4 characters.

### flashpoint_measurement_unit_code
- **Element Position:** 4.2
- **Pattern/Regex:** .{1,8}
- **Required:** no
- **Description:** Measurement unit code for flashpoint (e.g. CEL for Celsius)

### packaging_danger_level_code
- **Element Position:** 5
- **Pattern/Regex:** [123]
- **Required:** no
- **Description:** Packaging danger level code — 1 = Great danger, 2 = Medium danger, 3 = Minor danger

### emergency_procedure_for_ships_identifier
- **Element Position:** 6
- **Pattern/Regex:** .{1,6}
- **Required:** no
- **Description:** Emergency procedure for ships identifier

### hazard_medical_first_aid_guide_identifier
- **Element Position:** 7
- **Pattern/Regex:** .{1,4}
- **Required:** no
- **Description:** Hazard medical first aid guide identifier

### transport_emergency_card_identifier
- **Element Position:** 8
- **Pattern/Regex:** .{1,10}
- **Required:** no
- **Description:** Transport emergency card identifier

### orange_hazard_placard_upper_part_identifier
- **Element Position:** 9.1
- **Pattern/Regex:** .{1,4}
- **Required:** no
- **Description:** Orange hazard placard upper part identifier. First sub-component of C235.

### orange_hazard_placard_lower_part_identifier
- **Element Position:** 9.2
- **Pattern/Regex:** .{4}
- **Required:** no
- **Description:** Orange hazard placard lower part identifier

### dangerous_goods_marking_identifier_1
- **Element Position:** 10.1
- **Pattern/Regex:** .{1,4}
- **Required:** no
- **Description:** Dangerous goods marking identifier (first). First sub-component of C236.

### dangerous_goods_marking_identifier_2
- **Element Position:** 10.2
- **Pattern/Regex:** .{1,4}
- **Required:** no
- **Description:** Dangerous goods marking identifier (second)

### dangerous_goods_marking_identifier_3
- **Element Position:** 10.3
- **Pattern/Regex:** .{1,4}
- **Required:** no
- **Description:** Dangerous goods marking identifier (third)

### dangerous_goods_marking_identifier_4
- **Element Position:** 10.4
- **Pattern/Regex:** .{1,4}
- **Required:** no
- **Description:** Dangerous goods marking identifier (fourth, added by DSV spec)

### packing_instruction_type_code
- **Element Position:** 11
- **Pattern/Regex:** .{1,3}
- **Required:** no
- **Description:** Packing instruction type code

### transport_means_description_code
- **Element Position:** 12
- **Pattern/Regex:** .{1,8}
- **Required:** no
- **Description:** Transport means description code. Use "LQ" for limited quantity (Road).

### hazardous_cargo_transport_authorisation_code
- **Element Position:** 13
- **Pattern/Regex:** .{1,3}
- **Required:** no
- **Description:** Hazardous cargo transport authorisation code

### tunnel_restriction_code
- **Element Position:** 14.1
- **Pattern/Regex:** .{1,6}
- **Required:** no
- **Description:** Tunnel Restriction Code. First sub-component of C289.

## Edge Cases & Notes
If ADR, all legally mandatory information must be provided. If dangerous goods present with no detailed info, use DGS++HAZARD'. For Road sub-risks, use escape character "?" before "+" separator. Example: DGS+ADR+9:1:3?+6.1?+4+3082:200+:CEL+3+No Eme+++:0001+++31++E'

## Claude Confidence
MEDIUM — complex segment with many optional composites; positions mapped from spec examples and element ordering

## Review Status
- [ ] Reviewed by human