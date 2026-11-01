# Selected Use Cases

## 1. Selected Use Cases

| Use Case ID | Use Case Name | Primary Actor | Purpose | Reason for Selection |
|---|---|---|---|---|
| UC-01 | Submit Appeal | Permit Holder | Dispute a violation by filing an appeal within 14 days of issue, with a written reason and up to 3 attachments. | Core function of the system (Process 3.0). Covers the include UC-05 Verify Violation Record, the extend UC-02 Upload Evidence, and both scenarios S-01 (accepted) and S-02 (refused after 14 days). |
| UC-12 | Record Violation | Parking Officer | Issue a violation against a vehicle with a type, location and issue timestamp, after looking up the plate. | Creates the records that appeals dispute (Process 2.0). Covers the include UC-11 Look Up Vehicle by Plate, the role check (NFR-12) and the unmatched plate case (S-04, S-05). |
| UC-07 | Manage Permit Application | Administrator | Review a pending permit application and approve or reject it. | Central decision of permit issuance (Process 1.0). Covers the include UC-18 Review Eligibility Result, the extend UC-19 Issue Approved Permit and the quota check (FR-17 to FR-19, S-06). |

## 2. Sequence Diagrams

- Sequence Diagram for UC-01 Submit Appeal: `Sequence_Diagrams/UC-01_Submit_Appeal.png` (source: `UC-01_Submit_Appeal.puml`)
- Sequence Diagram for UC-12 Record Violation: `Sequence_Diagrams/UC-12_Record_Violation.png` (source: `UC-12_Record_Violation.puml`)
- Sequence Diagram for UC-07 Manage Permit Application: `Sequence_Diagrams/UC-07_Manage_Permit_Application.png` (source: `UC-07_Manage_Permit_Application.puml`)

## 3. Consistency Checklist

The team has performed and verified all consistency checks listed in A, B and C for Figures 1 to 3. The results are recorded below.

| Check | Status | Evidence |
|---|---|---|
| A. Each diagram represents one of the approved use cases | Verified | Figure 1: UC-01, Figure 2: UC-12, Figure 3: UC-07, all in Use_Cases.md (Lab 3). |
| A. The interaction supports the use case's goal | Verified | Each diagram ends with the goal reached: appeal SUBMITTED (Figure 1), violation stamped and stored (Figure 2), application decided and permit ACTIVE (Figure 3). |
| A. The sequence reflects the use case's description and flow | Verified | Includes and extends follow R-01 to R-05 (UC-05, UC-02, UC-11, UC-18, UC-19). Refusal paths follow S-02, S-05 and S-06. |
| A. The messages do not introduce unsupported functionality | Verified | Every rule traces to a requirement: 14-day window and 3 files (FR-01, FR-02), role check (NFR-12), unmatched plate (FR-14), eligibility and quota (FR-17 to FR-19), notifications (FR-10). |
| B. Participating objects correspond to classes in the Class Diagram | Verified | All 12 object classes and the 3 actors appear in the consolidated class diagram (Lab 5). |
| B. Message names correspond to appropriate class operations | Verified | All 28 call messages match an operation of the receiving class with the same parameters. create messages are constructors. |
| B. Messages are sent between plausible participants | Verified | Actors call only UI or service classes. Services call entities of their own process. Cross-process calls follow the Level-0 DFD flows (3.0 reads D3 through 2.0; 1.0, 2.0 and 3.0 send status changes to 5.0). |
| B. Required operations are in the class model or the model is updated | Verified | 7 operations were added to the class model (Class Model Updates below). |
| C. The interactions reflect the actual proposed system | Verified | The diagrams use the same processes (1.0, 2.0, 3.0, 5.0) and data stores as the Level-0 DFD (Lab 4). |
| C. The actor is consistent with the selected use case | Verified | Permit Holder (UC-01), Parking Officer (UC-12) and Administrator (UC-07), as in Use_Cases.md. |
| C. The sequence of messages is logical | Verified | Checks come before changes: form check before submission, violation and window check before the Appeal is created, role check before the Violation is created, quota check before the Permit is issued. |
| C. The diagrams are understandable and internally consistent | Verified | Same notation in all three: numbered messages, dashed returns, activation bars, * iteration, [] guards, alt for alternatives and dividers for included and extending use cases. |

## 4. Class Model Updates

The following operations were added to `Object_Modeling/Class_Diagram.puml` so that every message in the sequence diagrams is an operation of its receiving class.

| Operation | Class | Used in | Reason |
|---|---|---|---|
| verifyViolationRecord(violationId : String) : Violation | AppealService | Figure 1, message 4 | UC-05 and FR-05 had no operation. |
| getViolation(violationId : String) : Violation | ViolationService | Figure 1, message 5 | Process 3.0 reads the violation from D3 (DFD flow Violation Record and Evidence). |
| lookUpVehicle(plate : String) : Vehicle | ViolationService | Figure 2, message 1 | UC-11 and FR-11. It was in the Violation Enforcement model but left out at integration. |
| reviewEligibility(applicationId : String) : PermitApplication | PermitService | Figure 3, message 3 | UC-18 and FR-18. |
| getUnmetCriteria() : List&lt;String&gt; | PermitApplication | Figure 3, message 4 | FR-18 shows the unmet criteria to the Administrator. |
| decideApplication(applicationId : String, approve : boolean) : void | PermitService | Figure 3, message 7 | UC-07 had the decision only as an actor operation. |
| incrementIssued() : void | PermitType | Figure 3, message 16 | FR-17 quota count. It was in the Permit Issuance model but left out at integration. |

_AI Usage Declaration: Claude (Anthropic) was used to generate the PlantUML source for the three sequence diagrams and the updated class diagram. The team reviewed and edited all output and is responsible for the final content._
