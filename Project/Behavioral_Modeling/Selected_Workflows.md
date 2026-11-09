# Selected Workflows

## 1. Selected Workflows

The Activity Diagrams model the same use cases as the Lab 6 Sequence Diagrams.

| Use Case | Activity Diagram | Sequence Diagram (Lab 6) | Swimlanes | Parallel Activities |
|---|---|---|---|---|
| UC-01 Submit Appeal | `Activity_Diagrams/AD_UC01_Submit_Appeal.pdf` (`.png`, source `.puml`) | `Sequence_Diagrams/UC-01_Submit_Appeal.png` | Permit Holder, Appeal Form, Appeal Service, Violation Service, Notification Service | Send confirmation email and show confirmation |
| UC-12 Record Violation | `Activity_Diagrams/AD_UC12_Record_Violation.pdf` (`.png`, source `.puml`) | `Sequence_Diagrams/UC-12_Record_Violation.png` | Parking Officer, Violation Service, Notification Service | Notify permit holder or queue unmatched violation, and show recorded violation |
| UC-07 Manage Permit Application | `Activity_Diagrams/AD_UC07_Manage_Permit_Application.pdf` (`.png`, source `.puml`) | `Sequence_Diagrams/UC-07_Manage_Permit_Application.png` | Administrator, Permit Service, Notification Service | Notify permit holder of status change and show decision result |

## 2. Review and Validation

| # | Review Question | Result | Evidence |
|---|---|---|---|
| 1 | Does each Activity Diagram correspond to one of the use cases selected in Lab 6? | Yes | Figure 1: UC-01, Figure 2: UC-12, Figure 3: UC-07, the same use cases as the Lab 6 sequence diagrams. |
| 2 | Is the workflow consistent with the relevant functional requirements and use case description? | Yes | Figure 1: FR-01, FR-02, FR-05. Figure 2: FR-11, FR-12, FR-14, NFR-12. Figure 3: FR-17, FR-18, FR-19. All three: FR-10 (notifications). |
| 3 | Does the diagram contain a clearly identifiable initial node and final node? | Yes | One initial node per diagram. Two final nodes per diagram: one for the successful outcome and one for the refused, rejected or blocked outcome. |
| 4 | Are the actions named clearly and arranged in a logical order? | Yes | Actions are verb phrases, and checks come before changes: violation and 14-day window before the appeal is created, role check before the violation is created, quota check before the permit is issued. |
| 5 | Are control-flow arrows used correctly? | Yes | Each action has one incoming and one outgoing flow. Only decision, merge, fork and join nodes split or combine flows. |
| 6 | Are decision branches labeled with meaningful guard conditions? | Yes | Every outgoing decision flow has a guard, for example [valid] and [invalid], [within 14 days] and [more than 14 days], [authorised], [approved] and [rejected]. Each pair of guards is complete and mutually exclusive. |
| 7 | Do alternative paths lead to appropriate outcomes? | Yes | Refused appeals end with an error message, unauthorised recording ends with a logged rejection, and blocked issuance ends with the reason shown to the Administrator. |
| 8 | Are merge nodes used appropriately when alternative paths rejoin? | Yes | Figure 1: the two refusal paths merge before the error message. Figure 2: registered and unregistered plates merge before the officer review. Figure 3: rejected and approved paths merge before the notification. |
| 9 | Are fork and join nodes used correctly when parallel activities exist? | Yes | Each diagram forks the notification and the update shown to the actor, which run independently, and joins them before the final node. |
| 10 | Are swimlanes used appropriately to distinguish responsibilities, where needed? | Yes | One lane per actor and per system component, matching the Lab 6 lifelines. Each system action is in the lane of the class whose operation performs it (Action to Operation Mapping). |
| 11 | Are the modeled activities consistent with the system's intended behavior and the other project models? | Yes | Every system action maps to a Lab 5 class operation and a Lab 6 sequence message (Action to Operation Mapping). |
| 12 | Are there any missing activities, unnecessary steps, contradictory paths, or unreachable actions? | No | Every action is reachable from the initial node and every path ends in a final node. One contradiction with the Lab 6 UC-07 sequence diagram was found and fixed (Updates to Earlier Artifacts). |

## 3. Consistency with Previous Labs

The team has performed and verified all of the listed consistency checks with Lab 3, Lab 5 and Lab 6, and the 12 review questions above, for Figures 1 to 3. The results are recorded below.

| Lab | Check | Result | Evidence |
|---|---|---|---|
| Lab 3 | Each Activity Diagram reflects the relevant functional requirements and use case behavior | Verified | Requirements as in review question 2. Included and extending use cases appear as actions: UC-05 (verify violation record) and UC-02 (evidence loop) in Figure 1, UC-11 (plate lookup) in Figure 2, UC-18 (eligibility result) and UC-19 (issue permit) in Figure 3. |
| Lab 5 | Actions that correspond to system operations are compatible with class responsibilities | Verified | Every system action maps to an operation of the class that owns its swimlane, and every operation exists in the class diagram (Action to Operation Mapping). |
| Lab 6 | Each Activity Diagram represents the same use case as its Sequence Diagram, without contradictions | Verified | Same use cases, swimlanes match the lifelines, and decisions match the alt fragments and guards. The sequence diagrams show one valid order of the forked actions. UC-07 was revised so both diagrams cover an approved application that is not eligible. |

## 4. Action to Operation Mapping

Each system action, the Lab 5 class operation that performs it, and the matching message numbers in the Lab 6 sequence diagram of the same use case.

| Figure | System Action | Swimlane | Class Operation (Lab 5) | Sequence Message (Lab 6) |
|---|---|---|---|---|
| 1 | Validate form | Appeal Form | AppealForm.validateForm() | 2 |
| 1 | Highlight missing fields | Appeal Form | AppealForm.validateForm() (invalid result) | 2 |
| 1 | Submit appeal | Appeal Form | AppealService.submitAppeal() | 3 |
| 1 | Verify violation record | Appeal Service | AppealService.verifyViolationRecord() | 4 |
| 1 | Retrieve violation record | Violation Service | ViolationService.getViolation() | 5, 6 |
| 1 | Check 14-day window from issue date | Appeal Service | AppealService.isWithinWindow(), Violation.getIssuedAt() | 7, 8, 9 |
| 1 | Refuse appeal (no matching violation) | Appeal Service | AppealService.submitAppeal() (refused) | 10 |
| 1 | Refuse appeal (window has passed) | Appeal Service | AppealService.submitAppeal() (refused) | 12 |
| 1 | Show error message | Appeal Form | AppealForm.submitAppeal() (result shown) | 11, 13 |
| 1 | Create appeal (status SUBMITTED) | Appeal Service | Appeal constructor | 14 |
| 1 | Validate file type and size | Appeal Service | AppealEvidence.isValid() | 15, 16 |
| 1 | Add evidence to appeal | Appeal Service | Appeal.addEvidence() | 17 |
| 1 | Send confirmation email | Notification Service | NotificationService.sendSubmissionConfirmation() | 18 |
| 1 | Show confirmation | Appeal Form | AppealForm.submitAppeal() (result shown) | 19, 20 |
| 2 | Look up vehicle by plate | Violation Service | ViolationService.lookUpVehicle() | 1 |
| 2 | Check validity of each linked permit | Violation Service | Vehicle.getActivePermit(), Permit.isValid() | 2, 3, 4, 5 |
| 2 | Check account role | Violation Service | ViolationService.canRecord() | 8 |
| 2 | Reject and log attempt | Violation Service | ViolationService.recordViolation() (rejected) | 9 |
| 2 | Create violation with issue timestamp | Violation Service | ViolationService.recordViolation(), Violation constructor | 7, 10 |
| 2 | Notify permit holder | Notification Service | NotificationService.notifyViolationIssued() | 13 |
| 2 | Add to Administrator unmatched queue | Violation Service | Violation.isUnmatched(), ViolationService.listUnmatched() | 11, 12 |
| 3 | List pending applications | Permit Service | PermitService.listPending() | 1, 2 |
| 3 | Retrieve eligibility result and unmet criteria | Permit Service | PermitService.reviewEligibility(), PermitApplication.getUnmetCriteria() | 3, 4, 5, 6 |
| 3 | Set application status REJECTED | Permit Service | PermitApplication.setStatus() | 8 |
| 3 | Check eligibility and permit type quota | Permit Service | PermitType.hasQuotaRemaining() | 11, 12 |
| 3 | Block issuance and return reason | Permit Service | PermitService.decideApplication() (blocked) | 13 |
| 3 | Create permit (unique number, start and expiry dates) | Permit Service | PermitService.issuePermit(), Permit constructor | 14, 15 |
| 3 | Increment issued count | Permit Service | PermitType.incrementIssued() | 16 |
| 3 | Set application status APPROVED | Permit Service | PermitApplication.setStatus() | 17 |
| 3 | Notify permit holder of status change | Notification Service | NotificationService.notifyPermitStatusChange() | 9, 18 |

## 5. Updates to Earlier Artifacts

| Artifact | Change | Reason |
|---|---|---|
| Lab 6 sequence diagram UC-07 (Sequence_Diagrams/UC-07_Manage_Permit_Application) | Second alt operand changed from [approve = true and application eligible] to [approve = true]. Message 13 is now guarded by [not eligible or no quota remaining], and messages 14, 18 and 19 by [eligible and quotaRemaining]. | The activity diagram blocks issuance when an approved application is not eligible (FR-19). The sequence diagram did not cover that case. |
| Lab 5 class diagram (Object_Modeling/Class_Diagram.puml and Class_Diagram.png) | The 7 operations listed in Lab 6 (Class Model Updates) are now in the repository copy. | They were missing from the Lab 6 commit, while the sequence diagrams and this lab's mapping use them. |

_AI Usage Declaration: Claude (Anthropic) was used to generate the PlantUML source for the three activity diagrams and the revised UC-07 sequence diagram. The team reviewed and edited all output and is responsible for the final content._
