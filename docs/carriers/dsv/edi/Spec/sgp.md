# Field: SGP

## Display Name
Split Goods Placement

## Segment ID
SGP

## Required
no

## Description
Split goods placement segment at line item level (SG30). For Road: identifies masterpallet ID the GID items are on. For Sea: identifies the container the GID segment is related to.

## Subfields

### equipment_identifier
- **Element Position:** 1.1
- **Pattern/Regex:** .{1,17}
- **Required:** no
- **Description:** Equipment identifier — masterpallet ID (Road) or container ID (Sea). First sub-component of C237.

## Edge Cases & Notes
For Road shipments, identifies masterpallet ID. For Sea shipments, identifies the container. Examples: SGP+2007342059', SGP+ABCD1234567'

## Claude Confidence
HIGH — spec clearly defines all elements

## Review Status
- [ ] Reviewed by human