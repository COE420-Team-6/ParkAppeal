# DFD Consistency and Balancing Check

## 1. Balancing: Context Diagram vs Level-0 DFD

Both diagrams use the same 4 external entities: Permit Holder, Parking Officer, Administrator, Appeals Officer. All 15 external data flows in the Context Diagram appear in the Level-0 DFD with the same name, the same entity and the same direction. No Level-0 flow to or from an external entity is missing from the Context Diagram.

| # | External entity | Data flow | Direction (relative to system) | Level-0 process | Result |
| --- | --- | --- | --- | --- | --- |
| 1 | Permit Holder | Permit Application Details | In | 1.0 | Balanced |
| 2 | Permit Holder | Appeal Submission and Evidence | In | 3.0 | Balanced |
| 3 | Permit Holder | Status Notification | Out | 5.0 | Balanced |
| 4 | Parking Officer | Licence Plate Enquiry | In | 2.0 | Balanced |
| 5 | Parking Officer | Violation Details and Evidence | In | 2.0 | Balanced |
| 6 | Parking Officer | Vehicle and Permit Status | Out | 2.0 | Balanced |
| 7 | Administrator | Search and Report Query | In | 4.0 | Balanced |
| 8 | Administrator | Permit Approval Decision | In | 1.0 | Balanced |
| 9 | Administrator | Violation Void Request | In | 2.0 | Balanced |
| 10 | Administrator | Search Results and Reports | Out | 4.0 | Balanced |
| 11 | Administrator | Pending Application List | Out | 1.0 | Balanced |
| 12 | Administrator | Unmatched Violation List | Out | 2.0 | Balanced |
| 13 | Appeals Officer | Appeal Decision and Justification | In | 3.0 | Balanced |
| 14 | Appeals Officer | Appeal Details and Evidence | Out | 3.0 | Balanced |
| 15 | Administrator | Eligibility Criteria and Quota Settings | In | 1.0 | Balanced |

Internal flows (process to process, process to data store) appear only in the Level-0 DFD, as expected.

## 2. Level-0 content

| Requirement | Level-0 DFD | Result |
| --- | --- | --- |
| At least 5 major processes | 5: 1.0 Manage Permit Applications, 2.0 Manage Parking Violations, 3.0 Process Appeals, 4.0 Search and Report, 5.0 Manage Notifications | Met |
| At least 2 data stores | 4: D1 User and Vehicle Registry, D2 Permit Records, D3 Violation Records, D4 Appeal Records | Met |
| Core Processes Matrix has the same processes | Same 5 processes, same numbers and names | Met |
| Context Diagram has no internal processes or stores | Only entities, one process and flows | Met |

## 3. Consistency with Lab 3 (Use Cases, Functional Requirements, Scope)

| Check | Status | Note |
| --- | --- | --- |
| Entities match Lab 3 Use Case actors | Met | Issues 1 and 2 resolved in Lab 5 |
| DFD processes cover the Functional Requirements and Use Cases | Met | Issue 3 resolved in Lab 5 |
| Notifications, search and reporting, violations, appeals covered | Met | 5.0, 4.0, 2.0, 3.0 (FR-01 to FR-04, FR-09 to FR-15) |
| Scope.md matches the actors used | Met | Issue 5 resolved in Lab 5 |

## 4. Open issues to settle before the progress discussion

1. **Appeals Committee is missing from both DFDs.** The Lab 3 documents still include it: UC-05 Escalate Appeal, FR-05, NFR-02, and the actor on the Lab 3 use case diagram ("Execute appeal"). Either (a) add the entity and two flows to the Context Diagram and Level-0 (Escalated Appeal Details out of 3.0, Final Appeal Decision into 3.0), or (b) remove it from Lab 3: delete UC-05 and FR-05, edit NFR-02, redraw the use case diagram. Lab 4 says the earlier documents must be updated when an inconsistency is found.
   **Resolved (Lab 5), option (b):** UC-05 and FR-05 are redefined as Verify Violation Record (the include in R-01), NFR-02 names appeals officers only. The use case diagram is redrawn without the Appeals Committee (Requirements/Use_Case_Diagram.png).
2. **"Applicant" and "Permit Holder" are two actors in Lab 3, one entity in the DFDs.** UC-06, UC-08 and UC-10 use Applicant; UC-01 to UC-03 use Permit Holder. The DFDs use Permit Holder for both. Either rename Applicant to Permit Holder in Use_Cases.md, Scenarios.md and the use case diagram, or justify in the report that Applicant is the same stakeholder before a permit exists.
   **Resolved (Lab 5):** Applicant renamed to Permit Holder in Use_Cases.md, Scenarios.md, FR-08, FR-10, FR-18 and FR-19, and on the redrawn use case diagram.
3. **Eligibility and quota configuration has no flow.** FR-16, FR-17 and UC-16, UC-17 (Administrator sets eligibility criteria and permit quotas) have no matching Administrator flow into 1.0 and no store for the rules. Add a flow such as Eligibility Criteria and Quota Settings (Administrator into 1.0) to both DFDs, and decide where the rules are stored (for example D2).
   **Resolved (Lab 5):** Eligibility Criteria and Quota Settings (Administrator into 1.0) is added to both DFDs, and Eligibility and Quota Rules links 1.0 and D2, where the rules are stored.
4. **D1 is never written.** D1 has only outgoing flows. Scope.md says user and vehicle data are seeded test data, so this can be defended, but state it in the report or add a flow into D1 (for example account registration).
5. **Scope.md and Project_Description.md say Administrators review appeals.** The DFDs and Lab 3 use cases use a separate Appeals Officer. Update both documents to match.
   **Resolved (Lab 5):** both documents now list Appeals officers as a separate user group.
6. **Minor.** UC-14 (link an unmatched violation to an account) and the Violation Void Request path into D3 are not shown as explicit flows.

## 5. Questions to be ready for in the progress discussion

- Context Diagram derivation: each entity is a Lab 3 actor; each flow is the data an actor exchanges in that actor's use cases.
- Level-0 process identification: one process per use case group (permits, violations, appeals, search and reporting, notifications).
- Matrix to DFD: the matrix rows are the 5 Level-0 processes, and its inputs and outputs are the Level-0 flow names.
