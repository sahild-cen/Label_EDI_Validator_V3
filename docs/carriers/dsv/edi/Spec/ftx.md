# Field: FTX

## Display Name
Free Text

## Segment ID
FTX

## Required
no

## Description
Provides free text information including goods descriptions, handling instructions, delivery instructions, loading remarks, and various DSV-specific text fields.

## Subfields

### text_subject_code_qualifier
- **Element Position:** 1
- **Pattern/Regex:** (AAA|AAI|AEB|BLR|CLR|HAN|IDS|MKS|PAY|RPT|SIC|SPH|ZAD|ZAW|ZBL|ZCF|ZDM|ZFP|ZPT|ZLR|ZTF)
- **Required:** yes
- **Description:** Text subject code qualifier (4451). Valid codes: AAA=Goods item description, AAI=General information, AEB=Temperature control instructions, BLR=Transport contract document remark/Delivery instruction, CLR=Loading remarks/Pickup instructions, HAN=Consignment handling instruction, IDS=IDS Service code, MKS=Additional marks/numbers, PAY=Payables information, RPT=Report information, SIC=Consignment documentary instruction/Special instruction, SPH=Special handling, ZAD=Additional details, ZAW=Air Waybill Notes, ZBL=Delivery instructions, ZCF=CustomField, ZDM=DropMode, ZFP=Freight payer, ZPT=PassThrough, ZLR=Loading remarks, ZTF=Traffic from.

### free_text_function_code
- **Element Position:** 2
- **Pattern/Regex:** (PCK|DEL)
- **Required:** no
- **Description:** Free text function code (4453). Valid codes: PCK=DropMode Pickup, DEL=DropMode Delivery.

### free_text_description_code
- **Element Position:** 3.1
- **Pattern/Regex:** an..17
- **Required:** no
- **Description:** Free text description code (C107/4441). Dependent — not used in standard setups for Air, Road, Sea, or Courier.

### free_text_description_code_list
- **Element Position:** 3.2
- **Pattern/Regex:** an..17
- **Required:** no
- **Description:** Code list identification code (C107/1131). Not used.

### free_text_description_agency
- **Element Position:** 3.3
- **Pattern/Regex:** an..3
- **Required:** no
- **Description:** Code list responsible agency code (C107/3055). Not used.

### free_text_1
- **Element Position:** 4.1
- **Pattern/Regex:** .{1,512}
- **Required:** no
- **Description:** Free text line 1 (C108/4440). Transport instructions, document remarks, loading remarks, or other text content up to 512 characters.

### free_text_2
- **Element Position:** 4.2
- **Pattern/Regex:** .{1,512}
- **Required:** no
- **Description:** Free text line 2 (C108/4440). Additional text up to 512 characters.

### free_text_3
- **Element Position:** 4.3
- **Pattern/Regex:** .{1,512}
- **Required:** no
- **Description:** Free text line 3 (C108/4440). Additional text up to 512 characters.

### free_text_4
- **Element Position:** 4.4
- **Pattern/Regex:** .{1,512}
- **Required:** no
- **Description:** Free text line 4 (C108/4440). Additional text up to 512 characters.

### free_text_5
- **Element Position:** 4.5
- **Pattern/Regex:** .{1,512}
- **Required:** no
- **Description:** Free text line 5 (C108/4440). Additional text up to 512 characters.

### language_name_code
- **Element Position:** 5
- **Pattern/Regex:** an..3
- **Required:** no
- **Description:** Language name code (3453). Not used.

### free_text_format_code
- **Element Position:** 6
- **Pattern/Regex:** an..3
- **Required:** no
- **Description:** Free text format code (4447). Not used.

## Edge Cases & Notes
FTX can occur up to 99 times. Goods description is required at shipment level (FTX+AAA) or for each line item (SG19 FTX+AAA) for Road. SIC is for driver instructions at pick-up, BLR for transport document remarks, CLR for handling remarks. ZBL can be used instead of BLR to keep each 4440 in separate fields. IDS is used for IDS Service codes. ZTF and ZCF must be aligned before use. Different products may have different text field limitations. Use '?' as release character for special characters in text (e.g., 12?:00). Examples: FTX+SIC+++OBS! GLASS!', FTX+CLR+++udlev,.ref 102188', FTX+IDS+++97:DEL:06.02.2021 12?:00'.

## Claude Confidence
HIGH — spec provides extensive detail on qualifiers and usage

## Review Status
- [ ] Reviewed by human