# Field: customer_logo

## Display Name
Customer Logo

## Field Description
An optional graphic element reserved for a customer's logo, placed to the right of the sender address segment. Alternatively, this space can be used for a DHL Initiative Logo (e.g., GoGreen) if the customer agrees or requests it.

## Format & Validation Rules
- **Data Type:** graphic/image
- **Length:** N/A
- **Pattern/Regex:** N/A
- **Allowed Values:** Customer-provided logo image or DHL Initiative Logo (e.g., GoGreen)
- **Required:** no

## Examples from Spec
"This is reserved for an optional Customer Logo or alternatively for a DHL Initiative Logo (e.g. GoGreen) if customer agrees or asks for it."

## ZPL Rendering
- **Typical Position:** to the right of the Ship From address segment; also available near the Ship To area
- **Font / Size:** N/A — graphic element
- **Field Prefix:** None
- **ZPL Command:** ^GFA (graphic field)

## Edge Cases & Notes
This space appears in two locations on the label — near the Ship From address and near the Ship To address. In both cases, it can be used for either a Customer Logo or a DHL Initiative Logo. The customer must agree to or request a DHL Initiative Logo.

## Claude Confidence
HIGH — clearly described as optional in spec

## Review Status
- [x] Reviewed by human