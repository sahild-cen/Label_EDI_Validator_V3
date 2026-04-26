# Field: CTA

## Display Name
Contact Information

## Segment ID
CTA

## Required
no

## Description
To specify a person within a party. Used in SG5 (consignor contact) and SG44 (consignee/receiver contact).

## Subfields

### contact_function_code
- **Element Position:** 1
- **Pattern/Regex:** (CO|AC|IC)
- **Required:** yes
- **Description:** Contact function code. 'CO' = Consignor Contact (SG5), 'AC' = Accepting contact for product feature 'Delivery limited to receiver' (SG44), 'IC' = Contact information (general purpose).

### department_or_employee_name_code
- **Element Position:** 2.1
- **Pattern/Regex:** .*
- **Required:** no
- **Description:** Department or employee name code — Not used.

### department_or_employee_name
- **Element Position:** 2.2
- **Pattern/Regex:** .{1,35}
- **Required:** yes
- **Description:** Department or employee name. Contains the contact person name.

## Edge Cases & Notes
In SG44, this segment group is mandatory for product feature 'Delivery limited to receiver' because it holds the name of the person to whom delivery must be accomplished. In SG5, it contains shipper/consignor contact information.

## Claude Confidence
HIGH — spec clearly defines usage in both SG5 and SG44 contexts

## Review Status
- [ ] Reviewed by human