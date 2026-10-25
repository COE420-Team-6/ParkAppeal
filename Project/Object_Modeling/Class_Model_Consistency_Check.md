# Class Model Consistency Check

## 1. Consistency with Requirements and Use Cases

| Use case / requirement | Classes | DFD process / store |
|---|---|---|
| UC-01 Submit Appeal; FR-01, FR-02 | PermitHolder, Appeal, AppealEvidence, AppealService, AppealForm, NotificationService | 3.0, 5.0 / D4 |
| UC-02 Upload Evidence; FR-01 | AppealEvidence, Attachment, AppealService | 3.0 / D4 |
| UC-03 Track Appeal; FR-03 | Appeal, AppealStatus, Dashboard, SearchFilter | 3.0 / D4 |
| UC-04 Review Appeal; FR-04, NFR-02 | AppealsOfficer, Decision, DecisionOutcome, AppealService, ViolationService | 3.0, 2.0 / D4, D3 |
| UC-05 Verify Violation Record; FR-05 | AppealService, Violation | 3.0 / D3 |
| UC-06 Apply for Permit; FR-08 | PermitHolder, PermitApplication, PermitType, Vehicle, PermitService | 1.0 / D1, D2 |
| UC-07 Manage Permit Application | Administrator, PermitApplication, ApplicationStatus, PermitService | 1.0 / D2 |
| UC-08 Renew Parking Permit | PermitHolder, Permit, PermitService | 1.0, 5.0 / D2 |
| UC-09 Search Records; FR-09 | Administrator, ReportService, SearchFilter | 4.0 / D2, D3, D4 |
| UC-10 Receive Status Notification; FR-10 | PermitHolder, NotificationService | 5.0 / D1 |
| UC-11 Look Up Vehicle by Plate; FR-11 | ParkingOfficer, ViolationService, Vehicle, Permit | 2.0 / D1, D2 |
| UC-12 Record Violation; FR-12, NFR-12 | ParkingOfficer, Violation, ViolationType, ViolationService | 2.0, 5.0 / D3 |
| UC-13 Attach Violation Evidence; FR-13 | ViolationEvidence, Attachment, ViolationService | 2.0 / D3 |
| UC-14 Review Unmatched Violations; FR-14 | Administrator, Violation, Vehicle, ViolationService | 2.0 / D1, D3 |
| UC-15 Void Violation; FR-15 | Administrator, VoidRecord, Violation, ViolationService | 2.0 / D3 |
| UC-16 Configure Permit Eligibility; FR-16 | Administrator, PermitType | 1.0 / D2 |
| UC-17 Manage Permit Quota; FR-17 | Administrator, PermitType | 1.0 / D2 |
| UC-18 Review Eligibility Result; FR-18 | Administrator, PermitApplication, PermitService | 1.0 / D2 |
| UC-19 Issue Approved Permit; FR-19 | PermitService, Permit, PermitType, PermitStatus | 1.0, 5.0 / D2 |
| UC-20 Monitor Permit Expiry; FR-20 | Administrator, Permit, PermitStatus, ReportService | 1.0, 4.0 / D2 |
| FR-06, FR-07 (any device, responsive layout) | Page, LoginPage, Dashboard, AppealForm | - |

## 2. Consistency with the DFD and Data Stores

| DFD element | Class model | Status |
|---|---|---|
| Entity: Permit Holder | PermitHolder | Met |
| Entity: Parking Officer | ParkingOfficer | Met |
| Entity: Administrator | Administrator | Met |
| Entity: Appeals Officer | AppealsOfficer | Met |
| Process 1.0 Manage Permit Applications | PermitService | Met |
| Process 2.0 Manage Parking Violations | ViolationService | Met |
| Process 3.0 Process Appeals | AppealService | Met |
| Process 4.0 Search and Report | ReportService, SearchFilter | Met |
| Process 5.0 Manage Notifications | NotificationService | Met |
| D1 User and Vehicle Registry | User and its four subclasses, Vehicle | Met |
| D2 Permit Records | PermitApplication, PermitType, Permit | Met |
| D3 Violation Records | Violation, ViolationEvidence, VoidRecord | Met |
| D4 Appeal Records | Appeal, AppealEvidence, Decision | Met |
| Flow: Violation Void Status (3.0 to D3) | AppealService depends on ViolationService (void on approval) | Met |
| Flows: Permit Status Change, Violation Issued Event, Appeal Status Change | PermitService, ViolationService and AppealService depend on NotificationService | Met |
| Flow: Account Contact Details (D1 to 5.0) | User.email read by NotificationService | Met |
| Flows: Eligibility Criteria and Quota Settings (Administrator to 1.0), Eligibility and Quota Rules (1.0 and D2) | Administrator.configureEligibility() and setQuota(); PermitType in D2 | Met |

## 3. Verification of Relationships and Multiplicities

| Relationship | Multiplicity | Justification |
|---|---|---|
| PermitHolder files Appeal | 1 to 0..* | A holder may file no appeal or many |
| AppealsOfficer reviews Appeal | 0..1 to 0..* | An appeal has no officer until review starts |
| AppealsOfficer records Decision | 1 to 0..* | Every decision is logged with its officer (Process 3.0) |
| Appeal resolved by Decision (composition) | 1 to 0..1 | One decision after review; no escalation (decision 1) |
| Appeal supported by AppealEvidence (composition) | 1 to 0..3 | FR-01: at most 3 attachments |
| Violation is disputed by Appeal | 1 to 0..1 | An appeal must match one existing violation; one appeal per violation |
| ParkingOfficer issues Violation | 1 to 0..* | Every violation is recorded by one officer (UC-12) |
| Violation evidenced by ViolationEvidence (composition) | 1 to 0..5 | FR-13: up to 5 photos, evidence optional |
| Violation voided by VoidRecord | 1 to 0..1 | A violation is voided at most once (FR-15) |
| User records VoidRecord | 1 to 0..* | Administrator (manual) or Appeals Officer (approved appeal), decision 4 |
| Violation recorded against Vehicle | 0..* to 0..1 | 0 is the unmatched plate case (FR-14) |
| PermitHolder owns Vehicle | 1 to 0..* | Vehicles are registered to one account in D1 |
| PermitHolder submits PermitApplication | 1 to 0..* | A holder may apply for several permits |
| Administrator decides PermitApplication | 0..1 to 0..* | Pending applications have no deciding administrator yet |
| PermitApplication for Vehicle | 0..* to 1 | Each application names one vehicle |
| PermitApplication requests PermitType | 0..* to 1 | Each application requests one permit type |
| PermitApplication results in Permit | 1 to 0..1 | Approval issues exactly one permit (Process 1.0) |
| Vehicle holds Permit | 1 to 0..* | A vehicle keeps past (expired) permits |
| Permit of type PermitType | 0..* to 1 | Quota is counted per permit type |
| Inheritance: User to 4 actors; Attachment to 2 evidence classes; Page to 3 pages | - | Genuine generalisations: shared fields and behaviour, specialised rules |

## 4. Check Results

| Check | Status | Evidence |
|---|---|---|
| Class model is consistent with the use cases and requirements | Met | All 20 use cases and FR-01 to FR-20 traced (consistency table) |
| DFD external entities map to actor classes | Met | All four entities (DFD table) |
| Every Level-0 process has a responsible class | Met | Processes 1.0 to 5.0 (DFD table) |
| Every data store maps to persistent classes | Met | D1 to D4 (DFD table) |
| Multiplicities match the requirement limits | Met | Relationship table (0..3, 0..5, 0..1) |
| Inheritance used only for genuine generalisation | Met | Three hierarchies, each with shared fields |
| Consolidated diagram includes all approved classes | Met | C01 to C31 appear in Figure 5 |
| Earlier labs updated for the decisions above | Met | Requirements, Scope and Description files updated; use case diagram and both DFDs redrawn (Figures 6 to 8) |
