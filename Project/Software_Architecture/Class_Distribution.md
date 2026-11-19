# Class Distribution

All 31 classes of the Lab 5 consolidated class diagram are assigned, each to exactly one primary component. Classes are grouped by the DFD process or data store they belong to.

## 1. Class Distribution Table

| ID | Component Name | Responsibilities | Included Classes |
|---|---|---|---|
| CO1 | User Interface | Shows the pages and forms for the four roles on phones, tablets and computers. Logs users in and out (15-minute inactivity logout). Validates forms before submission, shows success and error messages, and passes each user action to the business component that handles it. | Page, LoginPage, Dashboard, AppealForm |
| CO2 | Permit Management | Accepts permit applications with documents, evaluates them against the eligibility criteria of the permit type, and lets the Administrator approve or reject them. Issues and renews permits within the quota (one permit per approved application), tracks validity and expiry, configures eligibility criteria and quotas, and gives the permit status of a vehicle to Violation Management. | PermitService, PermitApplication, PermitType, Permit, Vehicle, ApplicationStatus, PermitStatus |
| CO3 | Violation Management | Looks up vehicles by licence plate and shows their permit status. Records violations with type, location and issue time, only for Parking Officer or Administrator accounts, and attaches up to 5 photographs. Marks unmatched plates for review and links them to vehicles later. Voids violations with a reason while keeping the original record and the audit trail, and gives violation records to Appeal Management. | ViolationService, Violation, ViolationEvidence, VoidRecord, ViolationType |
| CO4 | Appeal Management | Accepts appeals within 14 days of the issue date with a reason and up to 3 files, after verifying the violation record. Tracks appeal status for the Permit Holder, lets Appeals Officers review an appeal and record a decision with a justification, and voids the violation when an appeal is approved. | AppealService, Appeal, AppealEvidence, Decision, AppealStatus, DecisionOutcome |
| CO5 | Search and Reporting | Searches and filters permits, violations and appeals by status or date for the Administrator, and generates reports for a date range. Reads the permit, violation and appeal records without changing them. | ReportService, SearchFilter |
| CO6 | Accounts and Common Services | Stores user accounts and their roles (D1) and authenticates users. Supplies the account and role that the business components check before an action. Sends the submission confirmation and the status change notifications to permit holders by email. Defines the common Attachment base class that validates the type and size of evidence files. | User, PermitHolder, AppealsOfficer, ParkingOfficer, Administrator, Attachment, NotificationService |

## 2. Class to Component

| Class (Lab 5) | Component | Reason |
|---|---|---|
| Page | CO1 User Interface | Abstract base of all pages (<<UI>> in Lab 5). |
| LoginPage | CO1 User Interface | Login form. Calls IAuthentication. |
| Dashboard | CO1 User Interface | Role home page. Calls the business interfaces. |
| AppealForm | CO1 User Interface | Appeal form and its validation (Lab 6 Figure 1, Lab 7 Figure 1). |
| PermitService | CO2 Permit Management | Process 1.0 service. |
| PermitApplication | CO2 Permit Management | Application record (D2). |
| PermitType | CO2 Permit Management | Eligibility criteria and quota of a permit type (D2). |
| Permit | CO2 Permit Management | Issued permit and its validity (D2). |
| Vehicle | CO2 Permit Management | Holds the permits of a vehicle (getActivePermit). Stored in D1, but used only with permits. |
| ApplicationStatus | CO2 Permit Management | Status values of PermitApplication. |
| PermitStatus | CO2 Permit Management | Status values of Permit. |
| ViolationService | CO3 Violation Management | Process 2.0 service. |
| Violation | CO3 Violation Management | Violation record (D3). |
| ViolationEvidence | CO3 Violation Management | Photographs of a violation (D3). |
| VoidRecord | CO3 Violation Management | Reason and actor for a voided violation (D3). |
| ViolationType | CO3 Violation Management | Predefined violation types (FR-12). |
| AppealService | CO4 Appeal Management | Process 3.0 service. |
| Appeal | CO4 Appeal Management | Appeal record (D4). |
| AppealEvidence | CO4 Appeal Management | Files of an appeal (D4). |
| Decision | CO4 Appeal Management | Appeals Officer decision and justification (D4). |
| AppealStatus | CO4 Appeal Management | Status values of Appeal. |
| DecisionOutcome | CO4 Appeal Management | Outcome values of Decision. |
| ReportService | CO5 Search and Reporting | Process 4.0 service. |
| SearchFilter | CO5 Search and Reporting | Search criteria passed to ReportService. Placed here, not in CO1, so that CO5 does not depend on the Presentation Layer. |
| User | CO6 Accounts and Common Services | Abstract account with authentication (D1). |
| PermitHolder | CO6 Accounts and Common Services | Account role (D1). |
| AppealsOfficer | CO6 Accounts and Common Services | Account role (D1). |
| ParkingOfficer | CO6 Accounts and Common Services | Account role (D1). |
| Administrator | CO6 Accounts and Common Services | Account role (D1). |
| Attachment | CO6 Accounts and Common Services | Common base class of AppealEvidence and ViolationEvidence, used by CO3 and CO4. |
| NotificationService | CO6 Accounts and Common Services | Process 5.0 service, used by CO2, CO3 and CO4. |

## 3. Summary

| ID | Component Name | Layer | Classes |
|---|---|---|---|
| CO1 | User Interface | Presentation | 4 |
| CO2 | Permit Management | Business Logic | 7 |
| CO3 | Violation Management | Business Logic | 5 |
| CO4 | Appeal Management | Business Logic | 6 |
| CO5 | Search and Reporting | Business Logic | 2 |
| CO6 | Accounts and Common Services | Foundation | 7 |
|  | Total |  | 31 |
