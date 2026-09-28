# Use Cases

## Mohamad Al Kadi (B00098738) Contributions

- UC-01
- UC-02
- UC-03
- UC-04
- UC-05

## Mehlam Muniwala (B00104714) Contributions

- UC-06
- UC-07
- UC-08
- UC-09
- UC-10

## Jad Zeidan (B00088013) Contributions

- UC-11
- UC-12
- UC-13
- UC-14
- UC-15

## Seyed Moshtagh Moulaei (B00106497) Contributions

- UC-16
- UC-17
- UC-18
- UC-19
- UC-20

## Team Consolidated Use Cases

| UC ID | Use Case Name | Primary Actor | Short Description | Contributor |
| --- | --- | --- | --- | --- |
| UC-01 | Submit Appeal | Permit Holder | Permit Holder wants to dispute a citation and files an appeal against it within a 14-day window, with a reason/evidence. | Mohamad Al Kadi |
| UC-02 | Upload Evidence | Permit Holder | Attaches photos or documents to support an appeal. | Mohamad Al Kadi |
| UC-03 | Track Appeal | Permit Holder | Views the current status and final decision of their appeals. | Mohamad Al Kadi |
| UC-04 | Review Appeal | Appeals Officer | Reviews the citation and evidence, then approves, reduces, or rejects the appeal with a justification. | Mohamad Al Kadi |
| UC-05 | Escalate Appeal | Appeals Committee | Reviews an appeal referred by the officer and records the final decision. | Mohamad Al Kadi |
| UC-06 | Apply for Permit | Applicant | The applicant completes and submits a parking permit application through the ParkAppeal system. | Mehlam Muniwala |
| UC-07 | Manage Permit Application | Administrator | The administrator reviews a permit application and approves or rejects it based on the provided information. | Mehlam Muniwala |
| UC-08 | Renew Parking Permit | Applicant | The applicant renews an existing parking permit before it expires. | Mehlam Muniwala |
| UC-09 | Search Records | Administrator | The administrator searches and filters permits, violations, or appeals using status or date. | Mehlam Muniwala |
| UC-10 | Receive Status Notification | Applicant | The applicant receives a notification when the status of a permit application or appeal changes. | Mehlam Muniwala |
| UC-11 | Look Up Vehicle by Plate | Parking Officer | The officer enters a licence plate during patrol and the system returns the registered vehicle, any linked permit, and that permit's validity status. | Jad Zeidan |
| UC-12 | Record Violation | Parking Officer | The officer issues a violation against a vehicle, selecting the violation type and entering the location. The system stores the record with an issue timestamp. | Jad Zeidan |
| UC-13 | Attach Violation Evidence | Parking Officer | The officer attaches photographs to a violation record at the time of issue to support it if the driver later appeals. | Jad Zeidan |
| UC-14 | Review Unmatched Violations | Administrator | The administrator works through violations issued against plates with no registered vehicle and links a record to an account once the owner is identified. | Jad Zeidan |
| UC-15 | Void Violation | Administrator | The administrator cancels a violation issued in error, recording a written reason. The record is kept marked voided rather than deleted. | Jad Zeidan |
| UC-16 | Configure Permit Eligibility | Administrator | Defines or updates the eligibility criteria for a permit type used when new applications are checked. | Seyed Moshtagh Moulaei |
| UC-17 | Manage Permit Quota | Administrator | Sets the active-permit limit for a permit type and checks current use before issuance. | Seyed Moshtagh Moulaei |
| UC-18 | Review Eligibility Result | Administrator | Opens a pending application and inspects the recorded eligibility result and unmet criteria before deciding it. | Seyed Moshtagh Moulaei |
| UC-19 | Issue Approved Permit | Administrator | Completes an approval by issuing one uniquely numbered permit with valid dates when quota permits. | Seyed Moshtagh Moulaei |
| UC-20 | Monitor Permit Expiry | Administrator | Views permits by validity status and identifies permits whose expiry dates have passed. | Seyed Moshtagh Moulaei |

## Use Case Relationships

| Relationship ID | Base Use Case | Related Use Case | Relationship | Justification |
| --- | --- | --- | --- | --- |
| R-01 | Submit Appeal (UC-01) | Verify Violation Record | `<<include>>` | Every appeal must match a valid citation. |
| R-02 | Submit Appeal (UC-01) | Upload Evidence (UC-02) | `<<extend>>` | Evidence is optional, since some appeals won't have documentation to help case. |
| R-03 | Record Violation (UC-12) | Look Up Vehicle by Plate (UC-11) | `<<include>>` | In order for a violation to be issued or checked for, the Parking Officer must check the plate by running it through the system every time. |
| R-04 | Manage Permit Application (UC-07) | Review Eligibility Result (UC-18) | `<<include>>` | Every permit decision requires the administrator to inspect the recorded eligibility result. UC-07 points to UC-18. |
| R-05 | Manage Permit Application (UC-07) | Issue Approved Permit (UC-19) | `<<extend>>` | Issuance occurs only on the approval branch of UC-07; a rejected application does not issue a permit. UC-19 points to UC-07 at the approval extension point. |
