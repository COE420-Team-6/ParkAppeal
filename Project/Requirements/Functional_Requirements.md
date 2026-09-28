# Functional Requirements

## Mohamad Al Kadi (B00098738) Contributions

- FR-01
- FR-02
- FR-03
- FR-04
- FR-05

## Mehlam Muniwala (B00104714) Contributions

- FR-06
- FR-07
- FR-08
- FR-09
- FR-10

## Jad Zeidan (B00088013) Contributions

- FR-11
- FR-12
- FR-13
- FR-14
- FR-15

## Seyed Moshtagh Moulaei (B00106497) Contributions

- FR-16
- FR-17
- FR-18
- FR-19
- FR-20

## Team Consolidated Requirements

| FR ID | Functional Requirement | Source Scenario/Stakeholder | Contributor |
| --- | --- | --- | --- |
| FR-01 | The system should allow a permit holder to submit an appeal within 14 days of the citation issue date, with a written reason and up to 3 attachments (PDF or JPG, max 5 MB each), and email a confirmation upon submission. | S-01 | Mohamad Al Kadi |
| FR-02 | The system should not allow an appeal to be submitted more than 14 days after the citation date, and should display "Appeal window has passed". | S-02 | Mohamad Al Kadi |
| FR-03 | The system should allow a permit holder to view the status of any appeal they have submitted. | S-01 | Mohamad Al Kadi |
| FR-04 | The system should allow an appeals officer to review a submitted appeal, including the citation record and any attached evidence, and record a decision to approve, reduce, or reject the appeal with a written justification. | UC-04 | Mohamad Al Kadi |
| FR-05 | The system should allow an appeals committee member to review an appeal escalated by an appeals officer and record a final decision that overrides the officer's original decision. | UC-05 | Mohamad Al Kadi |
| FR-06 | The system should allow users to access ParkAppeal from a mobile phone, tablet, or computer. | S-03 | Mehlam Muniwala |
| FR-07 | The system should adjust the interface layout to fit different screen sizes. | S-03 | Mehlam Muniwala |
| FR-08 | The system should allow an applicant to upload required documents directly from their device when applying for a parking permit. | S-03 | Mehlam Muniwala |
| FR-09 | The system shall allow users to search and filter permits, violations, and appeals by status or date. | S-03 | Mehlam Muniwala |
| FR-10 | The system shall send a notification to the applicant when a permit application or appeal status changes. | S-03 | Mehlam Muniwala |
| FR-11 | The system shall allow an authenticated parking officer to search for a vehicle by licence plate number and display any linked permit, its type, and its validity status. | S-04 | Jad Zeidan |
| FR-12 | The system shall allow a parking officer to record a violation against a vehicle by selecting a violation type from a predefined list and entering the location, and shall store the date and time of issue on the violation record. | S-04 | Jad Zeidan |
| FR-13 | The system shall allow a parking officer to attach up to 5 photographs (JPG or PNG, max 5 MB each) as evidence to a violation record at the time of issue. | S-04 | Jad Zeidan |
| FR-14 | The system shall create a violation record without a permit or account link when the entered licence plate matches no registered vehicle, and shall mark that record as "unmatched" for administrator review. | S-05 | Jad Zeidan |
| FR-15 | The system shall not allow a violation record to be edited or deleted after it has been issued, and shall allow an administrator to void a violation with a written reason while keeping the original record. | UC-15 | Jad Zeidan |
| FR-16 | The system shall allow an authorized administrator to configure eligibility criteria for each permit type and save the criteria used to evaluate new applications. | S-06 | Seyed Moshtagh Moulaei |
| FR-17 | The system shall allow an authorized administrator to set the maximum number of active permits for each permit type and display the number currently issued against that quota. | S-06 | Seyed Moshtagh Moulaei |
| FR-18 | For each submitted permit application, the system shall evaluate the applicant and vehicle information against the eligibility criteria configured for the selected permit type and display the result and unmet criteria to the administrator. | S-06 | Seyed Moshtagh Moulaei |
| FR-19 | When an administrator approves an eligible application and the permit type has available quota, the system shall issue exactly one permit linked to the application, applicant, and vehicle, with a unique permit number, start date, expiry date, and Active status. | S-06 | Seyed Moshtagh Moulaei |
| FR-20 | When the current date is later than a permit's expiry date, the system shall show that permit as Expired in permit details and administrator search results. | S-06 | Seyed Moshtagh Moulaei |
