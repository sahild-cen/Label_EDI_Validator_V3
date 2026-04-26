# Field: ups_account_number

## Display Name
UPS Account Number

## Group Description
The unique number assigned by UPS to the shipper, embedded in positions 3-8 of the Tracking Number.

## Sub-Fields

### ups_account_number
- **Data Type:** alphanumeric
- **Length:** 6 (positions 3-8 of tracking number)
- **Pattern/Regex:** Not specified in spec
- **Allowed Values:** UPS-assigned shipper account numbers
- **Required:** yes (embedded in tracking number; also listed on submission form)
- **Description:** The unique 6-character shipper account number assigned by UPS. Embedded within the tracking number at positions 3-8. Multiple account numbers can be included on the submission form if they are for the same customer name and address.
- **Detect By:** Extracted from tracking number positions 3-8
- **Position on Label:** Embedded within tracking number; may also appear separately
- **ZPL Font:** Not specified
- **Field Prefix:** None
- **ZPL Command:** ^FD (text field)

## Examples from Spec
No examples in spec (this extract).

## Edge Cases & Notes
- Multiple UPS account numbers can be used for a single customer location but must all be listed on the submission form.
- The number of UPS accounts used does not affect the total number of test labels required for certification.

## Claude Confidence
MEDIUM — Definition clearly states position and length; display format on label not detailed in this extract.

## Review Status
- [x] Reviewed by human