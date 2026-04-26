# Field: GOR

## Display Name
Governmental Requirements

## Segment ID
GOR

## Required
yes

## Description
A segment to indicate applicable governmental procedures related to import, export, and transport of the goods, including document function indication.

## Subfields

### transport_movement_code
- **Element Position:** 1
- **Pattern/Regex:** .{1,3}
- **Required:** yes
- **Description:** Transport movement code — e.g. identifies if import or export procedures apply

### government_action_code
- **Element Position:** 2
- **Pattern/Regex:** .{0,3}
- **Required:** no
- **Description:** Government action code — type of governmental action required

### government_involvement_code
- **Element Position:** 3
- **Pattern/Regex:** .{0,3}
- **Required:** no
- **Description:** Government involvement code

### government_action_code_2
- **Element Position:** 4
- **Pattern/Regex:** .{0,3}
- **Required:** no
- **Description:** Government action code — additional governmental action

## Edge Cases & Notes
GOR appears in SG33 at both Shipment level (max 1) and Invoice level (max 1). At invoice level, the FTX segment may follow with supplementary information such as Trading Transaction Type.

## Claude Confidence
MEDIUM — spec mentions GOR but provides limited detail on specific element values

## Review Status
- [ ] Reviewed by human