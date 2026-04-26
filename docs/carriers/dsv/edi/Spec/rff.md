# Field: RFF

## Display Name
Reference

## Segment ID
RFF

## Required
yes

## Description
Specifies reference numbers and identifiers for the shipment, including consignment numbers, order references, and various DSV-specific reference types.

## Subfields

### reference_code_qualifier
- **Element Position:** 1.1
- **Pattern/Regex:** (AG|AAM|AAO|AAS|AAU|AWM|BN|CG|CU|SRN|STS|ZAD|ZCP|ZCU|ZDO|ZIR|ZTF|ZHP|ZHT|ZMT|ZRM|ZSM|ZSR|ZUS|ZXX)
- **Required:** yes
- **Description:** Reference code qualifier (C506/1153). Valid codes: AG=Multiple Deliveries Discount ID, AAM=Waybill number, AAO=Consignment identifier consignee assigned, AAS=Transport contract document identifier, AAU=Despatch note document identifier, AWM=Service category reference, BN=Consignment identifier carrier assigned, CG=Consignee's order number, CU=Consignment identifier consignor assigned (mandatory for Track&Trace), SRN=Shipment reference number (GS1 code, 17 chars), STS=StatusText, ZAD=On sight authorization code, ZCP=CLPartnerCode, ZCU=OrderReference, ZDO=DSV ESBDomain, ZIR=InterimReceiptNo, ZTF=Traffic from assigned by Partner, ZHP=AllowHomePortDefaulting, ZHT=HouseBillType, ZMT=DSV specific for Method, ZRM=Receiver Mailbox for Dinas, ZSM=Sender Mailbox for Dinas, ZSR=ShipperReference, ZUS=AllowUpdateShipmentFromBooking, ZXX=Unidentified Reference.

### reference_identifier
- **Element Position:** 1.2
- **Pattern/Regex:** .{1,70}
- **Required:** no
- **Description:** Reference identifier (C506/1154). The actual reference number value. Norwegian waybill (n10), Swedish waybill (n10), document reference, consignor's reference, or EAN consignment number (n17).

### document_line_identifier
- **Element Position:** 1.3
- **Pattern/Regex:** .{1,6}
- **Required:** no
- **Description:** Document line identifier (C506/1156). Only used when RFF C506/1153 = "STS".

### version_identifier
- **Element Position:** 1.4
- **Pattern/Regex:** an..9
- **Required:** no
- **Description:** Version identifier (C506/1056). Not used.

### revision_identifier
- **Element Position:** 1.5
- **Pattern/Regex:** an..6
- **Required:** no
- **Description:** Revision identifier (C506/1060). Not used.

## Edge Cases & Notes
RFF is the trigger segment for SG3, which can occur up to 999 times. CU is mandatory for Track&Trace search on DSV T&T site. AAM is only for Norwegian traffic, AAS only for Swedish traffic and E-services. AAU is for special document reference when mutually agreed. SRN is for GS1 code reference number (17 characters). ZRM and ZSM are for Dinas Road Germany and must be aligned before use. Examples: RFF+AAS:6982842384', RFF+CU:310651', RFF+AG:321654'.

## Claude Confidence
HIGH — spec provides comprehensive list of reference qualifiers and usage notes

## Review Status
- [ ] Reviewed by human