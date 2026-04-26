# Field: CNI

## Display Name
Consignment Information

## Segment ID
CNI

## Required
yes

## Description
Identifies a consignment (shipment) within the message, including its sequence number and transport document reference.

## Subfields

### consolidation_item_number
- **Element Position:** 1
- **Pattern/Regex:** \d{1,4}|9999
- **Required:** yes
- **Description:** Sequence number of the consignment within the message. 9999 is used for Commercial Invoice data groups linked to a shipment.

### transport_document_reference
- **Element Position:** 2
- **Pattern/Regex:** .{1,35}(:\d)?
- **Required:** yes
- **Description:** Transport document number composite — the DHL waybill/AWB number, optionally followed by colon and document type code (e.g. 5 = Bill of lading)

## Edge Cases & Notes
CNI appears once per shipment. For BBX scenarios, mother and baby shipments each get their own CNI. CNI+9999 is a special sequence number used for Commercial Invoice data groups that follow the shipment's main CNI group. The waybill number in element 2 may be followed by ':5' indicating the document type.

## Claude Confidence
HIGH — clear from examples and BBX specification

## Review Status
- [ ] Reviewed by human