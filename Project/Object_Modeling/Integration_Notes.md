# Integration Notes

## 1. Duplicate Classes Identified and Resolved

| Duplicate or overlap | Found in | Resolution |
|---|---|---|
| User | Appeals (C01), Violation Enforcement (reference) | One abstract User; PermitHolder, AppealsOfficer, ParkingOfficer and Administrator inherit from it |
| Appeal | Appeals (C04), Violation Enforcement (reference) | Appeals version kept; the disputed by association from the Violation model is kept and Appeal.violationId is dropped |
| NotificationService | Appeals and Violation Enforcement (both reference) | One class with sendSubmissionConfirmation, notifyAppealStatusChange, notifyViolationIssued and notifyPermitStatusChange |
| Evidence and ViolationEvidence | Appeals (C05), Violation Enforcement (C14) | Same five fields and isValid(); moved into abstract Attachment, Evidence renamed AppealEvidence, capturedAt renamed uploadedAt |
| Permit | Violation Enforcement (reference C18), Permit Issuance (C18) | Permit Issuance version kept; the String permitType is replaced by the of type association to PermitType |
| Administrator | Violation Enforcement (C12), Permit Issuance (reference) | One Administrator with the violation methods and the permit configuration and decision methods |
| Owner of a vehicle | PermitHolder.vehiclePlates, Vehicle.ownerId | Both replaced by the association PermitHolder 1 owns 0..* Vehicle |
| Actor of a void | VoidRecord.voidedBy (String), Administrator records VoidRecord | Replaced by the association User 1 records 0..* VoidRecord |
| Appeal validation | AppealForm.validateForm(), AppealService | AppealForm checks input on the client only; AppealService enforces the rules |
| Redundant actor methods | Administrator.reviewUnmatched(), ParkingOfficer.attachPhoto(), PermitHolder.uploadEvidence() | Left out of the consolidated diagram; ViolationService and AppealService own this logic |

## 2. Major Integration Decisions

| # | Decision | Reason / affected artifacts |
|---|---|---|
| 1 | Appeals Committee is not modelled. An appeal has at most one Decision and AppealStatus has no ESCALATED value. | Matches the Lab 4 DFDs (Lab 4 issue 1). UC-05 and FR-05 are redefined as Verify Violation Record (the include in R-01), and NFR-02 now names Appeals Officers only. |
| 2 | Applicant and Permit Holder are one class, PermitHolder, with applyForPermit(). | Same stakeholder before and after a permit exists; matches the single DFD entity (Lab 4 issue 2). Use_Cases.md, Scenarios.md and FR-08, FR-10, FR-18, FR-19 now say Permit Holder. |
| 3 | Eligibility criteria and quota are stored in PermitType (D2) and set by Administrator.configureEligibility() and setQuota(). | Gives FR-16, FR-17, UC-16 and UC-17 a class and a store (Lab 4 issue 3). The Eligibility Criteria and Quota Settings flow is added to both DFDs (Figures 7 and 8). |
| 4 | An approved appeal voids the violation through ViolationService.voidViolation() with the Appeals Officer as actor. Manual voids stay Administrator only. | Process 3.0 outputs Violation Void Status to D3, while Process 2.0 allows only Administrators to void manually. VoidRecord now links to User. |
| 5 | A REDUCED decision stores the new amount in Decision.adjustedFine; Violation.fineAmount is never changed. | Keeps FR-15 (issued violations are never edited) while still supporting the reduce outcome of UC-04. |
| 6 | The Violation Enforcement model's reference Permit is merged into the Permit Issuance model's Permit (permitNumber, startDate, expiryDate, status). | Both describe the same D2 record; the Permit Issuance model owns it (FR-19, FR-20). |
| 7 | ReportService added for Process 4.0. It is read-only, used by the Administrator, and reuses SearchFilter. | Search and Report had no class in any individual model. |
| 8 | Evidence classes generalised under abstract Attachment; each subclass keeps its own isValid() rules. | Removes duplicated fields; limits differ (appeal: 3 PDF/JPG, violation: 5 JPG/PNG, 5 MB each). |
| 9 | UI classes kept as boundary classes under abstract Page and linked to services by dependencies only. | UI holds no business rules; AppealForm submits via AppealService and LoginPage calls User.authenticate(). |
| 10 | Class IDs renumbered so each class has one ID (C01 to C31). | Individual tables reused IDs (for example two classes were C01 and two were C08). |
| 11 | Renewal (UC-08) extends the same Permit through PermitService.renewPermit() and Permit.extendExpiry(). It is allowed only while the permit is ACTIVE, and eligibility is checked again. | Keeps the permit number; Process 1.0 rule 4 (renew before expiry) and rule 5 (renewal produces a Permit Status Change). |

## 3. Diagrams

- Individual models: `Individual_Models/` (PlantUML source and PNG per member)
- Consolidated model: `Class_Diagram.png` (source: `Class_Diagram.puml`)

All diagrams share one style: pink for actors (DFD external entities), lavender for the classes a model owns, white for reference classes and enums. Render the `.puml` files with PlantUML.

_AI tool declaration: Claude (Anthropic) was used to help draft the class inventory wording, the consolidation record and the consistency check, and to generate the PlantUML source for the diagrams. The team reviewed and edited all output and is responsible for the final content._
