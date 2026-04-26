# Field: UNB

## Display Name
Interchange Header

## Segment ID
UNB

## Required
yes

## Description
Identifies the interchange sender, recipient, and preparation date/time for the EDI interchange envelope.

## Subfields

### syntax_identifier
- **Element Position:** 1.1
- **Pattern/Regex:** UNOC
- **Required:** yes
- **Description:** Syntax identifier — UNOC means uppercase and lowercase characters A-Z, a-z, including western European special characters

### syntax_version_number
- **Element Position:** 1.2
- **Pattern/Regex:** 4
- **Required:** yes
- **Description:** Syntax version number — 4 = Version 4

### interchange_sender_identification
- **Element Position:** 2.1
- **Pattern/Regex:** .{1,35}
- **Required:** yes
- **Description:** Sender identification

### sender_identification_code_qualifier
- **Element Position:** 2.2
- **Pattern/Regex:** (14|ZZ)
- **Required:** no
- **Description:** Identification code qualifier — 14 = GS1, ZZ = Mutually defined

### interchange_recipient_identification
- **Element Position:** 3.1
- **Pattern/Regex:** .{1,35}
- **Required:** yes
- **Description:** Interchange recipient identification — DSV recipient ID is 5790000110018

### recipient_identification_code_qualifier
- **Element Position:** 3.2
- **Pattern/Regex:** 14
- **Required:** yes
- **Description:** Identification code qualifier — 14 = GS1

### date_of_preparation
- **Element Position:** 4.1
- **Pattern/Regex:** \d{8}
- **Required:** yes
- **Description:** Date of preparation in format CCYYMMDD

### time_of_preparation
- **Element Position:** 4.2
- **Pattern/Regex:** \d{4}
- **Required:** yes
- **Description:** Time of preparation in format HHMM

### interchange_control_reference
- **Element Position:** 5
- **Pattern/Regex:** .{1,14}
- **Required:** yes
- **Description:** Interchange control reference — unique reference for the interchange

### test_indicator
- **Element Position:** 11
- **Pattern/Regex:** 1
- **Required:** no
- **Description:** Test indicator — 1 = Interchange is a test. Used as unique setup requirement, does not route to different systems.

## Edge Cases & Notes
Example: UNB+UNOC:4+5912345678901:14+5790000110018:14+20151007:1147+321654++++++1'
DSV recipient ID is always 5790000110018.

## Claude Confidence
HIGH — spec clearly defines all used elements with examples

## Review Status
- [ ] Reviewed by human