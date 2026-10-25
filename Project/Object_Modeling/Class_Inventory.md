# Class Inventory

## Mohamad Al Kadi (B00098738) Contributions

- C01 User
- C02 PermitHolder
- C03 AppealsOfficer
- C04 Appeal
- C05 Evidence
- C06 Decision
- C07 AppealService
- C09 AppealStatus (enum)
- C10 DecisionOutcome (enum)

## Mehlam Muniwala (B00104714) Contributions

- C20 Dashboard
- C21 LoginPage
- C22 AppealForm
- C23 SearchFilter
- C24 Page (abstract)

## Jad Zeidan (B00088013) Contributions

- C11 ParkingOfficer
- C12 Administrator
- C13 Violation
- C14 ViolationEvidence
- C15 VoidRecord
- C16 ViolationService
- C19 ViolationType (enum)

## Seyed Moshtagh Moulaei (B00106497) Contributions

- C18 Permit
- C26 PermitApplication
- C27 PermitType
- C28 PermitService
- C30 ApplicationStatus (enum)
- C31 PermitStatus (enum)

## Team Consolidated Classes

| Class ID | Class Name | Purpose/Responsibility | Related Use Case(s) | Contributor |
|---|---|---|---|---|
| C01 | User | Abstract base class for logged-in users, handles authentication | UC-01 to UC-04 | Mohamad Al Kadi |
| C02 | PermitHolder | Files appeals, uploads evidence, views appeal status | UC-01, UC-02, UC-03 | Mohamad Al Kadi |
| C03 | AppealsOfficer | Reviews appeals, records decisions | UC-04 | Mohamad Al Kadi |
| C04 | Appeal | One appeal: violation ID, reason, date, status, evidence, decision | UC-01, UC-03, UC-04 | Mohamad Al Kadi |
| C05 | Evidence | One PDF/JPG attachment with type and size validation | UC-01, UC-02 | Mohamad Al Kadi |
| C06 | Decision | Outcome, justification, adjusted fine, time | UC-03, UC-04 | Mohamad Al Kadi |
| C07 | AppealService | Window and attachment rules, violation check, decision flow | UC-01 to UC-04 | Mohamad Al Kadi |
| C08 | NotificationService | Reference class (Process 5.0): confirmation and status-change messages | UC-01, UC-03 | Mohamad Al Kadi |
| C09 | AppealStatus (enum) | SUBMITTED, UNDER_REVIEW, DECIDED | UC-03 | Mohamad Al Kadi |
| C10 | DecisionOutcome (enum) | APPROVED, REDUCED, REJECTED | UC-04 | Mohamad Al Kadi |
| C11 | ParkingOfficer | Looks up plates, issues violations, attaches photographs | UC-11, UC-12, UC-13 | Jad Zeidan |
| C12 | Administrator | Reviews unmatched violations, links them to accounts, voids violations | UC-14, UC-15 | Jad Zeidan |
| C13 | Violation | One violation: plate, type, location, issue time, fine, void state | UC-12, UC-14, UC-15 | Jad Zeidan |
| C14 | ViolationEvidence | One JPG/PNG photograph with type and size | UC-13 | Jad Zeidan |
| C15 | VoidRecord | Void reason, acting administrator and time | UC-15 | Jad Zeidan |
| C16 | ViolationService | Role check, mandatory plate lookup, evidence limits, unmatched path and immutability | UC-11 to UC-15 | Jad Zeidan |
| C17 | Vehicle | Reference class (D1): plate and owner link | UC-11, UC-14 | Jad Zeidan |
| C18 | Permit | Reference class (D2): validity status shown at lookup | UC-11 | Jad Zeidan |
| C19 | ViolationType (enum) | EXPIRED_PERMIT, NO_VALID_PERMIT, RESERVED_BAY, OBSTRUCTING_ACCESS, OUTSIDE_MARKED_BAY | UC-12 | Jad Zeidan |
| C01 | User | Reference class (Appeals model): abstract base, officer and administrator inherit from it | UC-11 to UC-15 | Jad Zeidan |
| C04 | Appeal | Reference class (D4): may dispute a violation | UC-12 | Jad Zeidan |
| C08 | NotificationService | Reference class (Process 5.0): violation-issued message | UC-12 | Jad Zeidan |
| C20 | Dashboard | Displays the user's appeals, violations and recent updates | UC-03, UC-10 | Mehlam Muniwala |
| C21 | LoginPage | Lets users enter their credentials and access the platform | UC-01 to UC-20 | Mehlam Muniwala |
| C22 | AppealForm | Collects appeal details and evidence before submission | UC-01, UC-02 | Mehlam Muniwala |
| C23 | SearchFilter | Lets users search and filter appeals by status and date | UC-03, UC-09 | Mehlam Muniwala |
| C24 | Page (abstract) | Common base for UI pages: title and render() | UC-01 to UC-20 | Mehlam Muniwala |
| C18 | Permit | One issued permit: unique number, start and expiry dates, Active or Expired status | UC-19, UC-20 | Seyed Moshtagh Moulaei |
| C26 | PermitApplication | One permit application: vehicle, type, documents, status, eligibility result and unmet criteria | UC-18, UC-19 | Seyed Moshtagh Moulaei |
| C27 | PermitType | Eligibility criteria and active-permit quota for one permit type | UC-16, UC-17 | Seyed Moshtagh Moulaei |
| C28 | PermitService | Evaluates eligibility, checks quota, issues permits and lists permits by validity | UC-16 to UC-20 | Seyed Moshtagh Moulaei |
| C30 | ApplicationStatus (enum) | PENDING, APPROVED, REJECTED | UC-18, UC-19 | Seyed Moshtagh Moulaei |
| C31 | PermitStatus (enum) | ACTIVE, EXPIRED | UC-19, UC-20 | Seyed Moshtagh Moulaei |
| C01 | User | Reference class (Appeals model): abstract base for all actors | UC-16 to UC-20 | Seyed Moshtagh Moulaei |
| C12 | Administrator | Reference class (Violation Enforcement model): configures permit types and decides applications | UC-16 to UC-20 | Seyed Moshtagh Moulaei |
| C02 | PermitHolder | Reference class (Appeals model): submits the applications that are evaluated | UC-18, UC-19 | Seyed Moshtagh Moulaei |
| C17 | Vehicle | Reference class (D1): vehicle the permit is issued to | UC-19 | Seyed Moshtagh Moulaei |
| C08 | NotificationService | Reference class (Process 5.0): permit status change | UC-19 | Seyed Moshtagh Moulaei |

Class IDs are unique across the team. A class that one model references from another keeps its owner's ID and is marked as a reference class.

## Approved Classes (Consolidated Model)

| Class ID | Class | Source model | Store / process | Integration result |
|---|---|---|---|---|
| C01 | User (abstract) | Appeals, Violation Enforcement | D1 | Merged: one superclass for the four actors |
| C02 | PermitHolder | Appeals | D1 | Kept; vehiclePlates replaced by the owns association to Vehicle |
| C03 | AppealsOfficer | Appeals | D1 | Kept |
| C04 | Appeal | Appeals, Violation Enforcement | D4 | Merged; violationId replaced by the association to Violation |
| C05 | AppealEvidence | Appeals (Evidence) | D4 | Renamed from Evidence; now a subclass of Attachment |
| C06 | Decision | Appeals | D4 | Kept |
| C07 | AppealService | Appeals | Process 3.0 | Kept; isWithinWindow now takes a Violation |
| C08 | NotificationService | Appeals, Violation Enforcement | Process 5.0 | Merged: methods from both models plus permit status change |
| C09 | AppealStatus (enum) | Appeals | D4 | Kept |
| C10 | DecisionOutcome (enum) | Appeals | D4 | Kept |
| C11 | ParkingOfficer | Violation Enforcement | D1 | Kept |
| C12 | Administrator | Violation Enforcement, Permit Issuance | D1 | Merged: violation and permit methods in one class |
| C13 | Violation | Violation Enforcement | D3 | Kept |
| C14 | ViolationEvidence | Violation Enforcement | D3 | Kept; now a subclass of Attachment |
| C15 | VoidRecord | Violation Enforcement | D3 | Kept; voidedBy replaced by the records association to User |
| C16 | ViolationService | Violation Enforcement | Process 2.0 | Kept; voidViolation takes any authorised actor |
| C17 | Vehicle | Violation Enforcement | D1 | Kept; ownerId replaced by the owns association |
| C18 | Permit | Violation Enforcement, Permit Issuance | D2 | Merged: Permit Issuance version kept; extendExpiry() added for UC-08 |
| C19 | ViolationType (enum) | Violation Enforcement | D3 | Kept |
| C20 | Dashboard | App UI | UI | Kept |
| C21 | LoginPage | App UI | UI | Kept |
| C22 | AppealForm | App UI | UI | Kept; submits through AppealService |
| C23 | SearchFilter | App UI | UI | Kept; also used by ReportService |
| C24 | Page (abstract) | App UI | UI | Kept |
| C25 | Attachment (abstract) | Team | D3, D4 | Added: common superclass for both evidence classes |
| C26 | PermitApplication | Permit Issuance | D2 | Kept |
| C27 | PermitType | Permit Issuance | D2 | Kept |
| C28 | PermitService | Permit Issuance | Process 1.0 | Kept; submitApplication() and renewPermit() added for UC-06 and UC-08 |
| C29 | ReportService | Team | Process 4.0 | Added: missing service for Process 4.0 |
| C30 | ApplicationStatus (enum) | Permit Issuance | D2 | Kept |
| C31 | PermitStatus (enum) | Permit Issuance | D2 | Kept |
